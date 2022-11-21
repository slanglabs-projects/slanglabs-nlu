import unittest


from slanglabs_nlu.special_entities.weight_composite_entity import (
    WeightCompositeEntity
)


weight2normalized = {
    "zero kg": {'std_weight_value': 0.0, 'std_weight_unit': 'kg'},
    "one tonne": {'std_weight_value': 1.0, 'std_weight_unit': 't'},
    "two kgs": {'std_weight_value': 2.0, 'std_weight_unit': 'kg'},
    "2g": {'std_weight_value': 2.0, 'std_weight_unit': 'g'},
    "2.5kg": {'std_weight_value': 2.5, 'std_weight_unit': 'kg'},
    "half kg": {'std_weight_value': 0.5, 'std_weight_unit': 'kg'},
    "quarter kilogram": {'std_weight_value': 0.25, 'std_weight_unit': 'kg'},
    "100 gram": {'std_weight_value': 100, 'std_weight_unit': 'g'},
    "one hundred and twenty five kilograms": {'std_weight_value': 125.0, 'std_weight_unit': 'kg'},  # noqa
    "one hundred twenty five kg": {'std_weight_value': 125.0, 'std_weight_unit': 'kg'},  # noqa
    "seventeen hundred gram": {'std_weight_value': 1700.0, 'std_weight_unit': 'g'},  # noqa
    "17 hundred gram": {'std_weight_value': 1700.0, 'std_weight_unit': 'g'},
    "seventeen hundred and twenty five kg": {'std_weight_value': 1725.0, 'std_weight_unit': 'kg'},  # noqa
    "seven thousand kg": {'std_weight_value': 7000.0, 'std_weight_unit': 'kg'},
    "7 thousand kg": {'std_weight_value': 7000.0, 'std_weight_unit': 'kg'},
    "seven thousand three hundred kg": {'std_weight_value': 7300.0, 'std_weight_unit': 'kg'},  # noqa
    "7 thousand three hundred kg": {'std_weight_value': 7300.0, 'std_weight_unit': 'kg'},  # noqa
    "seven thousand three hundred and forty five kg": {'std_weight_value': 7345.0, 'std_weight_unit': 'kg'},  # noqa
    "seventeen thousand three hundred kg": {'std_weight_value': 17300.0, 'std_weight_unit': 'kg'},  # noqa
    "17 thousand three hundred kg": {'std_weight_value': 17300.0, 'std_weight_unit': 'kg'},  # noqa
    "twenty thousand kg": {'std_weight_value': 20000.0, 'std_weight_unit': 'kg'},  # noqa
    "20 thousand kg": {'std_weight_value': 20000.0, 'std_weight_unit': 'kg'},  # noqa
    "seventy thousand three hundred and fifty kg": {'std_weight_value': 70350.0, 'std_weight_unit': 'kg'},  # noqa
    "70 thousand three hundred and fifty kg": {'std_weight_value': 70350.0, 'std_weight_unit': 'kg'},  # noqa
    "million kgs": {'std_weight_value': 10.0**6, 'std_weight_unit': 'kg'},  # noqa
    "two million kgs": {'std_weight_value': 2 * 10.0**6, 'std_weight_unit': 'kg'},  # noqa
    "2 million kgs": {'std_weight_value': 2 * 10.0**6, 'std_weight_unit': 'kg'},  # noqa
    "twenty million kgs": {'std_weight_value': 20 * 10.0**6, 'std_weight_unit': 'kg'},  # noqa
    "20 million kgs": {'std_weight_value': 20 * 10.0**6, 'std_weight_unit': 'kg'},  # noqa
    "twenty million thirty thousand kgs": {'std_weight_value': 20030000.0, 'std_weight_unit': 'kg'},  # noqa
    "20 million thirty thousand kgs": {'std_weight_value': 20030000.0, 'std_weight_unit': 'kg'},  # noqa
    "seventeen million kgs": {'std_weight_value': 17000000.0, 'std_weight_unit': 'kg'},  # noqa
    "17 million kgs": {'std_weight_value': 17000000.0, 'std_weight_unit': 'kg'},  # noqa
    "seventeen million thirty thousand kgs": {'std_weight_value': 17030000.0, 'std_weight_unit': 'kg'},  # noqa
    "17 million thirty thousand kgs": {'std_weight_value': 17030000.0, 'std_weight_unit': 'kg'},  # noqa
    "seventy million forty thousand three hundred twenty five kgs": {'std_weight_value': 70040325.0, 'std_weight_unit': 'kg'},  # noqa
    "seventy million and two kgs": {'std_weight_value': 70000002.0, 'std_weight_unit': 'kg'},  # noqa
    "hundred kgs": {'std_weight_value': 100.0, 'std_weight_unit': 'kg'},  # noqa
    "dozen kgs": {'std_weight_value': 12.0, 'std_weight_unit': 'kg'},  # noqa
    "thousand kgs": {'std_weight_value': 1000.0, 'std_weight_unit': 'kg'},  # noqa
    "kgs": {'std_weight_value': 1.0, 'std_weight_unit': 'kg'},  # noqa
    "kilo": {'std_weight_value': 1.0, 'std_weight_unit': 'kg'},  # noqa
    "seventeen pounds": {'std_weight_value': 17.0, 'std_weight_unit': 'lbs'},  # noqa
    "13 ounces": {'std_weight_value': 13.0, 'std_weight_unit': 'oz'},  # noqa
    "pounds": {'std_weight_value': 1.0, 'std_weight_unit': 'lbs'},  # noqa
}


class WeightCompositeEntityTest(unittest.TestCase):
    def test_weight(self):
        self.weight_entity = WeightCompositeEntity()
        for text, ans in weight2normalized.items():
            for regex in self.weight_entity.find_in_text(text):
                self.assertEqual(regex.normalized_value(), ans, msg=text)


if __name__ == '__main__':
    unittest.main()
