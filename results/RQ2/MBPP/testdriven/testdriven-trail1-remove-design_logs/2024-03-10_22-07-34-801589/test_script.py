def extract_rear(test_tuple):
    result = []
    for s in test_tuple:
        if isinstance(s, str) and len(s) > 0:
            result.append(s[-1])
        else:
            return "Error: Invalid input data type or empty string"
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(extract_rear(('Mers', 'for', 'Vers')), ['s', 'r', 's'])

if __name__ == '__main__':
    unittest.main()