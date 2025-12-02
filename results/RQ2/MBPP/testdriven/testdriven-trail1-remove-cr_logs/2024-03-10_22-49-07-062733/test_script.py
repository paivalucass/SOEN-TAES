def noprofit_noloss(actual_cost, sale_amount):
    '''
    Function to check whether the given amount has no profit and no loss
    :param actual_cost: The actual cost of the item
    :param sale_amount: The amount it was sold for
    :return: True if there is no profit and no loss, False otherwise
    '''

    if sale_amount < actual_cost:
        return False
    elif sale_amount == actual_cost:
        return True
    else:
        return False

    # Additional input validation to ensure actual_cost and sale_amount are valid numbers and not negative
    if actual_cost < 0 or sale_amount < 0:
        return False

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(noprofit_noloss(1500, 1200), False)

if __name__ == '__main__':
    unittest.main()