def unique(input_list: list) -> list:
    if not input_list:
        raise ValueError("Input list is empty")
    
    if not isinstance(input_list, list):
        raise ValueError("Input is not a list")
    
    unique_elements = list(set(input_list))
    unique_elements.sort()
    
    return unique_elements
import unittest

class Test(unittest.TestCase):
    def test_unique(self):
        self.assertEqual(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]), [0, 2, 3, 5, 9, 123])

if __name__ == '__main__':
    unittest.main()