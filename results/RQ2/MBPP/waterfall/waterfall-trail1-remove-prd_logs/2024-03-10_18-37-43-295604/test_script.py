def extract_rear(test_tuple):
    if not isinstance(test_tuple, tuple):
        return "Input is not a tuple"
    
    if not test_tuple:
        return "Error: Empty input tuple"
    
    if not all(isinstance(elem, str) for elem in test_tuple):
        return "Error: Non-string elements in input tuple"
    
    rear_chars = [elem[-1] for elem in test_tuple]
    
    return rear_chars
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(extract_rear(('Mers', 'for', 'Vers')), ['s', 'r', 's'])

if __name__ == '__main__':
    unittest.main()