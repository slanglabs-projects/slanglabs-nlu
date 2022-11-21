import unittest


from slanglabs_nlu.special_entities.volume_composite_entity import (
    VolumeCompositeEntity
)


volume2normalized = {
    "zero l": {'std_volume_value': 0.0, 'std_volume_unit': 'l'},
    "one meter cube": {'std_volume_value': 1.0, 'std_volume_unit': 'm3'},
    "two liters": {'std_volume_value': 2.0, 'std_volume_unit': 'l'},
    "2ml": {'std_volume_value': 2.0, 'std_volume_unit': 'ml'},
    "2.5l": {'std_volume_value': 2.5, 'std_volume_unit': 'l'},
    "half cc": {'std_volume_value': 0.5, 'std_volume_unit': 'ml'},
    "quarter liter": {'std_volume_value': 0.25, 'std_volume_unit': 'l'},
    "100 ml": {'std_volume_value': 100, 'std_volume_unit': 'ml'},
    "one hundred and twenty five milliliter": {'std_volume_value': 125.0, 'std_volume_unit': 'ml'},  # noqa
    "one hundred twenty five mls": {'std_volume_value': 125.0, 'std_volume_unit': 'ml'},  # noqa
    "seventeen hundred liters": {'std_volume_value': 1700.0, 'std_volume_unit': 'l'},  # noqa
    "17 hundred cubic meters": {'std_volume_value': 1700.0, 'std_volume_unit': 'm3'}, # noqa
    "seventeen hundred and twenty five cubic centimeter": {'std_volume_value': 1725.0, 'std_volume_unit': 'ml'},  # noqa
    "seven thousand ccs": {'std_volume_value': 7000.0, 'std_volume_unit': 'ml'},  # noqa
    "7 thousand ml": {'std_volume_value': 7000.0, 'std_volume_unit': 'ml'},
    "seven thousand three hundred l": {'std_volume_value': 7300.0, 'std_volume_unit': 'l'},  # noqa
    "7 thousand three hundred l": {'std_volume_value': 7300.0, 'std_volume_unit': 'l'},  # noqa
    "seven thousand three hundred and forty five l": {'std_volume_value': 7345.0, 'std_volume_unit': 'l'},  # noqa
    "seventeen thousand three hundred l": {'std_volume_value': 17300.0, 'std_volume_unit': 'l'},  # noqa
    "17 thousand three hundred l": {'std_volume_value': 17300.0, 'std_volume_unit': 'l'},  # noqa
    "twenty thousand l": {'std_volume_value': 20000.0, 'std_volume_unit': 'l'},  # noqa
    "20 thousand l": {'std_volume_value': 20000.0, 'std_volume_unit': 'l'},  # noqa
    "seventy thousand three hundred and fifty l": {'std_volume_value': 70350.0, 'std_volume_unit': 'l'},  # noqa
    "70 thousand three hundred and fifty l": {'std_volume_value': 70350.0, 'std_volume_unit': 'l'},  # noqa
    "million l": {'std_volume_value': 10.0**6, 'std_volume_unit': 'l'},  # noqa
    "two million l": {'std_volume_value': 2 * 10.0**6, 'std_volume_unit': 'l'},  # noqa
    "2 million l": {'std_volume_value': 2 * 10.0**6, 'std_volume_unit': 'l'},  # noqa
    "twenty million l": {'std_volume_value': 20 * 10.0**6, 'std_volume_unit': 'l'},  # noqa
    "20 million l": {'std_volume_value': 20 * 10.0**6, 'std_volume_unit': 'l'},  # noqa
    "twenty million thirty thousand l": {'std_volume_value': 20030000.0, 'std_volume_unit': 'l'},  # noqa
    "20 million thirty thousand l": {'std_volume_value': 20030000.0, 'std_volume_unit': 'l'},  # noqa
    "seventeen million l": {'std_volume_value': 17000000.0, 'std_volume_unit': 'l'},  # noqa
    "17 million l": {'std_volume_value': 17000000.0, 'std_volume_unit': 'l'},  # noqa
    "seventeen million thirty thousand l": {'std_volume_value': 17030000.0, 'std_volume_unit': 'l'},  # noqa
    "17 million thirty thousand l": {'std_volume_value': 17030000.0, 'std_volume_unit': 'l'},  # noqa
    "seventy million forty thousand three hundred twenty five l": {'std_volume_value': 70040325.0, 'std_volume_unit': 'l'},  # noqa
    "seventy million and two l": {'std_volume_value': 70000002.0, 'std_volume_unit': 'l'},  # noqa
    "hundred l": {'std_volume_value': 100.0, 'std_volume_unit': 'l'},  # noqa
    "dozen l": {'std_volume_value': 12.0, 'std_volume_unit': 'l'},  # noqa
    "thousand l": {'std_volume_value': 1000.0, 'std_volume_unit': 'l'},  # noqa
    "liter": {'std_volume_value': 1.0, 'std_volume_unit': 'l'},  # noqa
    "milliliter": {'std_volume_value': 1.0, 'std_volume_unit': 'ml'},  # noqa
    "20 quarts": {'std_volume_value': 20.0, 'std_volume_unit': 'quarts'},   # noqa
    "a quart": {'std_volume_value': 1.0, 'std_volume_unit': 'quarts'},     # noqa
    "three fluid ounce": {'std_volume_value': 3.0, 'std_volume_unit': 'fluid oz'},   # noqa
    "30.5 fluid oz": {'std_volume_value': 30.5, 'std_volume_unit': 'fluid oz'},   # noqa
    "one hundred and ninety cubic foot": {'std_volume_value': 190.0, 'std_volume_unit': 'cu. ft'},   # noqa
    "one hundred and seventy cubic feet": {'std_volume_value': 170.0, 'std_volume_unit': 'cu. ft'},   # noqa
    "seventeen thousand one hundred cubic inches": {'std_volume_value': 17100.0, 'std_volume_unit': 'cu. in'},   # noqa
    "seventeen thousand and eighty gallons": {'std_volume_value': 17080.0, 'std_volume_unit': 'gallon'},   # noqa
}


class VolumeCompositeEntityTest(unittest.TestCase):
    def test_weight(self):
        self.volume_entity = VolumeCompositeEntity()
        for text, ans in volume2normalized.items():
            for regex in self.volume_entity.find_in_text(text):
                self.assertEqual(regex.normalized_value(), ans, msg=text)


if __name__ == '__main__':
    unittest.main()
