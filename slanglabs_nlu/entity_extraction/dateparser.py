# Copyright (c) 2017-2022 Slang Labs Private Limited. All rights reserved.

import re
from calendar import monthrange
from datetime import datetime, timedelta

from slanglabs_nlu.entity_extraction.generated.DateListener import DateListener
from slanglabs_nlu.entity_extraction.generated.DateParser import DateParser

MOTY_MAP = {
    'jan': 'january',
    'feb': 'february',
    'mar': 'march',
    'apr': 'april',
    'may': 'may',
    'jun': 'june',
    'jul': 'july',
    'aug': 'august',
    'sep': 'september',
    'sept': 'september',
    'oct': 'october',
    'nov': 'november',
    'dec': 'december',
}


MOTY = [
    'january',
    'february',
    'march',
    'april',
    'may',
    'june',
    'july',
    'august',
    'september',
    'october',
    'november',
    'december'
]


DOTW = [
    'monday',
    'tuesday',
    'wednesday',
    'thursday',
    'friday',
    'saturday',
    'sunday',
]


def ord2card(c):
    try:
        suffixes = ['st', 'nd', 'rd', 'th']
        suffix = None
        for s in suffixes:
            if s in c:
                suffix = s
                break
        if suffix is None:
            return 0

        return int(c[:c.index(suffix)])
    except Exception:
        return -1


def ordstr2card(c):
    ords = [
        'first',
        'second',
        'third',
        'fourth',
        'fifth',
        'sixth',
        'seventh',
        'eighth',
        'ninth',
        'tenth',
        'eleventh',
        'twelfth',
        'thirteenth',
        'fourteenth',
        'fifteenth',
        'sixteenth',
        'seventeenth',
        'eighteenth',
        'nineteenth',
        'twentieth',
        'twenty first',
        'twenty second',
        'twenty third',
        'twenty fourth',
        'twenty fifth',
        'twenty sixth',
        'twenty seventh',
        'twenty eighth',
        'twenty ninth',
        'thirtieth',
        'thirty first',
    ]
    try:
        return ords.index(c) + 1 if c in ords else -1
    except Exception:
        return -1


def norm(c):
    if isinstance(c, list):
        return [norm(elem) for elem in c]
    return str(c).strip()


def months2days(year, month, num_months):
    days = 0
    n = num_months if num_months > 0 else -num_months
    incr = 1 if num_months > 0 else -1
    for _ in range(n):
        days += monthrange(year, month)[1]
        month += incr
        if month > 12:
            month = 1
            year += 1
        elif month < 1:
            month = 12
            year -= 1
    return days if num_months > 0 else -days


def is_valid(year=0, month=0, day=0):
    now = datetime.now()
    year = now.year if year == 0 else year
    month = now.month if month == 0 else month
    day = now.day if day == 0 else day

    try:
        datetime(year=year, month=month, day=day)
        return True
    except ValueError:
        return False


