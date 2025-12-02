def loss_amount(actual_cost, sale_amount):
    if isinstance(actual_cost, (int, float)) and isinstance(sale_amount, (int, float)):
        loss = actual_cost - sale_amount
        return max(0, loss)
    else:
        return "Invalid input"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(loss_amount(1500, 1200), 0)

if __name__ == '__main__':
    unittest.main()