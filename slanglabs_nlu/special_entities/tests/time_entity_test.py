import datetime
import unittest

from slanglabs_nlu.special_entities.time_entity import TimeEntity


class TimeEntityTest(unittest.TestCase):
    def setUp(self):
        self.time_entity = TimeEntity()

    def test_time(self):
        time2normalized = {
            "1 o'clock": "01:00:00",
            "2 o'clock": "02:00:00",
            "3 o'clock": "03:00:00",
            "4 p.m.": "16:00:00",
            "5 a.m": "05:00:00",
            "6 pm": "18:00:00",
            "7:45": "07:45:00",
            "7:45 am": "07:45:00",
            "8:00 pm": "20:00:00",
            "21:00": "21:00:00",
            "10 o'clock": "10:00:00",
            "11 o'clock pm": "23:00:00",
            "12 o'clock am": "00:00:00",
        }

        for text, ans in time2normalized.items():
            for regex in self.time_entity.find_in_text(text):
                self.assertEqual(regex.normalized_value(), ans)

    def test_after_before_time_anchor_time(self):
        time2normalized = {
            "10 minutes after 2 o'clock": "02:10:00",
            "2 minutes before 3 o'clock pm": "14:58:00",
            "30 minutes before 7:40": "07:10:00",
            "5 minutes past 7": "07:05:00",
            "6 seconds past 6": "06:00:06",
            "2 hours 30 minutes past 5": "07:30:00",
            "2 minutes past 11:59 pm": "00:01:00",
            "2 minutes before 12:01 am": "23:59:00"
        }
        for text, ans in time2normalized.items():
            for regex in self.time_entity.find_in_text(text):
                self.assertEqual(regex.normalized_value(), ans)

    def _make_two_digits(self, value):
        if value is None:
            return '00'
        if len(str(value)) == 1:
            return '0{}'.format(value)
        else:
            return value

    def test_after_time_now(self):
        time2normalized = {
            "10 minutes later": "00:10:00",
            "2 seconds after": "00:00:02",
            "2 hours 30 minutes after": "02:30:00",
        }
        for text, ans in time2normalized.items():
            for regex in self.time_entity.find_in_text(text):
                hours, minutes, seconds = [int(i) for i in ans.split(':')]
                timedelta = datetime.timedelta(
                    hours=hours,
                    minutes=minutes,
                    seconds=seconds,
                )
                expected_time = (datetime.datetime.now() + timedelta).time()
                hour = self._make_two_digits(expected_time.hour)
                minute = self._make_two_digits(expected_time.minute)
                second = self._make_two_digits(expected_time.second)
                expected_time = "{}:{}:{}".format(hour, minute, second)
                self.assertEqual(regex.normalized_value(), expected_time)

    def test_before_time_now(self):
        time2normalized = {
            "10 minutes ago": "00:10:00",
            "2 seconds before": "00:00:02",
            "2 hours 30 minutes previous": "02:30:00",
        }
        for text, ans in time2normalized.items():
            for regex in self.time_entity.find_in_text(text):
                hours, minutes, seconds = [int(i) for i in ans.split(':')]
                timedelta = datetime.timedelta(
                    hours=hours,
                    minutes=minutes,
                    seconds=seconds,
                )
                expected_time = (datetime.datetime.now() - timedelta).time()
                hour = self._make_two_digits(expected_time.hour)
                minute = self._make_two_digits(expected_time.minute)
                second = self._make_two_digits(expected_time.second)
                expected_time = "{}:{}:{}".format(hour, minute, second)
                self.assertEqual(regex.normalized_value(), expected_time)


if __name__ == '__main__':
    unittest.main()
