def extract_rear(test_tuple):
    rear_chars = [string[-1] for string in test_tuple if string]
    return rear_chars
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(extract_rear(('Mers', 'for', 'Vers')), ['s', 'r', 's'])

if __name__ == '__main__':
    unittest.main()