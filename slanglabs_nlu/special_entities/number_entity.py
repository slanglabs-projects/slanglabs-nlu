from slanglabs_nlu.special_entities.abstract_special_entities import AbstractSpecialEntities  # noqa


# To Implement:
# Half million

float_regex = r"(?P<float>[0-9]+\.[0-9]+)"
int_regex = r"(?P<int>[0-9]+)"
number_hundreds_regex = r'[0-9]{1,3}(\.[0-9]+)?'
number_name_units_mapping = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

number_name_teens_mapping = {
    "ten": 10,
    "eleven": 11,
    "twelve": 12,
    "thirteen": 13,
    "fourteen": 14,
    "fifteen": 15,
    "sixteen": 16,
    "seventeen": 17,
    "eighteen": 18,
    "nineteen": 19,
}

number_name_tens_mapping = {
    "twenty": 20,
    "thirty": 30,
    "forty": 40,
    "fifty": 50,
    "sixty": 60,
    "seventy": 70,
    "eighty": 80,
    "ninety": 90,
}
special_numbers = {
    'half': 0.5,
    'quarter': 0.25,
    'three quarters': 0.75,
    'three quarter': 0.75,
    'dozen': 12,
    'half dozen': 6,
    'hundred': 100,
    'thousand': 1000,
    'million': 10e5,
    'lakh': 10e4,
    'crore': 10e6,
}

special_suffix = {
    'half': 0.5,
    'quarter': 0.25,
    'three quarters': 0.75,
    'three quarter': 0.75,
}

thousand_int_regex = "(?P<units>thousand) " + int_regex

special_numbers_regex = '|'.join(special_numbers.keys())
special_numbers_group_regex = r'(?P<special_number>{})'.format(special_numbers_regex)  # noqa

name2number = {
    **number_name_units_mapping,
    **number_name_teens_mapping,
    **number_name_tens_mapping,
    **special_numbers,
    **special_suffix,
}

number_name_units_regex = '|'.join(number_name_units_mapping.keys())
number_name_tens_regex = '|'.join(number_name_tens_mapping.keys())
number_name_teens_regex = '|'.join(number_name_teens_mapping.keys())

special_suffix_regex = '|'.join(special_suffix.keys())

special_suffix_list = [
    "and a (?P<{special_group_name}>{special_suffix_regex})",
    "and (?P<{special_group_name}>{special_suffix_regex})",
]

special_suffix_units_format_dict = {
    'special_group_name': 'special_suffix_units_group',
    'special_suffix_regex': special_suffix_regex
}

special_suffix_units_group = '|'.join(i.format(**special_suffix_units_format_dict) for i in special_suffix_list)  # noqa
number_name_units_group_regex = r'(?P<units>{})'.format(number_name_units_regex)  # noqa
number_name_tens_group_regex = r'(?P<tens>{})'.format(number_name_tens_regex)
number_name_teens_group_regex = r'(?P<teens>{})'.format(number_name_teens_regex)  # noqa
number_name_tens_place_group_regex = '({}( {})?( {})?|{}( {})?|{}( {})?)'.format(  # noqa
    number_name_tens_group_regex, number_name_units_group_regex, special_suffix_units_group,  # noqa
    number_name_teens_group_regex, special_suffix_units_group,
    number_name_units_group_regex, special_suffix_units_group,
)

# Hundreds
number_name_hundreds_units_group_regex = r'(?P<hundred_units>{})'.format(number_name_units_regex)  # noqa
number_name_hundreds_tens_group_regex = r'(?P<hundred_tens>{})'.format(number_name_tens_regex)  # noqa
number_name_hundreds_teens_group_regex = r'(?P<hundred_teens>{})'.format(number_name_teens_regex)  # noqa
number_numeral_hundreds_group_regex = r'(?P<hundred_numeral>{})'.format(number_hundreds_regex)  # noqa
number_name_hundreds_tens_place_group_regex = '({}( {})?|{}|{}|{})'.format(
    number_name_hundreds_tens_group_regex, number_name_hundreds_units_group_regex,  # noqa
    number_name_hundreds_teens_group_regex,
    number_name_hundreds_units_group_regex,
    number_numeral_hundreds_group_regex,
)
number_name_hundred_place_group_regex =\
    r'{} hundred'.format(number_name_hundreds_tens_place_group_regex)

