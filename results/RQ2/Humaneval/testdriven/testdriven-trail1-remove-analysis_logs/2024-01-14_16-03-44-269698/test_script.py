def sum_squares(lst):
    """
    This function takes a list of integers. For all entries in the list, the function squares the integer entry if its index is a
    multiple of 3 and cubes the integer entry if its index is a multiple of 4 and not a multiple of 3. The function does not
    change the entries in the list whose indexes are not a multiple of 3 or 4. The function then returns the sum of all entries.

    Examples:
    For lst = [1,2,3] the output should be 6
    For lst = []  the output should be 0
    For lst = [-1,-5,2,-1,-5]  the output should be -126
    """
    if len(lst) == 0:
        return 0
    else:
        total = 0
        for i, num in enumerate(lst):
            if i % 3 == 0:
                total += num ** 2
            elif i % 4 == 0 and i % 3 != 0:
                total += num ** 3
            else:
                total += num
        return total
import unittest

class Test(unittest.TestCase):
    def test_sum_squares(self):
        self.assertEqual(sum_squares([1,2,3]), 6)
        self.assertEqual(sum_squares([]), 0)
        self.assertEqual(sum_squares([-1,-5,2,-1,-5]), -126)

if __name__ == '__main__':
    unittest.main()