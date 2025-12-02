def split_odd_numbers(input_list):
    if not isinstance(input_list, list) or not all(isinstance(x, int) for x in input_list):
        return "Input is not a list of integers"
    odd_numbers = [num for num in input_list if num % 2 != 0]
    return odd_numbers
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Split([1,2,3,4,5,6]), [1,3,5])

if __name__ == '__main__':
    unittest.main()