# Thousands
special_suffix_thousands_format_dict = {
    'special_group_name': 'special_suffix_thousands_group',
    'special_suffix_regex': special_suffix_regex
}
special_suffix_thousands_group = '|'.join(i.format(**special_suffix_thousands_format_dict) for i in special_suffix_list)  # noqa
number_name_thousands_hundreds_units_group_regex = r'(?P<thousand_hundred_units>{})'.format(number_name_units_regex)  # noqa
number_name_thousands_hundreds_tens_group_regex = r'(?P<thousand_hundred_tens>{})'.format(number_name_tens_regex)  # noqa
number_name_thousands_hundreds_teens_group_regex = r'(?P<thousand_hundred_teens>{})'.format(number_name_teens_regex)  # noqa
number_name_thousands_hundreds_tens_place_group_regex =\
    '({}( {})?|{}|{})'.format(
        number_name_thousands_hundreds_tens_group_regex,
        number_name_thousands_hundreds_units_group_regex,
        number_name_thousands_hundreds_teens_group_regex,
        number_name_thousands_hundreds_units_group_regex,
    )
number_name_thousands_hundreds_hundreds_group_regex = r'(?P<thousand_hundred_hundreds>{})'.format(number_name_units_regex)  # noqa
number_numeral_thousands_hundreds_group_regex = r'(?P<thousand_hundred_numeral>{})'.format(number_hundreds_regex)  # noqa
number_name_thousands_group_regex =\
    r'(({} hundred)( and {})?|{}( {})?|{}( {})?)'.format(
        number_name_thousands_hundreds_hundreds_group_regex, number_name_thousands_hundreds_tens_place_group_regex,  # noqa
        number_name_thousands_hundreds_tens_place_group_regex, special_suffix_thousands_group,  # noqa
        number_numeral_thousands_hundreds_group_regex, special_suffix_thousands_group,  # noqa
    )

number_name_thousand_place_group_regex =\
    r'{}( ?[k](?=\s|$)| thousand)'.format(number_name_thousands_group_regex)

# Millions
special_suffix_millions_format_dict = {
    'special_group_name': 'special_suffix_millions_group',
    'special_suffix_regex': special_suffix_regex
}
special_suffix_millions_group = '|'.join(i.format(**special_suffix_millions_format_dict) for i in special_suffix_list)  # noqa
number_name_millions_hundreds_units_group_regex = r'(?P<million_hundred_units>{})'.format(number_name_units_regex)  # noqa
number_name_millions_hundreds_tens_group_regex = r'(?P<million_hundred_tens>{})'.format(number_name_tens_regex)  # noqa
number_name_millions_hundreds_teens_group_regex = r'(?P<million_hundred_teens>{})'.format(number_name_teens_regex)  # noqa
number_name_millions_hundreds_tens_place_group_regex = '({}( {})?|{}|{})'.format(  # noqa
    number_name_millions_hundreds_tens_group_regex,
    number_name_millions_hundreds_units_group_regex,
    number_name_millions_hundreds_teens_group_regex,
    number_name_millions_hundreds_units_group_regex
)
number_name_millions_hundreds_hundreds_group_regex = r'(?P<million_hundred_hundreds>{})'.format(number_name_units_regex)  # noqa
number_numeral_millions_hundreds_group_regex = r'(?P<million_hundred_numeral>{})'.format(number_hundreds_regex)  # noqa
number_name_millions_group_regex =\
    r'(({} hundred)( and {})?|{}( {})?|{}( {})?)'.format(
        number_name_millions_hundreds_hundreds_group_regex, number_name_millions_hundreds_tens_place_group_regex,  # noqa
        number_name_millions_hundreds_tens_place_group_regex, special_suffix_millions_group,  # noqa
        number_numeral_millions_hundreds_group_regex, special_suffix_millions_group,  # noqa
    )

number_name_million_place_group_regex =\
    r'{} million'.format(number_name_millions_group_regex)


