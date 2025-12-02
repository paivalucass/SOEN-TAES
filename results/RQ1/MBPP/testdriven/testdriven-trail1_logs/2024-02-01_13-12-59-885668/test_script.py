def noprofit_noloss(actual_cost, sale_amount):
    '''Write a function to check whether the given amount has no profit and no loss
    :param actual_cost: numeric value representing the actual cost
    :param sale_amount: numeric value representing the sale amount
    :return: boolean value (True or False) indicating no profit and no loss
    :raises: ValueError for non-numeric inputs and negative values
    '''
    if not (isinstance(actual_cost, (int, float)) and isinstance(sale_amount, (int, float))):
        raise ValueError("Input values must be numeric")
    if actual_cost < 0 or sale_amount < 0:
        raise ValueError("Input values cannot be negative")

    return sale_amount == actual_cost
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(noprofit_noloss(1500, 1200), False)

if __name__ == '__main__':
    unittest.main()