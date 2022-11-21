from slanglabs_nlu.special_entities.number_entity import NumberEntity, number_regex_list, float_regex, int_regex  # noqa


volume_units_mapping_litre = {
    'meter cube': 10.0**3,
    'cubic meter': 10.0**3,
    'metre cube': 10.0**3,
    'cubic metre': 10.0**3,
    'meters cube': 10.0**3,
    'cubic meters': 10.0**3,
    'metres cube': 10.0**3,
    'cubic metres': 10.0**3,
    'litre': 1.0,
    'liter': 1.0,
    'liters': 1.0,
    'litres': 1.0,
    'l': 1.0,
    'ml': 10.0**(-3),
    'milliliters': 10.0**(-3),
    'millilitres': 10.0**(-3),
    'cc': 10.0**(-3),
    'ccs': 10.0**(-3),
    'centimeter cube': 10.0**(-3),
    'centimetre cube': 10.0**(-3),
    'centimeters cube': 10.0**(-3),
    'centimetres cube': 10.0**(-3),
    'cubic centimeter': 10.0**(-3),
    'cubic centimetre': 10.0**(-3),
    'cubic centimeters': 10.0**(-3),
    'cubic centimetres': 10.0**(-3),
}

volume_units_mapping_millilitre = {
    'meter cube': 10.0**6,
    'cubic meter': 10.0**6,
    'metre cube': 10.0**6,
    'cubic metre': 10.0**6,
    'meters cube': 10.0**6,
    'cubic meters': 10.0**6,
    'metres cube': 10.0**6,
    'cubic metres': 10.0**6,
    'litre': 10.0**3,
    'liter': 10.0**3,
    'liters': 10.0**3,
    'litres': 10.0**3,
    'l': 1000.0,
    'ml': 1.0,
    'milliliters': 1.0,
    'millilitres': 1.0,
    'cc': 1.0,
    'ccs': 1.0,
    'centimeter cube': 1.0,
    'centimetre cube': 1.0,
    'centimeters cube': 1.0,
    'centimetres cube': 1.0,
    'cubic centimeter': 1.0,
    'cubic centimetre': 1.0,
    'cubic centimeters': 1.0,
    'cubic centimetres': 1.0,
}

volumes_units_regex = '|'.join(volume_units_mapping_litre.keys())
volumes_units_group_regex = r'(?P<volume_unit>{})'.format(volumes_units_regex)
volumes_regex_list = [i + [volumes_units_group_regex] for i in number_regex_list]  # noqa
volumes_regex_list += [float_regex + '({})'.format(volumes_units_group_regex)]
volume_regexes = [r'\s?'.join(i) for i in volumes_regex_list]


class VolumeEntity(NumberEntity):
    def __init__(self):
        super().__init__()
        self._regexes = volume_regexes

    def name(self):
        return 'std.volume'

    def normalize(self, found_pattern):
        use, value = super().normalize(found_pattern)
        group_dict = found_pattern.groupdict()
        weight_unit = group_dict.get('volume_unit')
        multiplier = self.volume_units_mapping(weight_unit)
        final_value = value * multiplier
        return True, final_value


class VolumeEntityLitre(VolumeEntity):
    def __init__(self):
        super().__init__()

    def name(self):
        return 'std.volume.litre'

    def volume_units_mapping(self, volume_unit):
        return volume_units_mapping_litre[volume_unit]


class VolumeEntityMillilitre(VolumeEntity):
    def __init__(self):
        super().__init__()

    def name(self):
        return 'std.weight.millilitre'

    def volume_units_mapping(self, volume_unit):
        return volume_units_mapping_millilitre[volume_unit]


def volume_units_set():
    return set(volume_units_mapping_litre.keys())
