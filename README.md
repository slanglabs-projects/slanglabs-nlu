![lint](https://img.shields.io/github/workflow/status/slanglabs-projects/slanglabs-nlu/Python%20Lint%20and%20Test?label=lint) ![lint](https://img.shields.io/github/workflow/status/slanglabs-projects/slanglabs-nlu/Python%20Lint%20and%20Test?label=tests) 

# Slang Labs NLU

This is a Python library that provides various tools for Natural Language Understanding. These tools are primarily used by the Voice Assistants built by Slang Labs (https://slanglabs.in), but could be useful in other contexts as well.

The set of tools currently implemented as part of this library are:
## 1. Date parser for Indian English (en-IN) locale
English-speaking users in India have some characteristic ways of speaking/writing date forms that are not accurately parsed by existing parsers (which are mostly targeted towards en-US or en-UK locales). For example: _"next month 10th"_, _"3 days before"_, _"5 months back"_, etc. This parser parses most forms of commonly spoken/written date forms, including the Indian ones described above.

Usage:
```
from slanglabs_nlu.entity_extraction.parsers import parse_dates

input = 'train tickets for 12th departure and next month 10th return'
dates = parse_dates(input)
print(dates)

# [('2022-11-15', (18, 21)), ('2022-12-10', (37, 51))]
# current date, as of this writing was 2022-11-13
```

## 2. Number parser for Indian English (en-IN) locale
Similar to the date parser, the number parser aims to accurately parse utterances containing numbers spoken with characteristics unique to Indian speakers. For example, "one not two" to represent 102, "five lakh 200" to represent 500200, etc. 

In addition to parsing numbers, the parser can also parse number ranges such as "4 bedroom apartment between 2000 and 4000 sq ft".

Usage:
```
from slanglabs_nlu.entity_extraction.parsers import parse_numbers, parse_numbers_with_ranges

input = 'send to not 5 to kumar'
numbers = parse_numbers(input)
print(numbers)
# [(205, (5, 12))]

input = '2 bhk apartment 2000 square feet area in a budget range of 80 lakhs and 2 crores'
ranges = parse_numbers_with_ranges(input)
print(ranges)
# [(2, (0, 0)), (2000, (16, 19)), (8000000, (59, 66)), (20000000, (72, 79))]
```
