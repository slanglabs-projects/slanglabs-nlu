from slanglabs_nlu.special_entities.number_entity import (
    NumberEntity, number_regex_list, float_regex, int_regex
)

t_unit_mapping = {
    'tonnes': 't',
    "tonne": 't',
    'tons': 't',
    "ton": 't',
    't': 't',
}

kg_unit_mapping = {
    'kgs': 'kg',
    'kilograms': 'kg',
    'kilogram': 'kg',
    'kilo gram': 'kg',
    "kilos": "kg",
    "kilo": "kg",
    'kg': 'kg',
}

mg_unit_mapping = {
    'mgs': 'mg',
    'mg': 'mg',
    'milligrams': 'mg',
    'milligram': 'mg',
    'milli grams': 'mg',
}

g_unit_mapping = {
    'grams': 'g',
    'gram': 'g',
    'gms': 'g',
    'gm': 'g',
    'g': 'g',

}

pound_unit_mapping = {
    'pounds': 'lbs',
    'pound': 'lbs',
    'lb': 'lbs',
    'lbs': 'lbs'
}

ounces_unit_mapping = {
    'ounce': 'oz',
    'ounces': 'oz',
    'oz': 'oz',
    'ozs': 'oz'
}

weight_units_mapping = {
    **kg_unit_mapping,
    **g_unit_mapping,
    **mg_unit_mapping,
    **t_unit_mapping,
    **pound_unit_mapping,
    **ounces_unit_mapping,
}

weights_units_regex = '|'.join(weight_units_mapping.keys())
weights_units_group_regex = r'(?P<weight_unit>{})'.format(weights_units_regex)
weights_regex_list = [i + [weights_units_group_regex] for i in number_regex_list]  # noqa
weights_regex_list += [float_regex + '({})'.format(weights_units_group_regex)]
weights_regex_list += [int_regex + '({})'.format(weights_units_group_regex)]
weights_regex_list += [[weights_units_group_regex]]
weight_regexes = [r'\s?'.join(i) for i in weights_regex_list]


class WeightCompositeEntity(NumberEntity):
    def __init__(self):
        super().__init__()
        self._regexes = weight_regexes

    def name(self):
        return 'std.weight'

    def entity2entitytypes(self):
        return {
            'std_weight_value': 'std.float',
            'std_weight_unit': 'std.weight.unit'
        }

    def normalize(self, found_pattern):
        use, value = super().normalize(found_pattern)
        if use is False:
            value = 1.0
        group_dict = found_pattern.groupdict()
        weight_unit = group_dict.get('weight_unit')
        weight_unit = weight_units_mapping.get(weight_unit)
        return True, {'std_weight_value': value, 'std_weight_unit': weight_unit}  # noqa
