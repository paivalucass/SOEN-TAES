def sum_squares(lst):
    """"
    This function will take a list of integers. For all entries in the list, the function shall square the integer entry if its index is a 
    multiple of 3 and will cube the integer entry if its index is a multiple of 4 and not a multiple of 3. The function will not 
    change the entries in the list whose indexes are not a multiple of 3 or 4. The function shall then return the sum of all entries. 
    
    Examples:
    For lst = [1,2,3] the output should be 6
    For lst = []  the output should be 0
    For lst = [-1,-5,2,-1,-5]  the output should be -126
    """
    try:
        if not all(isinstance(x, int) for x in lst):
            raise ValueError("Input list must contain only integers")

        result = 0
        for i in range(len(lst)):
            if i % 4 == 0 and i % 3 != 0:
                result += lst[i] ** 3
            else:
                result += lst[i] ** 2

        return result
    except IndexError:
        raise IndexError("Index out of range when accessing list elements")
import unittest

class Test(unittest.TestCase):
    def test_sum_squares(self):
        self.assertEqual(sum_squares([1,2,3]), 6)
        self.assertEqual(sum_squares([]), 0)
        self.assertEqual(sum_squares([-1,-5,2,-1,-5]), -126)

if __name__ == '__main__':
    unittest.main()