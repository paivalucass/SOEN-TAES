def larg_nnum(input_list, n):
    '''
    Write a function that takes in a list and an integer n and returns a list containing the n largest items from the list.
    assert set(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],2))==set([100,90])
    '''
    if not input_list:
        return []
    if n <= 0:
        return []
    if n >= len(input_list):
        return input_list
    if not all(isinstance(item, (int, float)) for item in input_list):
        return "Error message should be returned"
    return sorted(input_list, reverse=True)[:n]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100], 2), [100, 90])

if __name__ == '__main__':
    unittest.main()