def loss_amount(actual_cost, sale_amount):
    if not isinstance(actual_cost, (int, float)) or not isinstance(sale_amount, (int, float)):
        raise ValueError("actual_cost and sale_amount must be numbers")
    if actual_cost < 0 or sale_amount < 0:
        raise ValueError("actual_cost and sale_amount must be positive numbers")

    if actual_cost < sale_amount:
        return sale_amount - actual_cost
    else:
        return 0
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(loss_amount(1500, 1200), 0)

if __name__ == '__main__':
    unittest.main()