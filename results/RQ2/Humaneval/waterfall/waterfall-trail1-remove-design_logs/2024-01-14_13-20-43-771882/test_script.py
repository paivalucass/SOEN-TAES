def sum_squares(lst):
    """
    This function will take a list of integers. For all entries in the list, the function shall square the integer entry if its index is a 
    multiple of 3 and will cube the integer entry if its index is a multiple of 4 and not a multiple of 3. The function will not 
    change the entries in the list whose indexes are not a multiple of 3 or 4. The function shall then return the sum of all entries. 
    
    Examples:
    For lst = [1,2,3] the output should be 6
    For lst = []  the output should be 0
    For lst = [-1,-5,2,-1,-5]  the output should be -126
    """

    total = sum([num**2 if idx % 3 == 0 else num**3 if idx % 4 == 0 and idx % 3 != 0 else num for idx, num in enumerate(lst)])
    return total
import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(sum_squares([1,2,3]), 6)

    def test2(self):
        self.assertEqual(sum_squares([]), 0)

    def test3(self):
        self.assertEqual(sum_squares([-1,-5,2,-1,-5]), -126)

if __name__ == '__main__':
    unittest.main()