# Lakhs
special_suffix_lakhs_format_dict = {
    'special_group_name': 'special_suffix_lakhs_group',
    'special_suffix_regex': special_suffix_regex
}
special_suffix_lakhs_group = '|'.join(i.format(**special_suffix_lakhs_format_dict) for i in special_suffix_list)  # noqa
number_name_lakhs_hundreds_units_group_regex = r'(?P<lakh_hundred_units>{})'.format(number_name_units_regex)  # noqa
number_name_lakhs_hundreds_tens_group_regex = r'(?P<lakh_hundred_tens>{})'.format(number_name_tens_regex)  # noqa
number_name_lakhs_hundreds_teens_group_regex = r'(?P<lakh_hundred_teens>{})'.format(number_name_teens_regex)  # noqa
number_name_lakhs_hundreds_tens_place_group_regex = '({}( {})?|{}|{})'.format(
    number_name_lakhs_hundreds_tens_group_regex,
    number_name_lakhs_hundreds_units_group_regex,
    number_name_lakhs_hundreds_teens_group_regex,
    number_name_lakhs_hundreds_units_group_regex
)

number_name_lakhs_hundreds_hundreds_group_regex = r'(?P<lakh_hundred_hundreds>{})'.format(number_name_units_regex)  # noqa
number_numeral_lakhs_hundreds_group_regex = r'(?P<lakh_hundred_numeral>{})'.format(number_hundreds_regex)  # noqa
number_name_lakhs_group_regex =\
    r'(({} hundred)( and {})?|{}( {})?|{}( {})?)'.format(
        number_name_lakhs_hundreds_hundreds_group_regex, number_name_lakhs_hundreds_tens_place_group_regex,  # noqa
        number_name_lakhs_hundreds_tens_place_group_regex, special_suffix_lakhs_group,  # noqa
        number_numeral_lakhs_hundreds_group_regex, special_suffix_lakhs_group
    )

number_name_lakh_place_group_regex =\
    r'{} (lakhs?|lacs?)'.format(number_name_lakhs_group_regex)

# Crores
special_suffix_crores_format_dict = {
    'special_group_name': 'special_suffix_crores_group',
    'special_suffix_regex': special_suffix_regex
}
special_suffix_crores_group = '|'.join(i.format(**special_suffix_crores_format_dict) for i in special_suffix_list)  # noqa
number_name_crores_hundreds_units_group_regex = r'(?P<crore_hundred_units>{})'.format(number_name_units_regex)  # noqa
number_name_crores_hundreds_tens_group_regex = r'(?P<crore_hundred_tens>{})'.format(number_name_tens_regex)  # noqa
number_name_crores_hundreds_teens_group_regex = r'(?P<crore_hundred_teens>{})'.format(number_name_teens_regex)  # noqa
number_name_crores_hundreds_tens_place_group_regex = '({}( {})?|{}|{})'.format(
    number_name_crores_hundreds_tens_group_regex,
    number_name_crores_hundreds_units_group_regex,
    number_name_crores_hundreds_teens_group_regex,
    number_name_crores_hundreds_units_group_regex
)

number_name_crores_hundreds_hundreds_group_regex = r'(?P<crore_hundred_hundreds>{})'.format(number_name_units_regex)  # noqa
number_numeral_crores_hundreds_group_regex = r'(?P<crore_hundred_numeral>{})'.format(number_hundreds_regex)  # noqa
number_name_crores_group_regex =\
    r'(({} hundred)( and {})?|{}( {})?|{}( {})?)'.format(
        number_name_crores_hundreds_hundreds_group_regex, number_name_crores_hundreds_tens_place_group_regex,  # noqa
        number_name_crores_hundreds_tens_place_group_regex, special_suffix_lakhs_group,  # noqa
        number_numeral_crores_hundreds_group_regex, special_suffix_crores_group
    )

number_name_crore_place_group_regex =\
    r'{}( crores?| ?crs?)'.format(number_name_crores_group_regex)

