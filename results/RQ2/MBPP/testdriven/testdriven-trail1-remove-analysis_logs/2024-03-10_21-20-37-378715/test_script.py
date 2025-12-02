def loss_amount(actual_cost, sale_amount):
    if not isinstance(actual_cost, int) or not isinstance(sale_amount, int):
        raise TypeError("Input parameters must be integers")
    if actual_cost < 0 or sale_amount < 0:
        raise ValueError("Invalid input")
    return max(0, actual_cost - sale_amount)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(loss_amount(1500, 1200), 0)

if __name__ == '__main__':
    unittest.main()