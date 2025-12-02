def diff_even_odd(list1):
    def find_first_even(lst):
        for num in lst:
            if num % 2 == 0:
                return num

    def find_first_odd(lst):
        for num in lst:
            if num % 2 != 0:
                return num

    first_even = find_first_even(list1)
    first_odd = find_first_odd(list1)

    return abs(first_even - first_odd)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(diff_even_odd([1,3,5,7,4,1,6,8]), 3)

if __name__ == '__main__':
    unittest.main()