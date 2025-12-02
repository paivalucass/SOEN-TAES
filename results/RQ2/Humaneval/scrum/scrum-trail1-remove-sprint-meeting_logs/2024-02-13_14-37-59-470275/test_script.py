def get_positive(input_list: list) -> list:
    if input_list is None or not isinstance(input_list, list):
        raise ValueError("Input should be a non-empty list")
    
    result = [num for num in input_list if num > 0]
    return result
import unittest

class Test(unittest.TestCase):
    def test_get_positive(self):
        self.assertEqual(get_positive([-1, 2, -4, 5, 6]), [2, 5, 6])
        self.assertEqual(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]), [5, 3, 2, 3, 9, 123, 1])

if __name__ == '__main__':
    unittest.main()