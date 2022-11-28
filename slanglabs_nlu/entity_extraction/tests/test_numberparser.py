import argparse
import numpy as np
import pytest

from slanglabs_nlu.entity_extraction.parsers import parse_numbers, parse_numbers_with_ranges
from time import perf_counter_ns


def fmt(items):
    ret = []
    lst = items if isinstance(items, list) else [items]
    for item in lst:
        ret.append((item[0], item[1]))
    return ret


numbers_test_cases = {
    'one crore three lakhs four hundred and forty three': fmt((10300443, (0, 49))),
    'three lakh forty five thousand': fmt((345000, (0, 29))),
    'send thousand 365': fmt((1365, (5, 16))),
    'request 1 not 5 rupees': fmt((105, (8, 14))),
    'send thousand 255': fmt((1255, (5, 16))),
    'send 5 50 rupees': fmt((550, (5, 8))),
    'send 305 to sahi': fmt((305, (5, 7))),
    'send to not 5 to jagan': fmt((205, (5, 12))),
    'request 1.5 rupees': fmt((1.5, (8, 10))),
    'send 1000 to 55': fmt((1255, (5, 14))),
    'one lakh 200': fmt((100200, (0, 11))),
    'one lakh two hundred': fmt((100200, (0, 19))),
    'one thousand 10': fmt((1010, (0, 14))),
    'three and a half kg': fmt((3.5, (0, 15))),
    'four and a half thousand': fmt((4500, (0, 23))),
    'nine thirty': fmt((930, (0, 10))),
    'there are no numbers here': [],
    'three oh five': fmt((305, (0, 12))),
    'five thousand five hundred and three': fmt((5503, (0, 35))),
    'five thousand five oh three': fmt((5503, (0, 26))),
    '1 crore 10 lakhs 5 oh 3': fmt((11000503, (0, 22))),
    '3 lakhs two hundred and fifty': fmt((300250, (0, 28))),
    'three oh five lakhs': fmt((30500000, (0, 18))),
    'three oh five lakhs three oh five thousand three oh five': fmt((30805305, (0, 55))),
    '3 oh five thousand three oh 5': fmt((305305, (0, 28))),
    'fifteen hundred': fmt((1500, (0, 14))),
    'fifty 10': fmt((5010, (0, 7))),
    '20 10': fmt((2010, (0, 4))),
    '12 75': fmt((1275, (0, 4))),
    '14 99': fmt((1499, (0, 4))),
    'four and a half thousand four and a half': fmt((4504.5, (0, 39))),
}

ranges_test_cases = {
    '2 bhk apartment 2000 square feet area in a budget range of 80 lakhs and 2 crores':
        [(2, (0, 0)), (2000, (16, 19)), (8000000, (59, 66)), (20000000, (72, 79))],
}


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--profile', action='store_true')
    return parser.parse_args()


def run_tests(profile=False):
    iters = 1000 if profile else 1

    test_cases = {
        'numbers': (numbers_test_cases, parse_numbers),
        'ranges': (ranges_test_cases, parse_numbers_with_ranges),
    }

    for _, testinfo in test_cases.items():
        test_case, fn = testinfo
        for test, expected in test_case.items():
            latencies = []
            result = None
            for i in range(iters):
                start = perf_counter_ns()
                response = fn(test)
                result = response if len(response) > 0 else ''
                finish = perf_counter_ns()
                latencies.append(finish-start)

            print('{} | {} -> {} | {} | p99 latency: {:.1f} ms'.format(
                'passed' if str(result) == str(expected) else 'failed',
                test,
                result,
                expected,
                np.percentile(latencies, 99)/1e6
            ))


@pytest.mark.parametrize(
    "inputstr, expected",
    [
        (inputstr, expected)
        for inputstr, expected in numbers_test_cases.items()
    ]
)
def test_parse_numbers(inputstr, expected):
    assert parse_numbers(inputstr) == expected


@pytest.mark.parametrize(
    "inputstr, expected",
    [
        (inputstr, expected)
        for inputstr, expected in ranges_test_cases.items()
    ]
)
def test_parse_numbers_with_ranges(inputstr, expected):
    assert parse_numbers_with_ranges(inputstr) == expected


def main():
    args = parse_args()
    run_tests(args.profile)


if __name__ == '__main__':
    main()
