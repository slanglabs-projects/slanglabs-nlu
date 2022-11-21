import datetime
from dateutil.relativedelta import relativedelta
import regex

from slanglabs_nlu.special_entities.abstract_special_entities import AbstractSpecialEntities, SpecialEntityRegexMatch  # noqa
from slanglabs_nlu.special_entities.common import before_words_regex, after_words_regex  # noqa

from slanglabs_nlu.special_entities.date_entities_constants import (
    months_dict, relative_day, relative_week, relative_month,
    relative_year, dow_dict, special_dates_dict, date_preps
)

day_date_cardinal_regex = "1st|2nd|3rd|[1-2][0-9]th|[4-9]th|21st|22nd|23rd|30th|31st"  # noqa
day_date_ordinal_regex = "30|31|[1-2][0-9]|[1-9]"
day_date_regex = '|'.join([day_date_cardinal_regex, day_date_ordinal_regex])
day_date_group_regex = "(?P<date>{})".format(day_date_regex)

dow_dict.update({k.lower(): v for k, v in dow_dict.items()})
date_preps_regex = '|'.join(date_preps)
date_preps_regex = '({})'.format(date_preps_regex)
dow_dict.update({' '.join([date_prep, k.lower()]): v for k, v in dow_dict.items() for date_prep in date_preps})  # noqa
dow_words_regex = '|'.join(dow_dict.keys())
months_dict.update({k.lower(): v for k, v in months_dict.items()})
relative_day_regex = '|'.join(relative_day.keys())
relative_day_group_regex = "(?<relative_day>{})".format(relative_day_regex)
relative_week_regex = '|'.join(relative_week.keys())
relative_week_group_regex = "(?<relative_week>{})".format(relative_week_regex)
relative_month_regex = '|'.join(relative_month.keys())
relative_month_group_regex = "(?<relative_month>{})".format(relative_month_regex)  # noqa
relative_year_regex = '|'.join(relative_year.keys())
relative_year_group_regex = "(?<relative_year>{})".format(relative_year_regex)
year_group_regex = "(?<year>[1-2][0-9]{3})"
month_words_regex = '|'.join(months_dict.keys())
month_ordinal_regex = '0?[1-9]|11|12'
month_regex = '|'.join([month_ordinal_regex, month_words_regex])
month_group_regex = "(?<month>{})".format(month_regex)
month_words_group_regex = "(?<month>{})".format(month_words_regex)
date_stop_words = "of"

# Duration
year_delta_before_group_regex = '((?P<year_delta_before>[0-9]+) years?)'
year_delta_after_group_regex = '((?P<year_delta_after>[0-9]+) years?)'
month_delta_before_group_regex = '((?P<month_delta_before>[0-9]+) months?)'
month_delta_after_group_regex = '((?P<month_delta_after>[0-9]+) months?)'
week_delta_before_group_regex = '((?P<week_delta_before>[0-9]+) weeks?)'
week_delta_after_group_regex = '((?P<week_delta_after>[0-9]+) weeks?)'
day_delta_before_group_regex = '((?P<day_delta_before>[0-9]+) days?)'
day_delta_after_group_regex = '((?P<day_delta_after>[0-9]+) days?)'

delta_after_regex = r"({}\s?(and )?{}?\s?(and )?{}?|{}\s?(and )?{}?|{})".format(  # noqa
    year_delta_after_group_regex, month_delta_after_group_regex, day_delta_after_group_regex,  # noqa
    month_delta_after_group_regex, day_delta_after_group_regex,
    day_delta_after_group_regex,
)
delta_before_regex = r"({}\s?(and )?{}?\s?(and )?{}?|{}\s?(and )?{}?|{})".format(  # noqa
    year_delta_before_group_regex, month_delta_before_group_regex, day_delta_before_group_regex,  # noqa
    month_delta_before_group_regex, day_delta_before_group_regex,
    day_delta_before_group_regex,
)

