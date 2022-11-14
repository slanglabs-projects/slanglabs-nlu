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