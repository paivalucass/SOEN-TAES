def noprofit_noloss(actual_cost, sale_amount):
    '''Write a function to check whether the given amount has no profit and no loss
    assert noprofit_noloss(1500,1200)==False'''
    
    # Check if input values are of type int or float
    if not isinstance(actual_cost, (int, float)) or not isinstance(sale_amount, (int, float)):
        raise TypeError("Input values should be of type int or float")
    
    # Check if sale amount equals actual cost
    if sale_amount == actual_cost:
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(noprofit_noloss(1500, 1200), False)

if __name__ == '__main__':
    unittest.main()