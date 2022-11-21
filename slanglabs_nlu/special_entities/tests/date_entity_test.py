import datetime
from dateutil.relativedelta import relativedelta
import unittest
from unittest.mock import patch
from slanglabs_nlu.special_entities.date_entity import DateEntity, DateEntityFuture, DateEntityPast  # noqa


def today():
    return datetime.datetime.strptime('2020-06-15', r'%Y-%m-%d')


class DateEntityTest(unittest.TestCase):
    def setUp(self):
        self.date_entity = DateEntity()

    @patch('slanglabs_nlu.special_entities.date_entity.today', side_effect=today)  # noqa
    def test_date(self, mock_today):
        date2normalized = {
            "April 4th": (True, "2020-04-04"),
            "5th June 2009": (True, "2009-06-05"),
            "October 6th 1992": (True, "1992-10-06"),
            "22nd of Jan": (True, "2020-01-22"),
            "june 7": (True, "2020-06-07"),
            "8 Sep": (True, "2020-09-08"),
            "july 19 2019": (True, "2019-07-19"),
            "deliver on june 20th": (True, "2020-06-20"),
            "deliver on 20th": (True, "2020-06-20"),
            "deliver on 15th": (True, "2020-06-15"),
            "deliver on 14th": (True, "2020-06-14"),
            "now": (True, "2020-06-15"),
            "today": (True, "2020-06-15"),
            "deliver on October 2020": (True, "2020-10-15"),
            "deliver on April 2020": (True, "2020-04-15"),
            "deliver on July 2020": (True, "2020-07-15"),
            "deliver in October": (True, "2020-10-15"),
            "deliver in June": (True, "2020-06-15"),
            "deliver in April": (True, "2020-04-15"),
            "deliver in 2020": (True, "2020-06-15"),
            "deliver in 2021": (True, "2021-06-15"),
            "deliver in 2019": (True, "2019-06-15"),
            "deliver on coming monday": (True, "2020-06-22"),
            "deliver on monday": (True, "2020-06-22"),
            "deliver on next tuesday": (True, "2020-06-16"),
            "deliver on previous wednesday": (True, "2020-06-10"),
            "deliver on previous thursday": (True, "2020-06-11"),
            "deliver 2 weeks later": (True, "2020-06-29"),
            "deliver 3 weeks later": (True, "2020-07-06"),
            "deliver 2 weeks ago": (True, "2020-06-01"),
            "1st next month": (True, "2020-07-01"),
            "20th last month": (True, "2020-05-20"),
            "on 25 October": (True, "2020-10-25"),
            "on 6th October": (True, "2020-10-06"),
        }

        for text, (use, ans) in date2normalized.items():
            for regex in self.date_entity.find_in_text(text):
                self.assertEqual(regex.use(), use, msg=text)
                self.assertEqual(regex.normalized_value(), ans, msg=text)

    def test_relative_date_forward(self):
        current_day = datetime.datetime.now()
        date2normalized = {
            "tomorrow": "00:00:01",
            "day after tomorrow": "00:00:02",
            "next month": "00:01:00",
            "next year": "01:00:00",
            "2 days later": "00:00:02",
            "3 months later": "00:03:00",
            "4 years later": "04:00:00",
            "3 days from today": "00:00:03",
            "3 month 2 days from today": "00:03:02",
            "now": "00:00:00",
            "today": "00:00:00",
            "deliver day after tomorrow to my house": "00:00:02",
            "next year": "01:00:00",
            "next month": "00:01:00",
        }
        for text, ans in date2normalized.items():
            for regex in self.date_entity.find_in_text(text):
                years_delta, months_delta, days_delta = [int(i) for i in ans.split(':')]  # noqa
                datedelta = relativedelta(
                    years=years_delta,
                    months=months_delta,
                    days=days_delta,
                )
                expected_date = current_day + datedelta
                formated_expected_date = expected_date.strftime("%Y-%m-%d")
                self.assertEqual(regex.normalized_value(), formated_expected_date, msg=text)  # noqa

    def test_relative_date_backward(self):
        current_day = datetime.datetime.now()
        date2normalized = {
            "yesterday": "00:00:01",
            "day before yesterday": "00:00:02",
            "last month": "00:01:00",
            "last year": "01:00:00",
            "2 days ago": "00:00:02",
            "3 months before": "00:03:00",
            "4 years previous": "04:00:00",
            "3 days before today": "00:00:03",
            "flew my plane day before yesterday": "00:00:02",
            "last year": "01:00:00",
            "last month": "00:01:00",
        }
        for text, ans in date2normalized.items():
            for regex in self.date_entity.find_in_text(text):
                years_delta, months_delta, days_delta = [int(i) for i in ans.split(':')]  # noqa
                datedelta = relativedelta(
                    years=years_delta,
                    months=months_delta,
                    days=days_delta,
                )
                expected_date = current_day - datedelta
                formated_expected_date = expected_date.strftime("%Y-%m-%d")
                self.assertEqual(regex.normalized_value(), formated_expected_date, msg=text)  # noqa


