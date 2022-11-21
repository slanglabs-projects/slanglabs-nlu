import datetime

from slanglabs_nlu.special_entities.abstract_special_entities import\
    AbstractSpecialEntities
from slanglabs_nlu.special_entities.common import before_words_regex, after_words_regex  # noqa


# To implement:
# Half an hour
# Two and a half hours later

time_cardinal_regex = r"(?P<hour>10|11|12|[1-9])\:?(?P<minute>[0-5][0-9])?"
am_pm_regex = r"((?P<am>a\.m\.|am|a\.m)|(?P<pm>p\.m\.|pm|p\.m))"
o_clock_regex = "(?<hour>10|11|12|[1-9]) o'clock"
time_am_pm_regex = r'({} {}|{} {}|{}|{})'.format(
    time_cardinal_regex, am_pm_regex,
    o_clock_regex, am_pm_regex,
    o_clock_regex,
    time_cardinal_regex,
)

time_regex = time_am_pm_regex

# Relative
after_relative_millisecond_regex = '((?P<after_relative_millisecond>[0-9]+) milliseconds?)'  # noqa
after_relative_second_regex = '((?P<after_relative_second>[0-9]+) seconds?)'
after_relative_minute_regex = '((?P<after_relative_minute>[0-9]+) minutes?)'
after_relative_hour_regex = '((?P<after_relative_hour>[0-9]+) hours?)'
after_relative_duration_regex = r"({}\s?(and )?{}?\s?(and )?{}?\s?(and )?{}?|{}\s?(and )?{}?\s?(and )?{}?|{}\s?(and )?{}?|{})".format(  # noqa
    after_relative_hour_regex, after_relative_minute_regex, after_relative_second_regex, after_relative_millisecond_regex,  # noqa
    after_relative_minute_regex, after_relative_second_regex, after_relative_millisecond_regex,  # noqa
    after_relative_second_regex, after_relative_millisecond_regex,
    after_relative_millisecond_regex
)

before_relative_millisecond_regex = '((?P<before_relative_millisecond>[0-9]+) milliseconds?)'  # noqa
before_relative_second_regex = '((?P<before_relative_second>[0-9]+) seconds?)'
before_relative_minute_regex = '((?P<before_relative_minute>[0-9]+) minutes?)'
before_relative_hour_regex = '((?P<before_relative_hour>[0-9]+) hours?)'
before_relative_duration_regex = r"({}\s?(and )?{}?\s?(and )?{}?\s?(and )?{}?|{}\s?(and )?{}?\s?(and )?{}?|{}\s?(and )?{}?|{})".format(  # noqa
    before_relative_hour_regex, before_relative_minute_regex, before_relative_second_regex, before_relative_millisecond_regex,  # noqa
    before_relative_minute_regex, before_relative_second_regex, before_relative_millisecond_regex,  # noqa
    before_relative_second_regex, before_relative_millisecond_regex,
    before_relative_millisecond_regex
)

after_regex_1 = ' '.join([after_relative_duration_regex, after_words_regex])
after_regex_2 = ' '.join([after_words_regex, after_relative_duration_regex])
after_regex = '({}|{})'.format(after_regex_1, after_regex_2)
before_regex_1 = ' '.join([before_relative_duration_regex, before_words_regex])
before_regex_2 = ' '.join([before_words_regex, before_relative_duration_regex])
before_regex = '({}|{})'.format(before_regex_1, before_regex_2)
after_time_regex = ' '.join([after_regex, time_am_pm_regex])
before_time_regex = ' '.join([before_regex, time_am_pm_regex])

time_regex_list = [
        [after_time_regex],
        [before_time_regex],
        [after_regex],
        [before_regex],
        [time_regex],
    ]

time_regexes = [' '.join(i) for i in time_regex_list]


class TimeEntity(AbstractSpecialEntities):
    def __init__(self):
        super().__init__()
        self._regexes = time_regexes

    def name(self):
        return 'std.time'

    def _make_two_digits(self, value):
        if value is None:
            return '00'
        if len(str(value)) == 1:
            return '0{}'.format(value)
        else:
            return value

    def get_hours(self, groupdict):
        hours = groupdict.get('hour')
        if hours is None:
            return None
        if groupdict.get('pm') is not None:
            int_hours = int(hours)
            if 0 < int(hours) < 12:
                hours = int_hours + 12
        if groupdict.get('am') is not None:
            if int(hours) == 12:
                hours = 0
        return int(hours)

    def get_normalized_time_dict(self, groupdict):
        hours = self.get_hours(groupdict)
        minutes = int(groupdict.get('minute', 0))
        if hours is None:
            req_time = datetime.datetime.now().time()
        else:
            req_time = datetime.time(hour=hours, minute=minutes)

        before_relative_hours = int(groupdict.get('before_relative_hour', 0))
        before_relative_minutes = int(groupdict.get('before_relative_minute', 0))  # noqa
        before_relative_seconds = int(groupdict.get('before_relative_second', 0))  # noqa
        before_relative_milliseconds = int(groupdict.get('before_relative_millisecond', 0))  # noqa

        timedelta = datetime.timedelta(
            hours=before_relative_hours,
            minutes=before_relative_minutes,
            seconds=before_relative_seconds,
            milliseconds=before_relative_milliseconds
        )
        req_time = (datetime.datetime.combine(datetime.date(10, 10, 10), req_time) - timedelta).time()  # noqa

        after_relative_hours = int(groupdict.get('after_relative_hour', 0))
        after_relative_minutes = int(groupdict.get('after_relative_minute', 0))
        after_relative_seconds = int(groupdict.get('after_relative_second', 0))
        after_relative_milliseconds = int(groupdict.get('after_relative_millisecond', 0))  # noqa

        timedelta = datetime.timedelta(
            hours=after_relative_hours,
            minutes=after_relative_minutes,
            seconds=after_relative_seconds,
            milliseconds=after_relative_milliseconds
        )
        req_time = (datetime.datetime.combine(datetime.date(10, 10, 10), req_time) + timedelta).time()  # noqa

        hours = req_time.hour
        minutes = req_time.minute
        seconds = req_time.second

        return {"hours": hours, "minutes": minutes, "seconds": seconds}

    def format_time(self, time_dict):
        hours = time_dict.get('hours')
        hours = self._make_two_digits(hours)
        minutes = time_dict.get('minutes')
        minutes = self._make_two_digits(minutes)
        seconds = time_dict.get('seconds')
        seconds = self._make_two_digits(seconds)
        return '{}:{}:{}'.format(hours, minutes, seconds)

    def normalize(self, found_pattern):
        groupdict = found_pattern.groupdict()
        groupdict = {k: v for k, v in groupdict.items() if v is not None}
        time_dict = self.get_normalized_time_dict(groupdict)
        return True, self.format_time(time_dict)
