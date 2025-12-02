def find_even_numbers(input_list):
    if not isinstance(input_list, list):
        return "Error: Input data is not a list"
    
    even_numbers = [num for num in input_list if num % 2 == 0]
    return even_numbers
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Split([1,2,3,4,5]), [2,4])

if __name__ == '__main__':
    unittest.main()