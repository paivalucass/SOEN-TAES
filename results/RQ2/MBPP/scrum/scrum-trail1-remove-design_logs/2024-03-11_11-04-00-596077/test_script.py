def noprofit_noloss(actual_cost, sale_amount):
    if actual_cost <= 0 or sale_amount <= 0:
        return "Invalid input"
    elif actual_cost == sale_amount:
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(noprofit_noloss(1500, 1200), False)

if __name__ == '__main__':
    unittest.main()