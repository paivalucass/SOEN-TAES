def noprofit_noloss(actual_cost: float, sale_amount: float) -> bool:
    difference = sale_amount - actual_cost
    if difference > 0 or difference < 0:
        return False
    else:
        return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(noprofit_noloss(1500, 1200), False)

if __name__ == '__main__':
    unittest.main()