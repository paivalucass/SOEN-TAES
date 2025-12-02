def split_even_numbers(input_list):
    return [num for num in input_list if num % 2 == 0]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Split([1,2,3,4,5]), [2,4])

if __name__ == '__main__':
    unittest.main()