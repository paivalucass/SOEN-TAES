def loss_amount(actual_cost, sale_amount):
    if isinstance(actual_cost, (int, float)) and isinstance(sale_amount, (int, float)):
        if actual_cost > 0 and sale_amount > 0:
            if sale_amount < actual_cost:
                return actual_cost - sale_amount
            else:
                return 0
        else:
            return 'Sale amount and actual cost must be greater than 0'
    else:
        return 'Invalid input'
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(loss_amount(1500, 1200), 0)

if __name__ == '__main__':
    unittest.main()