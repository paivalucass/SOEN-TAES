def sum_range_list(list1, m, n):
    if not isinstance(list1, list) or not all(isinstance(x, (int, float)) for x in list1) or not isinstance(m, int) or not isinstance(n, int):
        raise TypeError("Input list must be a list of numbers and m and n must be integers")
    
    if not list1 or m > n:
        raise ValueError("Input list must not be empty and m must be less than or equal to n")

    return sum(list1[m:n+1])
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 8, 10), 29)

if __name__ == '__main__':
    unittest.main()