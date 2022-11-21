
# Constants used in vedvyasa.special_entities.date_entity

months_dict = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12,
    "Jan": 1,
    "Feb": 2,
    "Mar": 3,
    "Apr": 4,
    "May": 5,
    "Jun": 6,
    "Jul": 7,
    "Aug": 8,
    "Sep": 9,
    "Sept": 9,
    "Oct": 10,
    "Nov": 11,
    "Dec": 12,
}
relative_day = {
    "yesterday": -1,
    "tomorrow": +1,
    "now": 0,
    "today": 0,
    "tonight": 0,
    "day before yesterday": -2,
    "day after tomorrow": +2,
    "the day after tomorrow": +2,
    "the day before yesterday": -2,
}

relative_week = {
    "next week": 1,
    "last week": -1,
    "upcoming week": 1,
    "next to next week": 2,
    "previous week": -1,
    "the next week": 1,
    "the last week": -1,
    "the coming week": 1,
    "the upcoming week": 1,
    "the previous week": -1,
}

relative_month = {
    "next month": 1,
    "last month": -1,
    "coming month": 1,
    "next to next month": 2,
    "previous month": -1,
    "the next month": 1,
    "the last month": -1,
    "the coming month": 1,
    "the previous month": -1,
    "of next month": 1,
    "of last month": -1,
    "of coming month": 1,
    "of next to next month": 2,
    "of previous month": -1,
}

relative_year = {
    "next year": 1,
    "last year": -1,
    "coming year": 1,
    "next to next year": 2,
    "previous year": -1,
    "the next year": 1,
    "the last year": -1,
    "the coming year": 1,
    "the previous year": -1,
}

dow_dict = {
    "Monday": 0,
    "Tuesday": 1,
    "Wednesday": 2,
    "Thursday": 3,
    "Friday": 4,
    "Saturday": 5,
    "Sunday": 6,
}

special_dates_dict = {
    "thanksgiving": [
        "2019-11-28",
        "2020-11-26",
        "2021-11-25",
        "2022-11-24",
    ],
    "christmas": [
        "2019-12-25",
        "2020-12-25",
        "2021-12-25",
        "2022-12-25",
    ],
    "new year's eve": [
        "2019-12-31",
        "2020-12-31",
        "2021-12-31",
        "2022-12-31",
    ],
    "new year's": [
        "2020-01-01",
        "2021-01-01",
        "2022-01-01",
        "2023-01-01",
    ],
    "republic day": [
        "2020-01-26",
        "2021-01-26",
        "2022-01-26",
        "2023-01-26",
    ],
    "independence day": [
        "2019-08-15",
        "2020-08-15",
        "2021-08-15",
        "2022-08-15",
        "2023-08-15",
    ],
    "gandhi jayanti": [
        "2019-10-02",
        "2020-10-02",
        "2021-10-02",
        "2022-10-02",
        "2023-10-02"
    ],
    "may day": [
        "2019-05-01",
        "2020-05-01",
        "2021-05-01",
        "2022-05-01",
        "2023-05-01",
    ],
    "diwali": [
        "2019-10-27",
        "2020-11-14",
        "2021-11-04",
        "2022-10-24",
    ],
    "deepavali": [
        "2019-10-27",
        "2020-11-14",
        "2021-11-04",
        "2022-10-24",
    ],
    "deepawali": [
        "2019-10-27",
        "2020-11-14",
        "2021-11-04",
        "2022-10-24",
    ],
    "ganesh chaturti": [
        "2019-09-02",
        "2020-08-22",
        "2021-09-10",
        "2022-08-30",
    ],
    "ganesh pooja": [
        "2019-09-02",
        "2020-08-22",
        "2021-09-10",
        "2022-08-30",
    ],
    "ganesha pooja": [
        "2019-09-02",
        "2020-08-22",
        "2021-09-10",
        "2022-08-30",
    ],
    "krishna jayanti": [
        "2019-08-24",
        "2020-08-11",
        "2021-08-30",
        "2022-08-18",
    ],
    "krishna janmashatami": [
        "2019-08-24",
        "2020-08-11",
        "2021-08-30",
        "2022-08-18",
    ],
    "krishna pooja": [
        "2019-08-24",
        "2020-08-11",
        "2021-08-30",
        "2022-08-18",
    ],
    "easter": [
        "2019-04-21",
        "2020-04-12",
        "2021-04-04",
        "2022-04-17",
    ],
    "good friday": [
        "2019-04-19",
        "2020-04-10",
        "2021-04-02",
        "2022-04-15",
    ],
    "eid": [
        "2019-06-04",
        "2020-05-23",
        "2021-07-21",
        "2022-05-02",
    ],
    "muharam": [
        "2019-08-31",
        "2020-08-20",
        "2021-08-10",
        "2022-07-30",
    ],
    "milad un nabi": [
        "2019-11-08",
        "2020-10-29",
        "2021-10-18",
        "2022-10-08",
    ],
    "memorial day": [
        "2019-05-30",
        "2020-05-30",
        "2021-05-30",
        "2022-05-30",
    ],
    "labor day": [
        "2019-09-02",
        "2020-09-07",
        "2021-09-06",
        "2022-09-05",
    ],
    "veteran's day": [
        "2019-11-11",
        "2020-11-11",
        "2021-11-11",
        "2022-11-11",
    ]
}

date_preps = [
    "on", "in"
]