after_regex_1 = ' '.join([delta_after_regex, after_words_regex])
after_regex_2 = ' '.join([after_words_regex, delta_after_regex])
after_regex = '|'.join([after_regex_1, after_regex_2])
before_regex_1 = ' '.join([delta_before_regex, before_words_regex])
before_regex_2 = ' '.join([before_words_regex, delta_before_regex])
before_regex = '|'.join([before_regex_1, before_regex_2])

week_after_regex1 = ' '.join([week_delta_after_group_regex, after_words_regex])
week_after_regex2 = ' '.join([after_words_regex, week_delta_after_group_regex])
week_after_regex = '|'.join([week_after_regex1, week_after_regex2])
week_before_regex1 = ' '.join([week_delta_before_group_regex, before_words_regex])  # noqa
week_before_regex2 = ' '.join([before_words_regex, week_delta_before_group_regex])  # noqa
week_before_regex = '|'.join([week_before_regex1, week_before_regex2])

after_delta_keys = [
    'year_delta_after',
    'month_delta_after',
    'week_delta_after',
    'day_delta_after',
]

before_delta_key = [
    'year_delta_before',
    'month_delta_before',
    'week_delta_before',
    'day_delta_before',
]
delta_keys = after_delta_keys + before_delta_key

dow_future_words_regex = "(?<dow_future>{})".format('|'.join(dow_dict.keys()))
dow_past_words_regex = "(?<dow_past>{})".format('|'.join(dow_dict.keys()))
dow_future_regex = ' '.join([after_words_regex, dow_future_words_regex])
dow_past_regex = ' '.join([before_words_regex, dow_past_words_regex])
dow_regex = "(?<dow>{})".format('|'.join(dow_dict.keys()))
special_dates_regex = "(?<special_date>{})".format('|'.join(special_dates_dict.keys()))  # noqa


date_regex_list = [

        [date_preps_regex, day_date_group_regex, month_group_regex,
         year_group_regex],
        [date_preps_regex, month_group_regex, day_date_group_regex,
         year_group_regex],
        [date_preps_regex, day_date_group_regex, month_group_regex],
        [date_preps_regex, month_group_regex, day_date_group_regex],
        [date_preps_regex, day_date_group_regex, date_stop_words,
         month_group_regex, year_group_regex],
        [date_preps_regex, day_date_group_regex, date_stop_words,
         month_group_regex],
        [date_preps_regex, month_group_regex, year_group_regex],
        [date_preps_regex, day_date_group_regex, year_group_regex],

        [date_preps_regex, day_date_group_regex],
        [date_preps_regex, month_words_group_regex],
        [date_preps_regex, year_group_regex],

        [day_date_group_regex, month_group_regex, year_group_regex],
        [month_group_regex, day_date_group_regex, year_group_regex],
        [day_date_group_regex, month_group_regex],
        [month_group_regex, day_date_group_regex],
        [day_date_group_regex, date_stop_words, month_group_regex,
         year_group_regex],
        [day_date_group_regex, date_stop_words, month_group_regex],
        [month_group_regex, year_group_regex],
        [day_date_group_regex, year_group_regex],

        [day_date_group_regex, relative_month_group_regex],
        [relative_month_group_regex, day_date_group_regex],
        [dow_future_regex],
        [dow_past_regex],
        [dow_regex],
        [week_after_regex],
        [week_before_regex],
        [date_preps_regex, special_dates_regex],
        [after_regex_1, special_dates_regex],
        [before_regex_1, special_dates_regex],
        [after_regex],
        [before_regex],
        [day_date_group_regex],
        [month_words_group_regex],
        [year_group_regex],
        [relative_day_group_regex],
        [relative_week_group_regex],
        [relative_month_group_regex],
        [relative_year_group_regex],
    ]

date_regexes = [' '.join(i) for i in date_regex_list]


def today():
    return datetime.datetime.today()


