def loss_amount(actual_cost, sale_amount):
    if actual_cost > sale_amount:
        return actual_cost - sale_amount
    else:
        return 0
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(loss_amount(1500, 1200), 0)

if __name__ == '__main__':
    unittest.main()