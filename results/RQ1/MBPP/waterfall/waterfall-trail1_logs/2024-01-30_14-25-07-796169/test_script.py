def extract_rear(test_tuple):
    if not isinstance(test_tuple, tuple):
        raise TypeError("Input must be a tuple")
    for string in test_tuple:
        if not isinstance(string, str):
            raise TypeError("Elements in the tuple must be strings")
    rear_chars = [string[-1] for string in test_tuple]
    return rear_chars
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(extract_rear(('Mers', 'for', 'Vers')), ['s', 'r', 's'])

if __name__ == '__main__':
    unittest.main()