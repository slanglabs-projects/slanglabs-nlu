from slanglabs_nlu.special_entities.number_entity import (
    NumberEntity, number_regex_list, float_regex
)


weight_units_mapping_kilogram = {
    'ton': 10**3,
    'tonne': 10**3,
    'tonnes': 10**3,
    'tons': 10**3,
    'kilogram': 1.0,
    'kilgrams': 1.0,
    'kgs': 1.0,
    'kg': 1.0,
    'gram': 10.0**(-3),
    'grams': 10.0**(-3),
    'gms': 10.0**(-3),
    'gm': 10.0**(-3),
    'mg': 10.0**(-6),
    'mgs': 10.0**(-6),
    'milligrams': 10.0**(-6),
    'milligram': 10.0**(-6),
}

weight_units_mapping_milligram = {
    'ton': 10.0**(9),
    'tonne': 10.0**(9),
    'tonnes': 10.0**(9),
    'tons': 10.0**(9),
    'kilogram': 10.0**(6),
    'kilgrams': 10.0**(6),
    'kgs': 10.0**(6),
    'kg': 10.0**(6),
    'gram': 10.0**(3),
    'grams': 10.0**(3),
    'gms': 10.0**(3),
    'gm': 10.0**(3),
    'mg': 1.0,
    'mgs': 1.0,
    'milligrams': 1.0,
    'milligram': 1.0,
}

weights_units_regex = '|'.join(weight_units_mapping_kilogram.keys())
weights_units_group_regex = r'(?P<weight_unit>{})'.format(weights_units_regex)
weights_regex_list = [i + [weights_units_group_regex] for i in number_regex_list]  # noqa
weights_regex_list += [float_regex + '({})'.format(weights_units_group_regex)]
weight_regexes = [r'\s?'.join(i) for i in weights_regex_list]


class WeightEntity(NumberEntity):
    def __init__(self):
        super().__init__()
        self._regexes = weight_regexes

    def name(self):
        return 'std.weight'

    def normalize(self, found_pattern):
        use, value = super().normalize(found_pattern)
        group_dict = found_pattern.groupdict()
        weight_unit = group_dict.get('weight_unit')
        multiplier = self.weight_units_mapping(weight_unit)
        final_value = value * multiplier
        return True, final_value


class WeightEntityKilogram(WeightEntity):
    def __init__(self):
        super().__init__()

    def name(self):
        return 'std.weight.kilogram'

    def weight_units_mapping(self, weight_unit):
        return weight_units_mapping_kilogram[weight_unit]


class WeightEntityMilligram(WeightEntity):
    def __init__(self):
        super().__init__()

    def name(self):
        return 'std.weight.milligram'

    def weight_units_mapping(self, weight_unit):
        return weight_units_mapping_milligram[weight_unit]


def weight_units_set():
    return set(weight_units_mapping_kilogram.keys())
