from slanglabs_nlu.special_entities.number_entity import (
    NumberEntity, number_regex_list, float_regex, int_regex
)

currency_units_mapping = {
    'rupees': 'INR',
    'rupee': 'INR',
    '₹': 'INR',
    're': 'INR',
    'rs': 'INR',
    r'rs\.': 'INR',
    r're\.': 'INR',
    'rs.': 'INR',
    're.': 'INR',
    'dollars': 'USD',
    'dollar': 'USD',
    r'\$': 'USD',
    r'$': 'USD',
}

currency_sd_units_mapping = {
    'cents': ('USD', 0.01),
    'cent': ('USD', 0.01),
    'paisa': ('INR', 0.01),
    'paise': ('INR', 0.01),
    'p': ('INR', 0.01),
}

currency_units_regex = '|'.join(currency_units_mapping.keys())
currency_units_group_regex = r'(?P<currency_unit>{})'.format(currency_units_regex)  # noqa

currency_sd_units_regex = '|'.join(currency_sd_units_mapping.keys())
currency_sd_units_group_regex = r'(?P<currency_sd_unit>{})'.format(currency_sd_units_regex)  # noqa
number_group_regex = r'(?P<currency_sd_value>({}|{}))'.format(float_regex, int_regex)  # noqa
currency_sd_group_regex = r'\s?'.join([number_group_regex, currency_sd_units_group_regex])  # noqa
money_regex_list = []
money_regex_list += [i + [currency_units_group_regex] + [currency_sd_group_regex] for i in number_regex_list]  # noqa
money_regex_list += [[currency_units_group_regex] + i + [currency_sd_group_regex] for i in number_regex_list]  # noqa
money_regex_list += [[currency_units_group_regex] + i for i in number_regex_list]  # noqa
money_regex_list += [i + [currency_units_group_regex] for i in number_regex_list]  # noqa
money_regex_list += [[currency_sd_group_regex] for i in number_regex_list]
money_regexes = [r'\s?'.join(i) for i in money_regex_list]


class MoneyCompositeEntity(NumberEntity):
    def __init__(self):
        super().__init__()
        self._regexes = money_regexes

    def name(self):
        return 'std.money'

    def entity2entitytypes(self):
        return {
            'std_money_amount': 'std.float',
            'std_money_unit': 'std.currency'
        }

    def normalize(self, found_pattern):
        use, currency_value = super().normalize(found_pattern)
        group_dict = found_pattern.groupdict()
        currency_unit = group_dict.get('currency_unit')
        currency_unit = currency_units_mapping.get(currency_unit)
        currency_sd_unit = group_dict.get('currency_sd_unit')
        corresponding_currency, multiplier = currency_sd_units_mapping.get(currency_sd_unit, (None, 0))  # noqa
        if currency_unit is not None and currency_unit == corresponding_currency:  # noqa
            currency_sd_value = float(group_dict.get('currency_sd_value', 0)) * multiplier  # noqa
            currency_value += currency_sd_value
        if currency_unit is None and corresponding_currency is not None:
            currency_unit = corresponding_currency
            currency_sd_value = float(group_dict.get('currency_sd_value', 0)) * multiplier  # noqa
            currency_value = currency_sd_value
        if currency_unit is not None:
            return True, {'std_money_amount': currency_value, 'std_money_unit': currency_unit}  # noqa
        return False, None


def currency_units_set():
    return set(currency_units_mapping.keys()) | set(currency_sd_units_mapping.keys())  # noqa
