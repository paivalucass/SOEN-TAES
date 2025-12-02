def loss_amount(actual_cost, sale_amount):
    return max(actual_cost - sale_amount, 0)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(loss_amount(1500, 1200), 0)

if __name__ == '__main__':
    unittest.main()