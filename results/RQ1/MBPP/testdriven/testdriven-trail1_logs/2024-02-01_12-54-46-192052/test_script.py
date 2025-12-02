def split_odd_numbers(input_list):
    if len(input_list) == 0:
        return []
    elif all(num % 2 == 0 for num in input_list):
        return "Error: Invalid Input"
    else:
        return [num for num in input_list if num % 2 != 0]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Split([1,2,3,4,5,6]), [1,3,5])

if __name__ == '__main__':
    unittest.main()