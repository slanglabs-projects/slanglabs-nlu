import argparse
import calendar
import numpy as np

from slanglabs_nlu.entity_extraction.parsers import parse_dates
from datetime import datetime, timedelta
from time import perf_counter_ns
from dateutil.relativedelta import relativedelta

tmp = datetime.now()
NOW = datetime(
    year=tmp.year,
    month=tmp.month,
    day=tmp.day,
    hour=0,
    minute=0,
    second=0,
    microsecond=0
)
TODAY_3PM = datetime(
    year=NOW.year,
    month=NOW.month,
    day=NOW.day,
    hour=15,
    minute=0,
    second=0
)


def fmt(items):
    ret = []
    lst = items if isinstance(items, list) else [items]
    for item in lst:
        ret.append((str(item[0]), item[1]))
    return ret


test_cases = {
    'tomorrow': fmt((
        NOW + timedelta(days=1),
        (0, 7)
    )),
    'next january': fmt((
        datetime(day=1, month=1, year=NOW.year+1),
        (0, 11)
    )),
    '30th of next march': fmt((
        datetime(
            day=30,
            month=3,
            year=NOW.year if NOW.month < 3 else NOW.year+1
        ), (0, 17)
    )),
    'next december first': fmt((
        datetime(
            day=1,
            month=12,
            year=NOW.year if NOW.month < 12 else NOW.year+1
        ), (0, 18)
    )),
    'next wednesday at 3 pm': fmt((
        TODAY_3PM + relativedelta(
            weekday=calendar.WEDNESDAY,
            weeks=+1
        ), (0, 21)
    )),
    'twenty first of next month': fmt((
        NOW + relativedelta(day=21, months=+1),
        (0, 25)
    )),
    'tuesday of next week': fmt((
        NOW + relativedelta(
            weekday=calendar.TUESDAY,
            weeks=+1 if NOW.weekday() <= 1 else 0,
        ), (0, 19)
    )),
    'next sunday': fmt((
        NOW + relativedelta(weekday=calendar.SUNDAY, weeks=+1),
        (0, 10)
    )),
    'last sunday': fmt((
        NOW - relativedelta(weekday=calendar.SUNDAY, weeks=+1),
        (0, 10)
    )),
    '21st june 2021': fmt((
        datetime(year=2021, month=6, day=21),
        (0, 13)
    )),
    '2023 august 15th 4 am': fmt((
        datetime(year=2023, month=8, day=15, hour=4),
        (0, 20)
    )),
    'tuesday of last week at 2:53 pm': fmt((
        TODAY_3PM + relativedelta(
            weekday=calendar.TUESDAY,
            weeks=-2 if NOW.weekday() > 1 else -1,
            minutes=-7
        ), (0, 30)
    )),
    'tuesday next week': fmt((
        NOW + relativedelta(
            weekday=calendar.TUESDAY,
            weeks=+1 if NOW.weekday() <= 1 else 0,
        ), (0, 16)
    )),
    '20th of next month': fmt((
        NOW + relativedelta(day=20, months=+1),
        (0, 17)
    )),
    '1092022': fmt((
        datetime(year=2022, month=9, day=10),
        (0, 6)
    )),
    '10122022': fmt((
        datetime(year=2022, month=12, day=10),
        (0, 7)
    )),
    'a week from now': fmt((
        NOW + relativedelta(weeks=+1),
        (2, 14)
    )),
    'in a week': fmt((
        NOW + relativedelta(weeks=+1),
        (5, 8)
    )),
    'next week': fmt((
        NOW + relativedelta(weeks=+1),
        (0, 8)
    )),
    'last week': fmt((
        NOW + relativedelta(weeks=-1),
        (0, 8)
    )),
    '2 weeks later': fmt((
        NOW + relativedelta(weeks=+2),
        (0, 12)
    )),
    '5 days from now': fmt((
        NOW + relativedelta(days=+5),
        (0, 14)
    )),
    'in 5 days': fmt((
        NOW + relativedelta(days=+5),
        (3, 8)
    )),
    'in 5 months': fmt((
        NOW + relativedelta(months=+5),
        (3, 10)
    )),
    '5 days ago': fmt((
        NOW + relativedelta(days=-5),
        (0, 9)
    )),
    'day after': fmt((
        NOW + relativedelta(days=+2),
        (0, 8)
    )),
    '5 days back': fmt((
        NOW + relativedelta(days=-5),
        (0, 10)
    )),
    'this weekend': fmt((
        NOW + relativedelta(weekday=calendar.SATURDAY),
        (0, 11)
    )),
    'on ninth': fmt((
        NOW + relativedelta(day=9, months=+1 if NOW.day > 9 else 0),
        (3, 7)
    )),
    'on 25th': fmt((
        NOW + relativedelta(day=25, months=+1 if NOW.day > 25 else 0),
        (3, 6)
    )),
    '20 July': fmt((
        datetime(
            month=7,
            day=20,
            year=NOW.year+1
            if NOW.month > 7 or NOW.month == 7 and NOW.day > 20 else NOW.year
        ), (0, 6)
    )),
    'October 20': fmt((
        datetime(
            month=10,
            day=20,
            year=NOW.year+1
            if NOW.month > 10 or NOW.month == 10 and NOW.day > 20
            else NOW.year
        ), (0, 9)
    )),
    'previous wednesday': fmt((
        NOW + relativedelta(
            weekday=calendar.WEDNESDAY,
            weeks=-1 if NOW.weekday() < 3 else -1,
        ), (0, 17)
    )),
    '3rd next month': fmt((
        NOW + relativedelta(
            months=+1,
            day=3,
        ), (0, 13)
    )),
    '3 weeks ago': fmt((
        NOW + relativedelta(weeks=-3),
        (0, 10)
    )),
    '4 months later': fmt((
        NOW + relativedelta(months=4),
        (0, 13)
    )),
    'in 4 months': fmt((
        NOW + relativedelta(months=4),
        (3, 10)
    )),
    '3 months before': fmt((
        NOW + relativedelta(months=-3),
        (0, 14)
    )),
    'no date in here': '',
    'this utterance is empty': '',
    'Kasoda to pune tonight': fmt((
        NOW,
        (15, 21)
    )),
    'parbhani to Amravati now 9:00 to 10:00': fmt((
        NOW,
        (21, 37)
    )),
    'dhule to pune on 7 August': fmt((
        datetime(
            month=8,
            day=7,
            year=NOW.year
            if NOW.month < 8 or NOW.month == 8 and NOW.day < 7
            else NOW.year + 1
        ), (17, 24)
    )),
    'Is there any bus from Kolhapur to ahmedabad now?': fmt((
        NOW,
        (44, 46)
    )),
    'karana to travel from kota Rajasthan to lalitpur on 4th August': fmt((
        datetime(
            month=8,
            day=4,
            year=NOW.year
            if NOW.month < 8 or NOW.month == 8 and NOW.day < 4
            else NOW.year + 1
        ), (52, 61)
    )),
    'karana to travel from devri Rajasthan to Talbehat on 31st July': fmt((
        datetime(
            month=7,
            day=31,
            year=NOW.year
            if NOW.month < 7 or NOW.month == 7 and NOW.day < 32
            else NOW.year + 1
        ), (53, 61)
    )),
    'I karana to travel from devali Rajasthan to Talbehat on July': fmt((
        datetime(
            month=7,
            day=1,
            year=NOW.year if NOW.month < 7 else NOW.year + 1
        ), (56, 59)
    )),
    'Washim Te pune city Key': '',
    'erandol': '',
    '12 August 2022': fmt((
        datetime(year=2022, month=8, day=12),
        (0, 13)
    )),
    'I am from delhi to haldwani today after 11:00 am': fmt((
        NOW + relativedelta(hour=11),
        (28, 47)
    )),
    '28th seventh month': fmt((
        datetime(
            month=7,
            day=28,
            year=NOW.year
            if NOW.month < 7 or NOW.month == 7 and NOW.day < 28
            else NOW.year+1
        ), (0, 17)
    )),
    'heroine on 30th': fmt((
        datetime(
            day=30,
            month=NOW.month
            if NOW.day < 30 and NOW.month != 2
            else NOW.month + 1,
            year=NOW.year
        ),
        (11, 14)
    )),
    'Jobt to indore 28th': fmt((
        datetime(
            day=28,
            month=NOW.month if NOW.day < 28 else NOW.month + 1,
            year=NOW.year
        ),
        (15, 18)
    )),
    'jaipur to delhi tonight': fmt((
        NOW,
        (16, 22)
    )),
    'From Latur to palampur on 6th': fmt((
       datetime(
           year=NOW.year,
           month=NOW.month if NOW.day < 6 else NOW.month + 1,
           day=6,
       ), (26, 28)
    )),
    'after 2 days': fmt((
        NOW + relativedelta(days=2),
        (6, 11)
    )),
    'lucknow to kota on 11th August': fmt((
        datetime(
            day=11,
            month=8,
            year=NOW.year
            if NOW.month < 8 or NOW.month == 8 and NOW.day < 11
            else NOW.year + 1
        ),
        (19, 29)
    )),
    'October kota to Orai': fmt((
        datetime(
            day=1,
            month=10,
            year=NOW.year if NOW.month <= 10 else NOW.year + 1,
        ),
        (0, 6)
    )),
    'indore to jalgaon on 28th': fmt((
        datetime(
            day=28,
            month=NOW.month if NOW.day < 28 else NOW.month + 1,
            year=NOW.year,
        ),
        (21, 24)
    )),
    'pune To indore Shyam Ke Boss 5 Date': fmt((
        datetime(
            day=5,
            month=NOW.month if NOW.day < 5 else NOW.month + 1,
            year=NOW.year,
        ),
        (29, 29)
    )),
    'delhi to haridwar on 30th July': fmt((
        datetime(
            day=30,
            month=7,
            year=NOW.year
            if NOW.month < 7 or NOW.month == 7 and NOW.day < 30
            else NOW.year+1
        ),
        (21, 29)
    )),
    'Parel mumbai': '',
    'Balaghat to raipur on 29th July': fmt((
        datetime(
            day=29,
            month=7,
            year=NOW.year
            if NOW.month < 7 or NOW.month == 7 and NOW.day < 30
            else NOW.year+1
        ),
        (22, 30)
    )),
    'Tambaram chennai': '',
    'ahmedabad at 10:00': fmt((
        NOW + relativedelta(hours=10),
        (13, 17)
    )),
    'Sarangpur to Mehsana July': fmt((
        datetime(
            day=1,
            month=7,
            year=NOW.year if NOW.month < 7 else NOW.year+1
        ), (21, 24)
    )),
    'Train options of 29 July to go to pandharpur': fmt((
        datetime(
            day=29,
            month=7,
            year=NOW.year
            if NOW.month < 7 or NOW.month == 7 and NOW.day < 29
            else NOW.year+1
        ), (17, 23)
    )),
    'lucknow to merath 297 2022': fmt((
        datetime(
            year=NOW.year,
            month=1,
            day=1,
        ), (18, 25)
    )),
    'pune to Nanded 1st 130': fmt((
        datetime(
            year=NOW.year,
            month=NOW.month if NOW.day == 1 else NOW.month + 1,
            day=1,
        ), (15, 17)
    )),
    '129 August': fmt((
        datetime(
            day=1,
            month=8,
            year=NOW.year if NOW.month < 8 else NOW.year + 1
        ), (0, 9)
    )),
    'Nanded to pune 31st': fmt((
        datetime(
            day=31,
            month=NOW.month
            if NOW.day < 31 and calendar.monthrange(NOW.year, NOW.month)[1]
            == 31 else NOW.month+1,
            year=NOW.year,
        ), (15, 18)
    )),
    '2972020': fmt((
        datetime(
            day=29,
            month=7,
            year=2020,
        ), (0, 6)
    )),
    '31st at 10:00 am': fmt((
        datetime(
            day=31,
            month=NOW.month
            if NOW.day < 31 and calendar.monthrange(NOW.year, NOW.month)[1]
            == 31 else NOW.month+1,
            year=NOW.year,
        ) + relativedelta(hours=10),
        (0, 15)
    )),
    '31st at 6:00 pm': fmt((
        datetime(
            day=31,
            month=NOW.month
            if NOW.day < 31 and calendar.monthrange(NOW.year, NOW.month)[1]
            == 31 else NOW.month+1,
            year=NOW.year,
        ) + relativedelta(hours=18),
        (0, 14)
    )),
    '31st 10:00 AM 10:00 AM Bus Route to aurangabad': fmt([(
        datetime(
            day=31,
            month=NOW.month
            if NOW.day < 31 and calendar.monthrange(NOW.year, NOW.month)[1]
            == 31 else NOW.month+1,
            year=NOW.year,
        ) + relativedelta(hours=10),
        (0, 9)),
        (NOW + relativedelta(hours=10), (14, 18))
    ]),
    'delhi to lucknow is scheduled to go on 31st September': fmt((
        datetime(
            day=1,
            month=1,
            year=1970,
        ), (39, 52)
    )),
    '3172022': fmt((
        datetime(
            day=31,
            month=7,
            year=2022
        ), (0, 6)
    )),
    '2882022': fmt((
        datetime(
            day=28,
            month=8,
            year=2022,
        ), (0, 6)
    )),
    '2842022': fmt((
        datetime(
            day=28,
            month=4,
            year=2022,
        ), (0, 6)
    )),
    'saawar day': '',
    'fast house': '',
    'delhi to merath 29th 2000 2230': fmt((
        datetime(
            day=29,
            month=1,
            year=2000,
        ), (16, 24)
    )),
    'day before yesterday delhi to chennai': fmt((
        NOW + relativedelta(days=-2), (0, 19)
    )),
    'this Saturday': fmt((
        NOW + relativedelta(weekday=calendar.SATURDAY),
        (0, 12)
    )),
    'this week': fmt((
        NOW, (0, 8)
    )),
    'last day of this month': fmt((
        datetime(
            year=NOW.year,
            month=NOW.month,
            day=calendar.monthrange(NOW.year, NOW.month)[1]
        ),
        (0, 21)
    )),
    '28th of this month': fmt((
        datetime(
            year=NOW.year,
            month=NOW.month,
            day=28,
        ),
        (0, 17)
    )),
    'on 5th jan': fmt((
        datetime(
            day=5,
            month=1,
            year=NOW.year if NOW.month == 1 and NOW.day < 5 else NOW.year+1,
        ),
        (3, 9)
    )),
    'i want to travel on today\'s date': fmt((
        NOW,
        (20, 31)
    )),
    'bangalore to chennai junction tomorrow': fmt((
        NOW + timedelta(days=1),
        (30, 37)
    )),
    'bangalore junction': '',
}


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--profile', action='store_true')
    return parser.parse_args()


def run_tests(profile=False):
    iters = 1000 if profile else 1

    for input, expected in test_cases.items():
        latencies = []
        result = None
        for i in range(iters):
            start = perf_counter_ns()
            response = parse_dates(input, include_time=True)
            result = response if response else ''
            finish = perf_counter_ns()
            latencies.append(finish-start)

        print('{} | {} -> {} | {} | p99 latency: {:.1f} ms'.format(
            'passed' if str(result) == str(expected) else 'failed',
            input,
            result,
            expected,
            np.percentile(latencies, 99)/1e6
        ))


def main():
    args = parse_args()
    run_tests(args.profile)


if __name__ == '__main__':
    main()