class DateEntity(AbstractSpecialEntities):
    def __init__(self):
        super().__init__()
        self._regexes = date_regexes

    def name(self):
        return 'std.date'

    def _extract_date(self, date_match):
        found_pattern_list = regex.findall(r'[1-3]?[0-9]', date_match)
        for found_pattern in found_pattern_list:
            return self._make_two_digits(found_pattern)

    def _extract_special_date(self, groupdict):
        special_date = groupdict.get('special_date')
        special_dates_list = special_dates_dict.get(special_date)
        today_str = today().strftime('%Y-%m-%d')
        for i in range(len(special_dates_list) - 1):
            first = special_dates_list[i]
            second = special_dates_list[i + 1]
            if first < today_str <= second:
                return datetime.datetime.strptime(second, '%Y-%m-%d')
        return today()

    def _get_val(self, dictionary, key):
        val = dictionary.get(key, 0)
        if val is None:
            return 0
        else:
            return int(val)

    def _format_date(self, year, month, date):
        year = self._make_two_digits(year)
        month = self._make_two_digits(month)
        date = self._make_two_digits(date)
        return '{}-{}-{}'.format(year, month, date)

    def _extract_dow(self, groupdict):
        today_date = today()
        today_dow_number = today_date.weekday()
        if 'dow_future' in groupdict:
            dow_future = groupdict.get('dow_future')
            dow_number = dow_dict[dow_future]
            weeks = 1
            if dow_number > today_dow_number:
                weeks = 0
            required_date = today_date + datetime.timedelta(days=-today_dow_number + dow_number, weeks=weeks)  # noqa
            return required_date.strftime('%Y-%m-%d')
        if 'dow' in groupdict:
            dow_future = groupdict.get('dow')
            dow_number = dow_dict[dow_future]
            weeks = 1
            if dow_number > today_dow_number:
                weeks = 0
            required_date = today_date + datetime.timedelta(days=-today_dow_number + dow_number, weeks=weeks)  # noqa
            return required_date.strftime('%Y-%m-%d')
        if 'dow_past' in groupdict:
            dow_past = groupdict.get('dow_past')
            dow_number = dow_dict[dow_past]
            weeks = 1
            if dow_number < today_dow_number:
                weeks = 0
            required_date = today_date + datetime.timedelta(days=-today_dow_number + dow_number, weeks=-weeks)  # noqa
            return required_date.strftime('%Y-%m-%d')

    def _extract_relative_date(self, groupdict):
        required_date = today()
        if 'special_date' in groupdict:
            required_date = self._extract_special_date(groupdict)
        year_delta_after = self._get_val(groupdict, 'year_delta_after')
        month_delta_after = self._get_val(groupdict, 'month_delta_after')
        week_delta_after = self._get_val(groupdict, 'week_delta_after')
        day_delta_after = self._get_val(groupdict, 'day_delta_after')
        required_date = required_date + relativedelta(years=year_delta_after, months=month_delta_after, weeks=week_delta_after, days=day_delta_after)  # noqa
        year_delta_before = self._get_val(groupdict, 'year_delta_before')
        month_delta_before = self._get_val(groupdict, 'month_delta_before')
        week_delta_before = self._get_val(groupdict, 'week_delta_before')
        day_delta_before = self._get_val(groupdict, 'day_delta_before')
        required_date = required_date - relativedelta(years=year_delta_before, months=month_delta_before, weeks=week_delta_before, days=day_delta_before)  # noqa
        return required_date.strftime('%Y-%m-%d')

    def _extract_relative_days(self, relative_day_match):
        delta = relative_day.get(relative_day_match, 0)
        today_date = today()
        required_date = today_date + datetime.timedelta(days=delta)
        return required_date.strftime('%Y-%m-%d')

    def _extract_relative_weeks(self, relative_week_match):
        delta = relative_week.get(relative_week_match, 0)
        today_date = today()
        required_date = today_date + datetime.timedelta(weeks=delta)
        return required_date.strftime('%Y-%m-%d')

    def _extract_relative_months(self, relative_month_match):
        delta = relative_month.get(relative_month_match, 0)
        today_date = today()
        required_date = today_date + relativedelta(months=delta)
        return required_date.strftime('%Y-%m-%d')

    def _extract_relative_date_months(self, relative_month_match, date):
        date = self._extract_date(date)
        delta = relative_month.get(relative_month_match, 0)
        today_date = today()
        required_date = today_date + relativedelta(months=delta)
        required_date = required_date.replace(day=int(date))
        return required_date.strftime('%Y-%m-%d')

    def _extract_relative_years(self, relative_year_match):
        delta = relative_year.get(relative_year_match, 0)
        today_date = today()
        required_date = today_date + relativedelta(years=delta)
        return required_date.strftime('%Y-%m-%d')

    def _extract_month(self, month_match):
        month = None
        if month_match in months_dict:
            month = months_dict[month_match]
        elif month_match in months_dict.values():
            month = month_match
        else:
            current_month = today().month
            month = current_month
        return self._make_two_digits(month)

    def _extract_year(self, year_match):
        if year_match is None:
            current_year = today().year
            return current_year
        return year_match

    def _make_two_digits(self, value):
        if len(str(value)) == 1:
            return '0{}'.format(value)
        else:
            return value

    def normalize(self, found_pattern):
        groupdict = found_pattern.groupdict()
        deltas = [groupdict.get(i) for i in delta_keys]
        dows = [groupdict.get(i) for i in ['dow_future', 'dow_past', 'dow']]
        if any(dow is not None for dow in dows):
            return True, self._extract_dow(groupdict)
        if any(delta is not None for delta in deltas):
            return True, self._extract_relative_date(groupdict)
        if groupdict.get('relative_month') is not None and groupdict.get('date') is not None:  # noqa
            return True, self._extract_relative_date_months(groupdict.get('relative_month'), groupdict.get('date'))  # noqa
        if groupdict.get('relative_day') is not None:
            return True, self._extract_relative_days(groupdict.get('relative_day'))  # noqa
        if groupdict.get('relative_week') is not None:
            return True, self._extract_relative_weeks(groupdict.get('relative_week'))  # noqa
        if groupdict.get('relative_month') is not None:
            return True, self._extract_relative_months(groupdict.get('relative_month'))  # noqa
        if groupdict.get('relative_year') is not None:
            return True, self._extract_relative_years(groupdict.get('relative_year'))  # noqa
        if groupdict.get('special_date') is not None:
            full_date = self._extract_special_date(groupdict).strftime('%Y-%m-%d')  # noqa
            return True, full_date
        date = self._extract_date(groupdict.get('date', ''))
        if date is None:
            date = today().day
        month = self._extract_month(groupdict.get('month'))
        year = self._extract_year(groupdict.get('year'))
        return True, self._format_date(year, month, date)