class FutureDateEntityTest(unittest.TestCase):
    def setUp(self):
        self.date_entity = DateEntityFuture()

    @patch('slanglabs_nlu.special_entities.date_entity.today', side_effect=today)  # noqa
    def test_date(self, mock_datetime_now):
        date2normalized = {
            "on christmas": (True, "2020-12-25"),
            "on new year's": (True, "2021-01-01"),
            "on new year's eve": (True, "2020-12-31"),
            "on thanksgiving": (True, "2020-11-26"),
            "on republic day": (True, "2021-01-26"),
            "on independence day": (True, "2020-08-15"),
            "on gandhi jayanti": (True, "2020-10-02"),
            "on may day": (True, "2021-05-01"),
            "on diwali": (True, "2020-11-14"),
            "on deepavali": (True, "2020-11-14"),
            "on deepawali": (True, "2020-11-14"),
            "on ganesh chaturti": (True, "2020-08-22"),
            "on ganesh pooja": (True, "2020-08-22"),
            "on ganesha pooja": (True, "2020-08-22"),
            "on krishna jayanti": (True, "2020-08-11"),
            "on krishna janmashatami": (True, "2020-08-11"),
            "on krishna pooja": (True, "2020-08-11"),
            "on easter": (True, "2021-04-04"),
            "on good friday": (True, "2021-04-02"),
            "on eid": (True, "2021-07-21"),
            "on muharam": (True, "2020-08-20"),
            "on milad un nabi": (True, "2020-10-29"),
            "on memorial day": (True, "2021-05-30"),
            "on labor day": (True, "2020-09-07"),
            "on veteran's day": (True, "2020-11-11"),
            "April 4th": (True, "2021-04-04"),
            "5th June 2009": (True, "2009-06-05"),
            "October 6th 1992": (True, "1992-10-06"),
            "22nd of Jan": (True, "2021-01-22"),
            "june 7": (True, "2021-06-07"),
            "8 Sep": (True, "2020-09-08"),
            "july 19 2019": (True, "2019-07-19"),
            "deliver on june 20th": (True, "2020-06-20"),
            "deliver on 20th": (True, "2020-06-20"),
            "deliver on 15th": (True, "2020-06-15"),
            "deliver on 14th": (True, "2020-07-14"),
            "now": (True, "2020-06-15"),
            "today": (True, "2020-06-15"),
            "deliver on October 2020": (True, "2020-10-15"),
            "deliver on April 2020": (True, "2020-04-15"),
            "deliver on July 2020": (True, "2020-07-15"),
            "deliver in October": (True, "2020-10-15"),
            "deliver in June": (True, "2020-06-15"),
            "deliver in April": (True, "2021-04-15"),
            "deliver in 2020": (True, "2020-06-15"),
            "deliver in 2021": (True, "2021-06-15"),
            "deliver in 2019": (False, "2019-06-15"),
            "deliver on coming monday": (True, "2020-06-22"),
            "deliver on monday": (True, "2020-06-22"),
            "deliver on next tuesday": (True, "2020-06-16"),
            "deliver on previous wednesday": (True, "2020-06-10"),
            "deliver on previous thursday": (True, "2020-06-11"),
            "deliver 2 weeks later": (True, "2020-06-29"),
            "deliver 3 weeks later": (True, "2020-07-06"),
            "deliver 2 weeks ago": (True, "2020-06-01"),
            "1st next month": (True, "2020-07-01"),
            "20th last month": (True, "2020-05-20"),
        }

        for text, (use, ans) in date2normalized.items():
            for regex in self.date_entity.find_in_text(text):
                self.assertEqual(regex.use(), use, msg=text)
                self.assertEqual(regex.normalized_value(), ans, msg=text)

    @patch('slanglabs_nlu.special_entities.date_entity.today', side_effect=today)  # noqa
    def test_relative_date_forward(self, mock_datetime_now):
        current_day = today()
        date2normalized = {
            "tomorrow": "00:00:01",
            "day after tomorrow": "00:00:02",
            "next month": "00:01:00",
            "next year": "01:00:00",
            "2 days later": "00:00:02",
            "3 months later": "00:03:00",
            "4 years later": "04:00:00",
            "3 days from today": "00:00:03",
            "3 month 2 days from today": "00:03:02",
            "deliver day after tomorrow to my house": "00:00:02",
            "today": "00:00:00",
            "next year": "01:00:00",
            "next month": "00:01:00",
        }
        for text, ans in date2normalized.items():
            for regex in self.date_entity.find_in_text(text):
                years_delta, months_delta, days_delta = [int(i) for i in ans.split(':')]  # noqa
                datedelta = relativedelta(
                    years=years_delta,
                    months=months_delta,
                    days=days_delta,
                )
                expected_date = current_day + datedelta
                formated_expected_date = expected_date.strftime("%Y-%m-%d")
                self.assertEqual(regex.use(), True, msg=text)
                self.assertEqual(regex.normalized_value(), formated_expected_date, msg=text)  # noqa

    @patch('slanglabs_nlu.special_entities.date_entity.today', side_effect=today)  # noqa
    def test_relative_date_backward(self, mock_datetime_now):
        current_day = today()
        date2normalized = {
            "yesterday": "00:00:01",
            "day before yesterday": "00:00:02",
            "last month": "00:01:00",
            "last year": "01:00:00",
            "2 days ago": "00:00:02",
            "3 months before": "00:03:00",
            "4 years previous": "04:00:00",
            "3 days before today": "00:00:03",
            "flew my plane day before yesterday": "00:00:02",
            "last year": "01:00:00",
            "last month": "00:01:00",
        }
        for text, ans in date2normalized.items():
            for regex in self.date_entity.find_in_text(text):
                years_delta, months_delta, days_delta = [int(i) for i in ans.split(':')]  # noqa
                datedelta = relativedelta(
                    years=years_delta,
                    months=months_delta,
                    days=days_delta,
                )
                expected_date = current_day - datedelta
                formated_expected_date = expected_date.strftime("%Y-%m-%d")
                self.assertEqual(regex.use(), True, msg=text)
                self.assertEqual(regex.normalized_value(), formated_expected_date, msg=text)  # noqa


