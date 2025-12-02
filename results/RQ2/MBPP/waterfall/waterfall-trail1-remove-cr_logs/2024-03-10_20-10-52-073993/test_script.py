def diff_even_odd(list1):
    even_numbers = [num for num in list1 if num % 2 == 0]
    odd_numbers = [num for num in list1 if num % 2 != 0]
    
    if len(even_numbers) == 0 or len(odd_numbers) == 0:
        return "No even or odd numbers found in the input list"
    else:
        return abs(even_numbers[0] - odd_numbers[0])
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(diff_even_odd([1,3,5,7,4,1,6,8]), 3)

if __name__ == '__main__':
    unittest.main()