and_regex = r'(and)?'
number_regex_list = [
        [
            number_name_million_place_group_regex,
            number_name_thousand_place_group_regex,
            number_name_hundred_place_group_regex,
            and_regex,
            number_name_tens_place_group_regex,
        ],
        [
            number_name_million_place_group_regex,
            number_name_thousand_place_group_regex,
            number_name_hundred_place_group_regex,
        ],
        [
            number_name_million_place_group_regex,
            number_name_thousand_place_group_regex,
        ],
        [
            number_name_million_place_group_regex,
            number_name_thousand_place_group_regex,
            and_regex,
            number_name_tens_place_group_regex,
        ],
        [
            number_name_million_place_group_regex,
            number_name_hundred_place_group_regex,
            and_regex,
            number_name_tens_place_group_regex,
        ],
        [
            number_name_million_place_group_regex,
            and_regex,
            number_name_tens_place_group_regex,
        ],
        [
            number_name_crore_place_group_regex,
            number_name_lakh_place_group_regex,
            number_name_thousand_place_group_regex,
            number_name_hundred_place_group_regex,
            and_regex,
            number_name_tens_place_group_regex,
        ],
        [
            number_name_crore_place_group_regex,
            number_name_lakh_place_group_regex,
            number_name_thousand_place_group_regex,
            number_name_hundred_place_group_regex
        ],
        [
            number_name_crore_place_group_regex,
            number_name_lakh_place_group_regex,
            number_name_thousand_place_group_regex,
            and_regex,
            number_name_tens_place_group_regex,
        ],
        [
            number_name_crore_place_group_regex,
            number_name_thousand_place_group_regex,
            number_name_hundred_place_group_regex,
            and_regex,
            number_name_tens_place_group_regex,
        ],
        [
            number_name_crore_place_group_regex,
            number_name_lakh_place_group_regex,
            number_name_thousand_place_group_regex,
        ],
        [
            number_name_crore_place_group_regex,
            number_name_lakh_place_group_regex,
            number_name_hundred_place_group_regex,
        ],
        [
            number_name_crore_place_group_regex,
            number_name_thousand_place_group_regex,
            number_name_hundred_place_group_regex,
        ],
        [
            number_name_crore_place_group_regex,
            number_name_lakh_place_group_regex,
            and_regex,
            number_name_tens_place_group_regex,
        ],
        [
            number_name_crore_place_group_regex,
            number_name_thousand_place_group_regex,
            and_regex,
            number_name_tens_place_group_regex,
        ],
        [
            number_name_crore_place_group_regex,
            number_name_hundred_place_group_regex,
            and_regex,
            number_name_tens_place_group_regex,
        ],
        [
            number_name_crore_place_group_regex,
            number_name_lakh_place_group_regex,
        ],
        [
            number_name_crore_place_group_regex,
            number_name_thousand_place_group_regex,
        ],
        [
            number_name_crore_place_group_regex,
            number_name_hundred_place_group_regex,
        ],
        [
            number_name_crore_place_group_regex,
            and_regex,
            number_name_tens_place_group_regex,
        ],
        [
            number_name_lakh_place_group_regex,
            int_regex,
        ],
        [
            number_name_lakh_place_group_regex,
            number_name_thousand_place_group_regex,
            number_name_hundred_place_group_regex,
            and_regex,
            number_name_tens_place_group_regex,
        ],
        [
            number_name_lakh_place_group_regex,
            number_name_thousand_place_group_regex,
            number_name_hundred_place_group_regex,
        ],
        [
            number_name_lakh_place_group_regex,
            number_name_thousand_place_group_regex,
        ],
        [
            number_name_lakh_place_group_regex,
            number_name_thousand_place_group_regex,
            and_regex,
            number_name_tens_place_group_regex,
        ],
        [
            number_name_lakh_place_group_regex,
            number_name_hundred_place_group_regex,
        ],
        [
            number_name_lakh_place_group_regex,
            number_name_hundred_place_group_regex,
            and_regex,
            number_name_tens_place_group_regex,
        ],
        [
            number_name_lakh_place_group_regex,
            and_regex,
            number_name_tens_place_group_regex,
        ],
        [
            thousand_int_regex
        ],
        [
            number_name_thousand_place_group_regex,
            number_name_hundred_place_group_regex,
            and_regex,
            number_name_tens_place_group_regex,
        ],
        [
            number_name_thousand_place_group_regex,
            number_name_hundred_place_group_regex,
        ],
        [
            number_name_thousand_place_group_regex,
            and_regex,
            number_name_tens_place_group_regex,
        ],
        [
            number_name_million_place_group_regex,
        ],
        [
            number_name_crore_place_group_regex,
        ],
        [
            number_name_lakh_place_group_regex,
        ],
        [
            number_name_thousand_place_group_regex,
        ],
        [
            number_name_hundred_place_group_regex,
            and_regex,
            number_name_tens_place_group_regex
        ],
        [
            number_name_hundred_place_group_regex
        ],
        [
            number_name_tens_place_group_regex
        ],
        [
            float_regex
        ],
        [
            int_regex
        ],
        [
            special_numbers_group_regex
        ]
    ]

