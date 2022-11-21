import unittest


from slanglabs_nlu.special_entities.weight_entity import (
    WeightEntityKilogram, WeightEntityMilligram
)


weight2normalized = {
    "zero kg": 0.0,
    "one tonne": 1000.0,
    "two kgs": 2.0,
    "2g": 2.0,
    "2.5kg": 2.5,
    "half kg": 0.5,
    "quater kilogram": 0.25,
    "100 gram": 0.1,
    "one hundred and twenty five kilograms": 125.0,
    "one hundred twenty five kg": 125.0,
    "seventeen hundred gram": 1.7,
    "17 hundred gram": 1.7,
    "seventeen hundred and twenty five kg": 1725.0,
    "seven thousand kg": 7000.0,
    "7 thousand kg": 7000.0,
    "seven thousand three hundred kg": 7300.0,
    "7 thousand three hundred kg": 7300.0,
    "seven thousand three hundred and forty five kg": 7345.0,
    "seventeen thousand three hundred kg": 17300.0,
    "17 thousand three hundred kg": 17300.0,
    "twenty thousand kg": 20000.0,
    "20 thousand kg": 20000.0,
    "seventy thousand three hundred and fifty kg": 70350.0,
    "70 thousand three hundred and fifty kg": 70350.0,
    "million kgs": 1000000.0,
    "two million kgs": 2000000.0,
    "2 million kgs": 2000000.0,
    "twenty million kgs": 20000000.0,
    "20 million kgs": 20000000.0,
    "twenty million thirty thousand kgs": 20030000.0,
    "20 million thirty thousand kgs": 20030000.0,
    "seventeen million kgs": 17000000.0,
    "17 million kgs": 17000000.0,
    "seventeen million thirty thousand kgs": 17030000.0,
    "17 million thirty thousand kgs": 17030000.0,
    "seventy million forty thousand three hundred twenty five kgs": 70040325.0,
    "seventy million and two kgs": 70000002.0,
    "hundred kgs": 100.0,
    "dozen kgs": 12.0,
    "thousand kgs": 1000.0,
}


class WeightEntityTest(unittest.TestCase):
    def test_weight_kgs(self):
        self.weight_entity = WeightEntityKilogram()
        for text, ans in weight2normalized.items():
            for regex in self.weight_entity.find_in_text(text):
                self.assertEqual(regex.normalized_value(), ans, msg=text)

    def test_weight_grams(self):
        self.weight_entity = WeightEntityMilligram()
        for text, ans in weight2normalized.items():
            for regex in self.weight_entity.find_in_text(text):
                self.assertEqual(regex.normalized_value(), ans * 10**6, msg=text)  # noqa


if __name__ == '__main__':
    unittest.main()
