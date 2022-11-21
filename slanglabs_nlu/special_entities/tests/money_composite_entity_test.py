import unittest


from slanglabs_nlu.special_entities.money_composite_entity import (
    MoneyCompositeEntity
)


money2normalized = {
    "50 rupees 50 paisa": {'std_money_amount': 50.5, 'std_money_unit': 'INR'},
    "₹1": {'std_money_amount': 1.0, 'std_money_unit': 'INR'},
    "₹ 1": {'std_money_amount': 1.0, 'std_money_unit': 'INR'},
    "1 ₹": {'std_money_amount': 1.0, 'std_money_unit': 'INR'},
    "1₹": {'std_money_amount': 1.0, 'std_money_unit': 'INR'},
    "2.5 rupees": {'std_money_amount': 2.5, 'std_money_unit': 'INR'},
    "one hundred and twenty five rupees": {'std_money_amount': 125.0, 'std_money_unit': 'INR'},  # noqa
    "33 paisa": {'std_money_amount': .33, 'std_money_unit': 'INR'},
    "$1": {'std_money_amount': 1.0, 'std_money_unit': 'USD'},
    "$ 100": {'std_money_amount': 100.0, 'std_money_unit': 'USD'},
    "$ hundred": {'std_money_amount': 100.0, 'std_money_unit': 'USD'},
    "24.99 dollars": {'std_money_amount': 24.99, 'std_money_unit': 'USD'},
}


class MoneyCompositeEntityTest(unittest.TestCase):
    def test_money(self):
        self.money_entity = MoneyCompositeEntity()
        for text, ans in money2normalized.items():
            regex = self.money_entity.find_in_text(text)[0]
            self.assertEqual(regex.normalized_value(), ans, msg=text)


if __name__ == '__main__':
    unittest.main()