class DateEntityFuture(DateEntity):
    def __init__(self):
        super().__init__()
        self._regexes = date_regexes

    def name(self):
        return 'std.date.future'

    def _extract_date(self, date_match):
        date = None
        found_pattern_list = regex.findall(r'[1-3]?[0-9]', date_match)
        for found_pattern in found_pattern_list:
            date = found_pattern
            break
        if date is not None:
            return int(date)
        return None

    def _extract_month(self, month_match):
        month = None
        if month_match in months_dict:
            month = months_dict[month_match]
            month = int(month)
        elif month_match in months_dict.values():
            month = month_match
            month = int(month)
        return month

    def _extract_year(self, year_match):
        if year_match is None:
            return year_match
        return int(year_match)

    def _use_full_date(self, date_value):
        return True
        # today_date = today()
        # today_date = today_date.strftime(r'%Y-%m-%d')
        # if today_date <= date_value:
        #     return True
        # else:
        #     return False

    def _use_year(self, year):
        today_year = today().year
        if today_year <= year:
            return True
        else:
            return False

    def _use_month_year(self, month, year):
        return True
        # today_year = today().year
        # today_month = today().month
        # if today_year == year and today_month <= month:
        #     return True
        # else:
        #     return False
        # if today_year <= year:
        #     return True
        # return False

    def _normalize_date_month(self, date, month):
        today_year = today().year
        today_month = today().month
        today_date = today().day
        year = today_year
        if month == today_month and date < today_date:
            year = today_year + 1
        if month < today_month:
            year = today_year + 1
        date = self._format_date(year, month, date)
        return True, date

    def _normalize_only_month(self, month):
        today_year = today().year
        today_month = today().month
        today_date = today().day
        if today_month <= month:
            return True, self._format_date(today_year, month, today_date)
        else:
            year = today_year + 1
            return True, self._format_date(year, month, today_date)

    def _normalize_only_date(self, date):
        today_year = today().year
        today_month = today().month
        today_date = today().day
        if date < today_date:
            temp_date = self._format_date(today_year, today_month, date)
            datetime_date = datetime.datetime.strptime(temp_date, r'%Y-%m-%d')
            date = datetime_date + relativedelta(years=0, months=1, days=0)
            return True, date.strftime(r'%Y-%m-%d')
        date = self._format_date(today_year, today_month, date)
        return True, date

    def normalize(self, found_pattern):
        groupdict = found_pattern.groupdict()
        deltas = [groupdict.get(i) for i in delta_keys]
        dows = [groupdict.get(i) for i in ['dow_future', 'dow_past', 'dow']]
        if any(dow is not None for dow in dows):
            full_date = self._extract_dow(groupdict)
            use = self._use_full_date(full_date)
            return use, full_date
        if any(delta is not None for delta in deltas):
            full_date = self._extract_relative_date(groupdict)
            use = self._use_full_date(full_date)
            return use, full_date
        if groupdict.get('relative_month') is not None and groupdict.get('date') is not None:  # noqa
            full_date = self._extract_relative_date_months(groupdict.get('relative_month'), groupdict.get('date'))  # noqa
            use = self._use_full_date(full_date)
            return use, full_date
        if groupdict.get('relative_day') is not None:
            full_date = self._extract_relative_days(groupdict.get('relative_day'))  # noqa
            use = self._use_full_date(full_date)
            return use, full_date
        if groupdict.get('relative_week') is not None:
            full_date = self._extract_relative_weeks(groupdict.get('relative_week'))  # noqa
            use = self._use_full_date(full_date)
            return use, full_date
        if groupdict.get('relative_month') is not None:
            full_date = self._extract_relative_months(groupdict.get('relative_month'))  # noqa
            use = self._use_full_date(full_date)
            return use, full_date
        if groupdict.get('relative_year') is not None:
            full_date = self._extract_relative_years(groupdict.get('relative_year'))  # noqa
            use = self._use_full_date(full_date)
            return use, full_date
        if groupdict.get('special_date') is not None:
            full_date = self._extract_special_date(groupdict).strftime('%Y-%m-%d')  # noqa
            use = self._use_full_date(full_date)
            return use, full_date
        date = self._extract_date(groupdict.get('date', ''))
        month = self._extract_month(groupdict.get('month'))
        year = self._extract_year(groupdict.get('year'))
        today_day = today().day
        today_month = today().month
        if all(i is not None for i in (date, month, year)):
            full_date = self._format_date(year, month, date)
            use = self._use_full_date(full_date)
            return use, full_date
        if all(i is not None for i in (month, year)):
            use = self._use_month_year(month, year)
            date = self._format_date(year, month, today_day)
            return use, date
        if year is not None:
            use = self._use_year(year)
            date = self._format_date(year, today_month, today_day)
            return use, date
        if all(i is not None for i in (date, month)):
            return self._normalize_date_month(date, month)
        if all(i is None for i in (date, year)) and month is not None:
            return self._normalize_only_month(month)
        if date is not None:
            return self._normalize_only_date(date)

    def extra_special_dates(self, text):
        special_fests = special_dates_dict.keys()
        for fest in special_fests:
            if fest in text.lower():
                return True
        return False

    def find_in_text(self, text):
        matching_regexes = []
        start_index2token_index, end_index2token_index = self.char_index2token_index(text)  # noqa
        spans = self._get_previous_spans(matching_regexes)
        for regex_pattern in self.regexes():
            found_patterns = regex.finditer(regex_pattern, text)
            for found_pattern in found_patterns:
                total_span = found_pattern.span()
                start_char_index = total_span[0]
                end_char_index = total_span[1] - 1
                use_regex = self._use_regex(start_index2token_index, end_index2token_index, start_char_index, end_char_index)  # noqa
                if self.extra_special_dates(text):
                    condition_flag = self.extra_special_dates(text[start_char_index: end_char_index + 1])   # noqa
                else:
                    condition_flag = self._is_not_overlap(spans, total_span)
                if use_regex and condition_flag:
                    spans.append(total_span)
                    start_token_index = start_index2token_index[start_char_index]  # noqa
                    end_token_index = end_index2token_index[end_char_index]
                    if all(i is not None for i in [start_token_index, end_token_index]):  # noqa
                        use, normalized_value = self.normalize(found_pattern)
                        special_entity_regex_match = SpecialEntityRegexMatch(
                            entitytype=self.name(),
                            start_token_index=start_token_index,
                            end_token_index=end_token_index,
                            start_char_index=start_char_index,
                            end_char_index=end_char_index,
                            use=use,
                            normalized_value=normalized_value,
                        )
                        matching_regexes.append(special_entity_regex_match)
        return matching_regexes