class PastDateEntityTest(unittest.TestCase):
    def setUp(self):
        self.date_entity = DateEntityPast()

    @patch('slanglabs_nlu.special_entities.date_entity.today', side_effect=today)  # noqa
    def test_date(self, mock_datetime_now):
        date2normalized = {
            "on christmas": (True, "2019-12-25"),
            "on new year's": (True, "2020-01-01"),
            "on new year's eve": (True, "2019-12-31"),
            "on thanksgiving": (True, "2019-11-28"),
            "on republic day": (True, "2020-01-26"),
            "on independence day": (True, "2019-08-15"),
            "on gandhi jayanti": (True, "2019-10-02"),
            "on may day": (True, "2020-05-01"),
            "on diwali": (True, "2019-10-27"),
            "on deepavali": (True, "2019-10-27"),
            "on deepawali": (True, "2019-10-27"),
            "on ganesh chaturti": (True, "2019-09-02"),
            "on ganesh pooja": (True, "2019-09-02"),
            "on ganesha pooja": (True, "2019-09-02"),
            "on krishna jayanti": (True, "2019-08-24"),
            "on krishna janmashatami": (True, "2019-08-24"),
            "on krishna pooja": (True, "2019-08-24"),
            "on easter": (True, "2020-04-12"),
            "on good friday": (True, "2020-04-10"),
            "on eid": (True, "2020-05-23"),
            "on muharam": (True, "2019-08-31"),
            "on milad un nabi": (True, "2019-11-08"),
            "on memorial day": (True, "2020-05-30"),
            "on labor day": (True, "2019-09-02"),
            "on veteran's day": (True, "2019-11-11"),
            "April 4th": (True, "2020-04-04"),
            "5th June 2009": (True, "2009-06-05"),
            "October 6th 2021": (False, "2021-10-06"),
            "2021": (False, "2021-06-15"),
            "February 2022": (False, "2022-02-15"),
            "22nd of Jan": (True, "2020-01-22"),
            "june 7": (True, "2020-06-07"),
            "8 Sep": (True, "2019-09-08"),
            "20th": (True, "2020-05-20"),
            "8th": (True, "2020-06-08"),
            "july 19 2019": (True, "2019-07-19"),
            "logged on june 20th": (True, "2019-06-20"),
            "logged on 10th december": (True, "2019-12-10"),
            "logged on 12th": (True, "2020-06-12"),
            "logged on 14th april": (True, "2020-04-14"),
            "now": (True, "2020-06-15"),
            "today": (True, "2020-06-15"),
        }

        for text, (use, ans) in date2normalized.items():
            for regex in self.date_entity.find_in_text(text):
                self.assertEqual(regex.use(), use, msg=text)
                self.assertEqual(regex.normalized_value(), ans, msg=text)

    @patch('slanglabs_nlu.special_entities.date_entity.today', side_effect=today)  # noqa
    def test_relative_date_forward(self, mock_datetime_now):
        current_day = today()
        date2normalized = {
            "tomorrow": "00:00:01",
            "day after tomorrow": "00:00:02",
            "next month": "00:01:00",
            "next year": "01:00:00",
            "2 days later": "00:00:02",
            "3 months later": "00:03:00",
            "4 years later": "04:00:00",
            "3 days from today": "00:00:03",
            "3 month 2 days from today": "00:03:02",
            "deliver day after tomorrow to my house": "00:00:02",
            "next year": "01:00:00",
            "next month": "00:01:00",
        }
        for text, ans in date2normalized.items():
            for regex in self.date_entity.find_in_text(text):
                years_delta, months_delta, days_delta = [int(i) for i in ans.split(':')]  # noqa
                datedelta = relativedelta(
                    years=years_delta,
                    months=months_delta,
                    days=days_delta,
                )
                expected_date = current_day + datedelta
                formated_expected_date = expected_date.strftime("%Y-%m-%d")
                self.assertEqual(regex.use(), False, msg=text)
                self.assertEqual(regex.normalized_value(), formated_expected_date, msg=text)  # noqa

    @patch('slanglabs_nlu.special_entities.date_entity.today', side_effect=today)  # noqa
    def test_relative_date_backward(self, mock_datetime_now):
        current_day = today()
        date2normalized = {
            "yesterday": "00:00:01",
            "day before yesterday": "00:00:02",
            "last month": "00:01:00",
            "last year": "01:00:00",
            "2 days ago": "00:00:02",
            "3 months before": "00:03:00",
            "4 years previous": "04:00:00",
            "3 days before today": "00:00:03",
            "today": "00:00:00",
            "flew my plane day before yesterday": "00:00:02",
            "last year": "01:00:00",
            "last month": "00:01:00",
        }
        for text, ans in date2normalized.items():
            for regex in self.date_entity.find_in_text(text):
                years_delta, months_delta, days_delta = [int(i) for i in ans.split(':')]  # noqa
                datedelta = relativedelta(
                    years=years_delta,
                    months=months_delta,
                    days=days_delta,
                )
                expected_date = current_day - datedelta
                formated_expected_date = expected_date.strftime("%Y-%m-%d")
                self.assertEqual(regex.use(), True, msg=text)
                self.assertEqual(regex.normalized_value(), formated_expected_date, msg=text)  # noqa


if __name__ == '__main__':
    unittest.main()
