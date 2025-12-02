def diff_even_odd(list1):
    even_number = None
    odd_number = None
    for number in list1:
        if number % 2 == 0 and even_number is None:
            even_number = number
        elif number % 2 != 0 and odd_number is None:
            odd_number = number
        if even_number is not None and odd_number is not None:
            return abs(even_number - odd_number)
    return "No even or odd numbers found in the list."
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(diff_even_odd([1,3,5,7,4,1,6,8]), 3)

if __name__ == '__main__':
    unittest.main()