def loss_amount(actual_cost: float, sale_amount: float) -> float:
    difference = sale_amount - actual_cost
    if difference > 0:
        return difference
    else:
        return 0
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(loss_amount(1500, 1200), 0)

if __name__ == '__main__':
    unittest.main()