class DateExtractionListener(DateListener):
    def __init__(self, lexer, include_time=False, bias_to_future=True):
        now = datetime.now()
        self.lexer = lexer
        self.datetime = datetime(
            year=now.year,
            month=now.month,
            day=now.day,
            hour=0,
            minute=0,
            second=0
        )
        self.overflow_y = self.overflow_m = self.overflow_w = 0
        self.rel_y = self.rel_m = self.rel_w = self.rel_d = 0
        self.abs_y = self.abs_m = self.abs_w = self.abs_d = 0
        self.num_updates = 0
        self.result_validated = False

        self.prefix = []
        self.suffix = []
        self.results = []

        self.include_time = include_time
        self.bias_to_future = bias_to_future

    def reset(self):
        now = datetime.now()
        self.datetime = datetime(
            year=now.year,
            month=now.month,
            day=now.day,
            hour=0,
            minute=0,
            second=0
        )
        self.overflow_y = self.overflow_m = self.overflow_w = 0
        self.rel_y = self.rel_m = self.rel_w = self.rel_d = 0
        self.abs_y = self.abs_m = self.abs_w = self.abs_d = 0
        self.num_updates = 0
        self.result_validated = False

    def update(self, years=0, months=0, weeks=0, days=0, hours=0, minutes=0):
        if years != 0:
            days += (365 * years)

        if months != 0:
            m2d = months2days(self.datetime.year, self.datetime.month, months)
            days += m2d

        if weeks != 0:
            days += (7 * weeks)

        td = timedelta(days=days, hours=hours, minutes=minutes)
        self.datetime = self.datetime + td

    def update_relative(self, years=0, months=0, weeks=0, days=0):
        if years != 0:
            self.rel_y += years
            self.num_updates += 1

        if months != 0:
            self.rel_m += months
            self.num_updates += 1

        if weeks != 0:
            self.rel_w += weeks
            self.num_updates += 1

        if days != 0:
            self.rel_d += days
            self.num_updates += 1

    def set_absolute(self, year=0, month=0, week=0, day=0):
        if year != 0:
            self.abs_y = year
            self.num_updates += 1

        if month != 0:
            self.abs_m = month
            self.num_updates += 1

        if week != 0:
            self.abs_w = week
            self.num_updates += 1

        if day != 0:
            self.abs_d = day
            self.num_updates += 1

    def set(self, year=0, month=0, day=0, hour=0, minute=0):
        self.datetime = datetime(
            year=year if year > 0 else self.datetime.year,
            month=month if month > 0 else self.datetime.month,
            day=day if day > 0 else self.datetime.day,
            hour=hour if hour > 0 else self.datetime.hour,
            minute=minute if minute > 0 else self.datetime.minute,
        )

    def moty_index(self, s):
        s = MOTY_MAP[s] if s in MOTY_MAP else s
        return MOTY.index(s) + 1

    def enterUtterance(self, ctx: DateParser.UtteranceContext):
        self.reset()
        self.results = []
        self.prefix = []
        self.suffix = []

    def exitUtterance(self, ctx: DateParser.UtteranceContext):
        pass

    def enterPrefix(self, ctx: DateParser.PrefixContext):
        self.prefix.extend(norm(ctx.WORD()))

    def enterSuffix(self, ctx: DateParser.SuffixContext):
        self.suffix.extend(norm(ctx.WORD()))

    def enterDate_pattern(self, ctx: DateParser.Date_patternContext):
        self.reset()
        self.result_validated = False

    def exitDate_pattern(self, ctx: DateParser.Date_patternContext):
        try:
            if self.abs_y:
                self.set(year=self.abs_y, month=self.abs_m)
            else:
                self.update(years=self.rel_y)

            if self.abs_m:
                self.set(month=self.abs_m)
            else:
                self.update(months=self.rel_m)

            if self.abs_d:
                self.set(day=self.abs_d)
            else:
                self.update(days=self.rel_d)

            self.update(weeks=self.rel_w)

            datestr = '{}-{:02}-{:02}'.format(
                self.datetime.year,
                self.datetime.month,
                self.datetime.day
            )

            if self.include_time:
                datestr = '{} {:02}:{:02}:{:02}'.format(
                    datestr,
                    self.datetime.hour,
                    self.datetime.minute,
                    self.datetime.second,
                )
        except ValueError:
            # we know how to handle this invalid date, so
            # we mark it as validated
            self.result_validated = True
            year = 1970 if self.bias_to_future else 2070
            datestr = '{}-{:02}-{:02}'.format(year, 1, 1)
            if self.include_time:
                datestr = '{} {:02}:{:02}:{:02}'.format(datestr, 0, 0, 0)

        if self.result_validated:
            # normalize the returned indices to exclude spaces
            istream = self.lexer.inputStream
            text = istream.getText(0, istream.size)
            start = ctx.start.start
            stop = ctx.stop.stop
            while text[start] == ' ':
                start += 1
            while text[stop] == ' ':
                stop -= 1

            if stop >= start:
                self.results.append((datestr, (start, stop)))

    def exitLiteral_form(self, ctx: DateParser.Literal_formContext):
        pattern8 = '([0-9]{2})/?([0-9]{2})/?([0-9]{4})'
        pattern7_1 = '([0-9]{1})/?([0-9]{2})/?([0-9]{4})'
        pattern7_2 = '([0-9]{2})/?([0-9]{1})/?([0-9]{4})'

        number = ctx.DATE_NUMBER()

        if not number:
            return

        self.result_validated = True
        number = str(number)
        if len(number) == 8:
            match = re.match(pattern8, number)
            if match:
                self.abs_y = int(match.group(3))
                self.abs_m = int(match.group(2))
                self.abs_d = int(match.group(1))
        elif len(number) == 7:
            match1 = re.match(pattern7_1, number)
            match2 = re.match(pattern7_2, number)

            c1 = [
                int(match1.group(3)),
                int(match1.group(2)),
                int(match1.group(1)),
            ]

            c2 = [
                int(match2.group(3)),
                int(match2.group(2)),
                int(match2.group(1)),
            ]

            cur = [
                self.datetime.year,
                self.datetime.month,
                self.datetime.day
            ]

            winner = 0
            if not is_valid(c1[0], c1[1], c1[2]) \
                    and is_valid(c2[0], c2[1], c2[2]):
                winner = 2
            elif not is_valid(c2[0], c2[1], c2[2]) \
                    and is_valid(c1[0], c1[1], c1[2]):
                winner = 1
            elif not is_valid(c1[0], c1[1], c1[2]) \
                    and not is_valid(c2[0], c2[1], c2[2]):
                winner = 1

            if winner == 0:
                d1 = []
                d2 = []

                # prefer future, closer dates over past, farther dates
                # should probably be domain-specific and controlled by options
                for i in range(3):
                    d1.append(c1[i] - cur[i])
                    d2.append(c2[i] - cur[i])

                for i in range(3):
                    if d1[i] > 0 and d2[i] < 0:
                        winner = 1
                        break
                    elif d1[i] < 0 and d2[i] > 0:
                        winner = 2
                        break
                    elif d1[i] > 0 and d2[i] > 0:
                        if d1[i] != d2[-i]:
                            winner = 1 if d1[i] < d2[i] else 2
                            break
                    else:
                        if d1[i] != d2[i]:
                            winner = 1 if d1[i] > d2[i] else 2

            winner = 1 if winner == 0 else winner
            if winner == 1:
                self.set_absolute(year=c1[0], month=c1[1], day=c1[2])
            else:
                self.set_absolute(year=c2[0], month=c2[1], day=c2[2])

    def enterYear_form(self, ctx: DateParser.Year_formContext):
        self.num_updates = 0

    def exitYear_form(self, ctx: DateParser.Year_formContext):
        if self.abs_m == 0:
            self.set_absolute(month=1)

        if ctx.MOTY():
            moty_idx = self.moty_index(norm(ctx.MOTY()))
            self.set_absolute(month=moty_idx)

        if ctx.ORDINAL():
            card = ord2card(norm(ctx.ORDINAL()))
            self.set_absolute(day=card)
        elif ctx.ORDINALSTR():
            card = ordstr2card(norm(ctx.ORDINALSTR()))
            self.set_absolute(day=card)

        self.result_validated = True

    def exitYear(self, ctx: DateParser.YearContext):
        if ctx.LITERAL_YEAR():
            self.set_absolute(year=int(norm(ctx.LITERAL_YEAR())))
        elif ctx.NEXT_YEAR():
            self.update_relative(years=+1)
        elif ctx.PREV_YEAR():
            self.update_relative(years=-1)

    def enterMonth_form(self, ctx: DateParser.Month_formContext):
        self.overflow_y = 0
        self.num_updates = 0

    def exitMonth_form(self, ctx: DateParser.Month_formContext):
        self.result_validated = True
        child_updates = self.num_updates
        self.update_relative(years=self.overflow_y)

        if ctx.MOTY():
            moty_idx = self.moty_index(norm(ctx.MOTY()))
            self.set_absolute(month=moty_idx)
            if self.datetime.month > moty_idx:
                self.update_relative(years=1)
            if self.abs_d == -1:
                d = monthrange(
                    self.datetime.year + 1
                    if self.datetime.month > moty_idx
                    else self.datetime.year,
                    moty_idx
                )[1]
                self.set_absolute(day=d)

        card = None
        if ctx.ORDINAL():
            card = ord2card(norm(ctx.ORDINAL()))
        elif ctx.ORDINALSTR():
            card = ordstr2card(norm(ctx.ORDINALSTR()))
        elif ctx.NUMBER():
            card = int(norm(ctx.NUMBER()))

        y = self.datetime.year
        m = self.abs_m if self.abs_m != 0 else self.datetime.month
        d = self.datetime.day

        if card:
            if card <= 31:
                self.set_absolute(day=card)
                if child_updates == 0:
                    if d < card and not self.bias_to_future:
                        self.rel_m -= 1
                    elif d > card and self.bias_to_future:
                        self.rel_m += 1
                    elif self.abs_m == 0 and card > monthrange(y, m)[1]:
                        if card <= monthrange(y, m+1)[1] and self.bias_to_future:  # noqa
                            self.rel_m += 1
                        elif card <= monthrange(y, m-1)[1] and not self.bias_to_future:  # noqa
                            self.rel_m -= 1
            else:
                # If the moty if specified or if there are valid children,
                # mark this result as valid
                if ctx.MOTY() or child_updates > 0:
                    self.result_validated = True
                else:
                    self.result_validated = False

        if self.abs_d <= 0:
            self.set_absolute(day=1)

    def exitDouble_ordinal_month(self, ctx: DateParser.Double_ordinal_monthContext):  # noqa
        midx = 1 if str(ctx.getChild(1)) == 'month' else 2
        if midx == 1:
            mtmp = ctx.getChild(0)
            dtmp = ctx.getChild(2)
        else:
            mtmp = ctx.getChild(1)
            dtmp = ctx.getChild(0)

        m = ord2card(norm(mtmp))
        m = ordstr2card(norm(mtmp)) if m == -1 else m
        d = ord2card(norm(dtmp))
        d = ordstr2card(norm(dtmp)) if d == -1 else d
        self.set_absolute(month=m, day=d)

        if m < self.datetime.month \
                or m == self.datetime.month and d < self.datetime.day:
            self.update_relative(years=1)

    def exitMonth(self, ctx: DateParser.MonthContext):
        moty_idx = -1

        if not ctx.isEmpty():
            tokens = ctx.getText().split()
            for token in tokens:
                if token in MOTY:
                    moty_idx = self.moty_index(token)
                    self.set_absolute(month=moty_idx)
                    break

        moty = self.datetime.month
        if ctx.CURR_MONTH():
            self.set_absolute(month=self.datetime.month)
            if self.abs_d == -1:
                d = monthrange(self.datetime.year, self.datetime.month)[1]
                self.set_absolute(day=d)
        elif ctx.NEXT_MONTH():
            delta = (moty_idx - moty) if moty_idx > -1 else 1
            self.update_relative(months=delta)
            if self.rel_m < 0:
                self.overflow_y = 1
            if self.abs_d == -1:
                d = monthrange(
                    self.datetime.year + self.overflow_y,
                    self.datetime.month + delta
                )[1]
                self.set_absolute(day=d)
        elif ctx.PREV_MONTH():
            delta = (moty - moty_idx) if moty_idx > -1 else 1
            self.update_relative(months=-delta)
            if self.rel_m > 0:
                self.overflow_y = -1
            if self.abs_d == -1:
                d = monthrange(
                    self.datetime.year + self.overflow_y,
                    self.datetime.month + delta
                )[1]
                self.set_absolute(day=d)

    def exitLiteral_month(self, ctx: DateParser.Literal_monthContext):
        day = 1

        if ctx.NUMBER():
            day = int(str(ctx.NUMBER()))
        elif ctx.ORDINAL():
            day = ord2card(norm(ctx.ORDINAL()))
        elif ctx.ORDINALSTR():
            day = ordstr2card(norm(ctx.ORDINALSTR()))

        if ctx.MOTY():
            month = MOTY.index(norm(ctx.MOTY())) + 1
            self.set_absolute(month=month)

            if self.datetime.month > month \
                    or (self.datetime.month == month
                        and self.datetime.day >= day):
                if self.bias_to_future:
                    self.update_relative(years=1)

        if day:
            self.set_absolute(day=day)

    def exitRelative_month(self, ctx: DateParser.Relative_monthContext):
        delta = 1

        if ctx.NUMBER():
            delta = int(str(ctx.NUMBER()))
            self.result_validated = True

        if ctx.RELATIVE_MONTH_PREV():
            self.update_relative(months=-delta)
            self.set_absolute(day=self.datetime.day)
            self.result_validated = True
        elif ctx.RELATIVE_MONTH_NEXT() or ctx.RELATIVE_MONTH():
            self.update_relative(months=delta)
            self.set_absolute(day=self.datetime.day)
            self.result_validated = True

    def exitWeek_form(self, ctx: DateParser.Week_formContext):
        self.result_validated = True

    def exitWeek(self, ctx: DateParser.WeekContext):
        if ctx.NEXT_WEEK():
            self.update_relative(weeks=1)
        elif ctx.PREV_WEEK():
            self.update_relative(weeks=-1)
        elif ctx.NEXT_WEEKEND():
            delta = 5 - self.datetime.weekday()  # saturday = weekend
            if delta <= 0:
                self.update_relative(days=7+delta)
            else:
                self.update_relative(days=delta)

    def exitRelative_week(self, ctx: DateParser.Relative_weekContext):
        delta = 1

        if ctx.NUMBER():
            delta = int(str(ctx.NUMBER()))
            self.result_validated = True

        if 'fortnight' in ctx.getText().split():
            delta *= 2

        if ctx.RELATIVE_WEEK_PREV():
            self.update_relative(weeks=-delta)
            self.result_validated = True
        elif ctx.RELATIVE_WEEK_NEXT() or ctx.RELATIVE_WEEK():
            self.update_relative(weeks=delta)
            self.result_validated = True

    def enterDay_form(self, ctx: DateParser.Day_formContext):
        self.overflow_w = 0

    def exitDay_form(self, ctx: DateParser.Day_formContext):
        self.update_relative(weeks=self.overflow_w)
        self.result_validated = True

    def exitDay(self, ctx: DateParser.DayContext):
        dotw_idx = -1

        if not ctx.isEmpty():
            tokens = ctx.getText().split()
            for token in tokens:
                if token in DOTW:
                    dotw_idx = DOTW.index(token)
                    break

        dotw = self.datetime.weekday()
        if ctx.DOTW():
            delta = dotw_idx - dotw
            self.update_relative(days=delta)
        elif ctx.NEXT_DAY():
            if dotw_idx == -1:
                self.update_relative(days=1)
            else:
                delta = dotw_idx - dotw
                self.update_relative(days=delta+7)
                if delta < 0:
                    self.overflow_w = 1
        elif ctx.CURR_DAY():
            delta = (dotw_idx - dotw) if dotw_idx > -1 else 0
            if 'this' in ctx.getText().split():
                if delta < 0 and self.bias_to_future:
                    delta += 7
                elif 0 < delta < 7 and not self.bias_to_future:
                    delta -= 7
            self.update_relative(days=delta)
        elif ctx.PREV_DAY():
            # special case: last day of this month
            if 'last' in ctx.getText().split() and dotw_idx == -1:
                self.set_absolute(day=-1)
            else:
                delta = (dotw - dotw_idx) if dotw_idx > -1 else 1
                self.update_relative(days=-delta)
                if self.rel_d >= 0:
                    self.overflow_w = -1
        elif ctx.NEXT2_DAY():
            self.update_relative(days=2)
        elif ctx.PREV2_DAY():
            self.update_relative(days=-2)

    def exitRelative_day(self, ctx: DateParser.Relative_dayContext):
        delta = 1

        if ctx.NUMBER():
            delta = int(str(ctx.NUMBER()))
            self.result_validated = True

        if ctx.RELATIVE_DAY_NEXT() and 'after' in norm(ctx.RELATIVE_DAY_NEXT()):  # noqa
            self.update_relative(days=2)
            self.result_validated = True
        elif ctx.RELATIVE_DAY_PREV():
            self.update_relative(days=-delta)
            self.result_validated = True
        else:
            self.update_relative(days=delta)

    def enterTime(self, ctx: DateParser.TimeContext):
        t = ctx.TIME()
        n = ctx.NUMBER()
        if t:
            try:
                if ':' in norm(t):
                    d = datetime.strptime(norm(t), '%H:%M')
                else:
                    d = datetime.strptime(norm(t), '%H%M')
                self.set(hour=d.hour, minute=d.minute)
            except ValueError:
                h = int(str(t))
                if h < 13:
                    self.set(hour=h)
        elif n:
            try:
                d = datetime.strptime(norm(n), '%H%M')
                self.set(hour=d.hour, minute=d.minute)
            except ValueError:
                self.set(hour=int(str(n)))

    def exitTod(self, ctx: DateParser.TodContext):
        if ctx.getText() in ['pm', 'evening', 'night']:
            self.update(hours=12)


if __name__ == "__main__":
    val = 'september 31st'
    # print(parse_dates(val))
