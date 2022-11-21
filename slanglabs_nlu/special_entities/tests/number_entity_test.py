import unittest


from slanglabs_nlu.special_entities.number_entity import NumberEntity, IntegerNumberEntity  # noqa


number2normalized = {
    "zero": 0.0,
    "one": 1.0,
    "two": 2.0,
    "2": 2.0,
    "2.5": 2.5,
    "half": 0.5,
    "quarter": 0.25,
    "100": 100.0,
    "one hundred and twenty five": 125.0,
    "one hundred twenty five": 125.0,
    "seventeen hundred": 1700.0,
    "17 hundred": 1700.0,
    "seventeen hundred and twenty five": 1725.0,
    "seven thousand": 7000.0,
    "7 thousand": 7000.0,
    "seven thousand three hundred": 7300.0,
    "7 thousand three hundred": 7300.0,
    "seven thousand three hundred and forty five": 7345.0,
    "seventeen thousand three hundred": 17300.0,
    "17 thousand three hundred": 17300.0,
    "twenty thousand": 20000.0,
    "20 thousand": 20000.0,
    "seventy thousand three hundred and fifty": 70350.0,
    "70 thousand three hundred and fifty": 70350.0,
    "million": 1000000.0,
    "two million": 2000000.0,
    "2 million": 2000000.0,
    "twenty million": 20000000.0,
    "20 million": 20000000.0,
    "twenty million thirty thousand": 20030000.0,
    "20 million thirty thousand": 20030000.0,
    "seventeen million": 17000000.0,
    "17 million": 17000000.0,
    "seventeen million thirty thousand": 17030000.0,
    "17 million thirty thousand": 17030000.0,
    "seventy million forty thousand three hundred twenty five": 70040325.0,
    "seventy million and two": 70000002.0,
    "hundred": 100.0,
    "dozen": 12.0,
    "thousand": 1000.0,
    "17 lakhs thirty thousand": 1730000.0,
    "seventy lakhs forty thousand three hundred twenty five": 7040325.0,
    "17.5 lakhs and two": 1750002.0,
    "17.5 lacs and two": 1750002.0,
    "17 and a half lakhs": 1750000.0,
    "seventeen and a half lakhs": 1750000.0,
    "17 and a half million": 17500000.0,
    "17 and a quarter thousand": 17250.0,
    "two hundred thousand": 200000.0,
    "200 thousand": 200000.0,
    "crore": 10000000.0,
    "150 crores": 1500000000.0,
    "15 crores fifty lakhs": 155000000.0,
    "4 crore 5 thousand": 40005000.0,
    "2 crores seven hundred": 20000700.0,
    "fifteen crores seventy five": 150000075.0,
    "25 crores and two": 250000002.0,
    "fifteen crores twenty lakhs 5 thousand": 152005000.0,
    "5 crores 10 lakhs five hundred": 51000500.0,
    "eight crores twenty lakhs and nine": 82000009.0,
    "3 crores five lakhs and fifty rupees": 30500050.0,
    "six crores fifty thousand five hundred": 60050500.0,
    "5 crores seven thousand and three": 50007003.0,
    "fifteen crores six hundred and five": 150000605.0,
    "4 crore twenty lacs seven thousand six hundred": 42007600.0,
    "5 crores 10 lakhs and five": 51000005.0,
    "six crores fifty thousand five hundred and nine": 60050509.0,
    "25 crores 5 lakhs 60 thousand 5 hundred and thirty five": 250560535.0,
    "1 lakh 90": 100090,
    "25.5k": 25500.0,
    "25k six hundred and fifty": 25650.0,
    "7 lakhs 50k": 750000.0,
    "under 50k in delhi": 50000.0,
    "7.85 cr": 78500000.0,
    "2cr 40 lakhs": 24000000.0,
    "thousand 324": 1324,
    "thousand 900": 1900,
}

multiple_number2normalized = {
    "from 6000 to 8000": [6000, 8000],
    "between 20 lakh and 40 lakh": [2000000.0, 4000000.0]
}


class NumberEntityTest(unittest.TestCase):
    def setUp(self):
        self.number_entity = NumberEntity()
        self.integer_entity = IntegerNumberEntity()

    def test_number(self):
        expected_answers = []
        predicted_answers = []
        for text, ans in number2normalized.items():
            expected_answers.append(ans)
            for regex in self.number_entity.find_in_text(text):
                predicted_answers.append(regex.normalized_value())
        self.assertEqual(expected_answers, predicted_answers)

    def test_integer(self):
        expected_answers = []
        predicted_answers = []
        for text, ans in number2normalized.items():
            expected_answers.append(int(ans))
            for regex in self.integer_entity.find_in_text(text):
                predicted_answers.append(regex.normalized_value())
        self.assertEqual(expected_answers, predicted_answers)

    def test_multiple_number(self):
        for text, ans in multiple_number2normalized.items():
            values = []
            for regex in self.number_entity.find_in_text(text):
                values.append(regex.normalized_value())
            self.assertEqual(values, ans, msg=text)


if __name__ == '__main__':
    unittest.main()
