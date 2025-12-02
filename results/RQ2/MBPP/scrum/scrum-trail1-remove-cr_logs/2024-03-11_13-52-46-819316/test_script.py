def noprofit_noloss(actual_cost, sale_amount):
    if not isinstance(actual_cost, (int, float)) or not isinstance(sale_amount, (int, float)):
        return "Invalid Input"
    if sale_amount < actual_cost:
        return False
    elif sale_amount == actual_cost:
        return True
    else:
        return False

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(noprofit_noloss(1500, 1200), False)

if __name__ == '__main__':
    unittest.main()