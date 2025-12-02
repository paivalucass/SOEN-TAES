def loss_amount(actual_cost, sale_amount):
    if actual_cost < 0 or sale_amount < 0:
        raise ValueError("actual_cost and sale_amount must be non-negative numbers")

    if sale_amount >= actual_cost:
        return 0
    else:
        return actual_cost - sale_amount
import unittest

class TestLossAmount(unittest.TestCase):
    def test_loss_no_loss(self):
        self.assertEqual(loss_amount(1500, 1200), 0)

    def test_loss_with_loss(self):
        self.assertEqual(loss_amount(1500, 1000), 500)

if __name__ == '__main__':
    unittest.main()