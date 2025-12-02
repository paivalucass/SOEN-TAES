def sum_range_list(list1, m, n):
    if not isinstance(list1, list):
        return "Input list is not valid"
    if not all(isinstance(x, (int, float)) for x in list1):
        return "List contains non-numeric values"

    if m < 0 or n < 0 or m >= len(list1) or n >= len(list1) or m > n:
        return "Invalid indices"

    return sum(list1[m:n+1]) if list1 else 0
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 8, 10), 29)

if __name__ == '__main__':
    unittest.main()