from slanglabs_nlu.special_entities.number_entity import (
    NumberEntity, number_regex_list, float_regex, int_regex
)

m3_unit_mapping = {
    'meter cube': 'm3',
    'cubic meters': 'm3',
    'cubic meter': 'm3',
    'metre cube': 'm3',
    'cubic metres': 'm3',
    'cubic metre': 'm3',
    'meters cube': 'm3',
    'metres cube': 'm3',
}

l_unit_mapping = {
    'liters': 'l',
    'litres': 'l',
    'litre': 'l',
    'liter': 'l',
    'l': 'l',
}

ml_unit_mapping = {
    'ml': 'ml',
    'milliliters': 'ml',
    'millilitres': 'ml',
    'milliliter': 'ml',
    'millilitre': 'ml',
    'ccs': 'ml',
    'cc': 'ml',
    'centimeter cube': 'ml',
    'centimetre cube': 'ml',
    'centimeters cube': 'ml',
    'centimetres cube': 'ml',
    'cubic centimeters': 'ml',
    'cubic centimetres': 'ml',
    'cubic centimeter': 'ml',
    'cubic centimetre': 'ml',
}

cubic_inch_mapping = {
    'cubic inches': 'cu. in',
    'cubic inch': 'cu. in'
}

cubic_foot_mapping = {
    'cubic foot': 'cu. ft',
    'cubic feet': 'cu. ft',
}

quarts_mapping = {
    'quarts': 'quarts',
    'quart': 'quarts',
}

fluid_ounce_mapping = {
    'fluid oz': 'fluid oz',
    'fluid ounces': 'fluid oz',
    'fluidounces': 'fluid oz',
    'fluid ounce': 'fluid oz',
    'fluidounce': 'fluid oz',
}

gallon_mapping = {
    'gallons': 'gallon',
    'gallon': 'gallon',
    'gal': 'gallon',
    'gl': 'gallon',
}

volume_units_mapping = {
    **m3_unit_mapping,
    **l_unit_mapping,
    **ml_unit_mapping,
    **cubic_inch_mapping,
    **cubic_foot_mapping,
    **quarts_mapping,
    **fluid_ounce_mapping,
    **gallon_mapping,
}

volume_units_regex = '|'.join(volume_units_mapping.keys())
volume_units_group_regex = r'(?P<volume_unit>{})'.format(volume_units_regex)
volume_regex_list = [i + [volume_units_group_regex] for i in number_regex_list]  # noqa
volume_regex_list += [float_regex + '({})'.format(volume_units_group_regex)]
volume_regex_list += [int_regex + '({})'.format(volume_units_group_regex)]
volume_regex_list += [[volume_units_group_regex]]
volume_regexes = [r'\s?'.join(i) for i in volume_regex_list]


class VolumeCompositeEntity(NumberEntity):
    def __init__(self):
        super().__init__()
        self._regexes = volume_regexes

    def name(self):
        return 'std.volume'

    def entity2entitytypes(self):
        return {
            'std_volume_value': 'std.float',
            'std_volume_unit': 'std.volume.unit'
        }

    def normalize(self, found_pattern):
        use, value = super().normalize(found_pattern)
        if use is False:
            value = 1.0
        group_dict = found_pattern.groupdict()
        volume_unit = group_dict.get('volume_unit')
        volume_unit = volume_units_mapping.get(volume_unit)
        return True, {'std_volume_value': value, 'std_volume_unit': volume_unit}  # noqa
