import unittest


from slanglabs_nlu.special_entities.volume_entity import (
    VolumeEntityLitre, VolumeEntityMillilitre
)


volume2normalized = {
    "zero litre": 0.0,
    "one liter": 1.0,
    "two meter cube": 2000.0,
    "2ml": 0.002,
    "2.5l": 2.5,
    "half l": 0.5,
    "quater liter": 0.25,
    "100 ml": 0.1,
    "one hundred and twenty five liter": 125.0,
    "one hundred twenty five liter": 125.0,
    "seventeen hundred ml": 1.7,
    "17 hundred mls": 1.7,
    "seventeen hundred and twenty five liter": 1725.0,
    "seven thousand liter": 7000.0,
    "7 thousand liters": 7000.0,
    "seven thousand three hundred litres": 7300.0,
    "7 thousand three hundred cubic meters": 7300000.0,
    "seven thousand three hundred and forty five liter": 7345.0,
    "seventeen thousand three hundred liter": 17300.0,
    "17 thousand three hundred liter": 17300.0,
    "twenty thousand liter": 20000.0,
    "20 thousand litre": 20000.0,
    "seventy thousand three hundred and fifty liter": 70350.0,
    "70 thousand three hundred and fifty liter": 70350.0,
    "million liter": 1000000.0,
    "two million liter": 2000000.0,
    "2 million cc": 2000.0,
    "twenty million ccs": 20000000000.0,
    "20 million liter": 20000000.0,
    "twenty million thirty thousand liter": 20030000.0,
    "20 million thirty thousand liter": 20030000.0,
    "seventeen million liter": 17000000.0,
    "17 million liter": 17000000.0,
    "seventeen million thirty thousand liter": 17030000.0,
    "17 million thirty thousand liter": 17030000.0,
    "seventy million forty thousand three hundred twenty five liter": 70040325.0,  # noqa
    "seventy million and two liter": 70000002.0,
    "hundred liter": 100.0,
    "dozen liter": 12.0,
    "thousand liter": 1000.0,
}


class VolumeEntityTest(unittest.TestCase):
    def test_volume_litre(self):
        self.weight_entity = VolumeEntityLitre()
        for text, ans in volume2normalized.items():
            for regex in self.weight_entity.find_in_text(text):
                self.assertEqual(regex.normalized_value(), ans, msg=text)

    def test_volume_millilitres(self):
        self.weight_entity = VolumeEntityMillilitre()
        for text, ans in volume2normalized.items():
            for regex in self.weight_entity.find_in_text(text):
                self.assertEqual(regex.normalized_value(), ans * 10**3, msg=text)  # noqa


if __name__ == '__main__':
    unittest.main()
