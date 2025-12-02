def noprofit_noloss(actual_cost: float, sale_amount: float) -> bool:
    if actual_cost <= 0 or sale_amount <= 0:
        raise ValueError("Inputs must be positive numbers")

    if round(actual_cost, 2) == round(sale_amount, 2):
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(noprofit_noloss(1500, 1200), False)

if __name__ == '__main__':
    unittest.main()