class DateEntityPast(DateEntity):
    def __init__(self):
        super().__init__()
        self._regexes = date_regexes

    def name(self):
        return 'std.date.past'

    def _extract_date(self, date_match):
        date = None
        found_pattern_list = regex.findall(r'[1-3]?[0-9]', date_match)
        for found_pattern in found_pattern_list:
            date = found_pattern
            break
        if date is not None:
            return int(date)
        return None

    def _extract_month(self, month_match):
        month = None
        if month_match in months_dict:
            month = months_dict[month_match]
            month = int(month)
        elif month_match in months_dict.values():
            month = month_match
            month = int(month)
        return month

    def _extract_year(self, year_match):
        if year_match is None:
            return year_match
        return int(year_match)

    def _use_full_date(self, date_value):
        today_date = today()
        today_date = today_date.strftime(r'%Y-%m-%d')
        if today_date >= date_value:
            return True
        else:
            return False

    def _use_year(self, year):
        today_year = today().year
        if today_year >= year:
            return True
        else:
            return False

    def _use_month_year(self, month, year):
        today_year = today().year
        today_month = today().month
        if today_year == year and today_month >= month:
            return True
        else:
            return False
        if today_year >= year:
            return True
        return False

    def _normalize_date_month(self, date, month):
        today_year = today().year
        today_month = today().month
        today_date = today().day
        year = today_year
        if month == today_month and date > today_date:
            year = today_year - 1
        if month > today_month:
            year = today_year - 1
        date = self._format_date(year, month, date)
        return True, date

    def _normalize_only_month(self, month):
        today_year = today().year
        today_month = today().month
        today_date = today().day
        if today_month >= month:
            return True, self._format_date(today_year, month, today_date)
        else:
            year = today_year - 1
            return True, self._format_date(year, month, today_date)

    def _normalize_only_date(self, date):
        today_year = today().year
        today_month = today().month
        today_date = today().day
        if date > today_date:
            temp_date = self._format_date(today_year, today_month, date)
            datetime_date = datetime.datetime.strptime(temp_date, r'%Y-%m-%d')
            date = datetime_date - relativedelta(years=0, months=1, days=0)
            return True, date.strftime(r'%Y-%m-%d')
        date = self._format_date(today_year, today_month, date)
        return True, date

    def _extract_special_date(self, groupdict):
        special_date = groupdict.get('special_date')
        special_dates_list = special_dates_dict.get(special_date)
        today_str = today().strftime('%Y-%m-%d')
        for i in range(len(special_dates_list) - 1):
            first = special_dates_list[i]
            second = special_dates_list[i + 1]
            if first <= today_str < second:
                return datetime.datetime.strptime(first, '%Y-%m-%d')
        return today()

    def normalize(self, found_pattern):
        groupdict = found_pattern.groupdict()
        deltas = [groupdict.get(i) for i in delta_keys]
        dows = [groupdict.get(i) for i in ['dow_future', 'dow_past', 'dow']]
        if any(dow is not None for dow in dows):
            full_date = self._extract_dow(groupdict)
            use = self._use_full_date(full_date)
            return use, full_date
        if any(delta is not None for delta in deltas):
            full_date = self._extract_relative_date(groupdict)
            use = self._use_full_date(full_date)
            return use, full_date
        if groupdict.get('relative_month') is not None and groupdict.get('date') is not None:  # noqa
            full_date = self._extract_relative_date_months(groupdict.get('relative_month'), groupdict.get('date'))  # noqa
            use = self._use_full_date(full_date)
            return use, full_date
        if groupdict.get('relative_day') is not None:
            full_date = self._extract_relative_days(groupdict.get('relative_day'))  # noqa
            use = self._use_full_date(full_date)
            return use, full_date
        if groupdict.get('relative_week') is not None:
            full_date = self._extract_relative_weeks(groupdict.get('relative_week'))  # noqa
            use = self._use_full_date(full_date)
            return use, full_date
        if groupdict.get('relative_month') is not None:
            full_date = self._extract_relative_months(groupdict.get('relative_month'))  # noqa
            use = self._use_full_date(full_date)
            return use, full_date
        if groupdict.get('relative_year') is not None:
            full_date = self._extract_relative_years(groupdict.get('relative_year'))  # noqa
            use = self._use_full_date(full_date)
            return use, full_date
        if groupdict.get('special_date') is not None:
            full_date = self._extract_special_date(groupdict).strftime('%Y-%m-%d')  # noqa
            use = self._use_full_date(full_date)
            return use, full_date
        date = self._extract_date(groupdict.get('date', ''))
        month = self._extract_month(groupdict.get('month'))
        year = self._extract_year(groupdict.get('year'))
        today_day = today().day
        today_month = today().month
        if all(i is not None for i in (date, month, year)):
            full_date = self._format_date(year, month, date)
            use = self._use_full_date(full_date)
            return use, full_date
        if all(i is not None for i in (month, year)):
            use = self._use_month_year(month, year)
            date = self._format_date(year, month, today_day)
            return use, date
        if year is not None:
            use = self._use_year(year)
            date = self._format_date(year, today_month, today_day)
            return use, date
        if all(i is not None for i in (date, month)):
            return self._normalize_date_month(date, month)
        if all(i is None for i in (date, year)) and month is not None:
            return self._normalize_only_month(month)
        if date is not None:
            return self._normalize_only_date(date)

    def extra_special_dates(self, text):
        special_fests = special_dates_dict.keys()
        for fest in special_fests:
            if fest in text.lower():
                return True
        return False

    def find_in_text(self, text):
        matching_regexes = []
        start_index2token_index, end_index2token_index = self.char_index2token_index(text)  # noqa
        spans = self._get_previous_spans(matching_regexes)
        for regex_pattern in self.regexes():
            found_patterns = regex.finditer(regex_pattern, text)
            for found_pattern in found_patterns:
                total_span = found_pattern.span()
                start_char_index = total_span[0]
                end_char_index = total_span[1] - 1
                use_regex = self._use_regex(start_index2token_index, end_index2token_index, start_char_index, end_char_index)  # noqa
                if self.extra_special_dates(text):
                    condition_flag = self.extra_special_dates(text[start_char_index: end_char_index + 1])   # noqa
                else:
                    condition_flag = self._is_not_overlap(spans, total_span)
                if use_regex and condition_flag:
                    spans.append(total_span)
                    start_token_index = start_index2token_index[start_char_index]  # noqa
                    end_token_index = end_index2token_index[end_char_index]
                    if all(i is not None for i in [start_token_index, end_token_index]):  # noqa
                        use, normalized_value = self.normalize(found_pattern)
                        special_entity_regex_match = SpecialEntityRegexMatch(
                            entitytype=self.name(),
                            start_token_index=start_token_index,
                            end_token_index=end_token_index,
                            start_char_index=start_char_index,
                            end_char_index=end_char_index,
                            use=use,
                            normalized_value=normalized_value,
                        )
                        matching_regexes.append(special_entity_regex_match)
        return matching_regexes