number_regexes = [r'\s?'.join(i) for i in number_regex_list]

multipliers = {
    'special_number': 1.0,
    'special_suffix_units_group': 1.0,
    'int': 1.0,
    'float': 1.0,
    'units': 1.0,
    'tens': 1.0,
    'teens': 1.0,
    'hundred_units': 100.0,
    'hundred_tens': 100.0,
    'hundred_teens': 100.0,
    'hundred_numeral': 100.0,
    'thousand_hundred_units': 1000.0,
    'thousand_hundred_tens': 1000.0,
    'thousand_hundred_teens': 1000.0,
    'thousand_hundred_hundreds': 100000.0,
    'thousand_hundred_numeral': 1000.0,
    'special_suffix_thousands_group': 10**3,
    'million_hundred_numeral': 10.0**6,
    'million_hundred_units': 10.0**6,
    'million_hundred_tens': 10.0**6,
    'million_hundred_teens': 10.0**6,
    'million_hundred_hundreds': 10.0**6,
    'special_suffix_millions_group': 10**6,
    'lakh_hundred_numeral': 10.0**5,
    'lakh_hundred_units': 10.0**5,
    'lakh_hundred_tens': 10.0**5,
    'lakh_hundred_teens': 10.0**5,
    'lakh_hundred_hundreds': 10.0**5,
    'special_suffix_lakhs_group': 10**5,
    'crore_hundred_numeral': 10.0**7,
    'crore_hundred_units': 10.0**7,
    'crore_hundred_tens': 10.0**7,
    'crore_hundred_teens': 10.0**7,
    'crore_hundred_hundreds': 10.0**7,
    'special_suffix_crores_group': 10**7,
}

numeric_regex_group_names = [
    'int',
    'float',
    'lakh',
    'hundred_numeral',
    'thousand_hundred_numeral',
    'million_hundred_numeral',
    'lakh_hundred_numeral',
    'crore_hundred_numeral',
]


class NumberEntity(AbstractSpecialEntities):
    def __init__(self):
        super().__init__()
        self._regexes = number_regexes

    def name(self):
        return 'std.float'

    def _normalize_numeral(self, groupdict):
        final_value = 0
        for key, value in groupdict.items():
            if key in numeric_regex_group_names:
                multiplier = multipliers.get(key, 0)
                final_value += float(value) * multiplier
        return final_value

    def _normalize_named_number(self, groupdict):
        final_value = 0
        for key, value in groupdict.items():
            if value.isalpha():
                multiplier = multipliers.get(key, 0)
                number_value = name2number.get(value, 0)
                final_value += number_value * multiplier
        return final_value

    def normalize(self, found_pattern):
        final_value = 0.0
        groupdict = {k: v for k, v in found_pattern.groupdict().items() if v is not None}  # noqa
        if all(key not in groupdict for key in multipliers.keys()):
            return False, final_value
        final_value += self._normalize_numeral(groupdict)
        final_value += self._normalize_named_number(groupdict)
        return True, final_value


class IntegerNumberEntity(NumberEntity):
    def name(self):
        return 'std.integer'

    def normalize(self, found_pattern):
        use, final_value = super().normalize(found_pattern)
        return use, int(final_value)


def number_words_set():
    mappings = [
        number_name_units_mapping,
        number_name_teens_mapping,
        number_name_tens_mapping,
        special_numbers,
        special_suffix,
    ]
    words_set = set()
    for mapping in mappings:
        words_set |= set(mapping.keys())
    return words_set
