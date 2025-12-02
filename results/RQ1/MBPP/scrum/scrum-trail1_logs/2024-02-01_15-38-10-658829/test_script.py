def extract_rear(test_tuple):
    if not test_tuple:
        raise ValueError("Input tuple is empty")
    for element in test_tuple:
        if not isinstance(element, str):
            raise TypeError("Input tuple contains non-string elements")
    rear_index_elements = [string[-1] for string in test_tuple]
    return rear_index_elements
import unittest

class Test(unittest.TestCase):
    def test_extract_rear(self):
        self.assertEqual(extract_rear(('Mers', 'for', 'Vers')), ['s', 'r', 's'])

if __name__ == '__main__':
    unittest.main()