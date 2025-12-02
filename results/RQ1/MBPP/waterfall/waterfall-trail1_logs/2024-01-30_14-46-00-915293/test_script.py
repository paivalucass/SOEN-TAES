def diff_even_odd(input_list):
    if not isinstance(input_list, list):
        raise TypeError("Input parameter must be a list")

    even_nums = [num for num in input_list if num % 2 == 0]
    odd_nums = [num for num in input_list if num % 2 != 0]

    if len(even_nums) == 0 or len(odd_nums) == 0:
        return None

    return min(even_nums) - min(odd_nums)

assert diff_even_odd([1,3,5,7,4,1,6,8])==3
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(diff_even_odd([1,3,5,7,4,1,6,8]), 3)

if __name__ == '__main__':
    unittest.main()