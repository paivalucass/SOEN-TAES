def sum_range_list(list1, m, n):
    if not isinstance(list1, list):
        raise TypeError("Input list must be a valid list")
    if not all(isinstance(x, (int, float)) for x in list1):
        raise ValueError("Input list must contain only numbers")
    if m < 0 or n < 0:
        raise ValueError("Indices m and n must be non-negative")
    if n >= len(list1):
        raise ValueError("Index n is out of bounds")

    return sum(list1[m:n+1])
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 8, 10), 29)

if __name__ == '__main__':
    unittest.main()