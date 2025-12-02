def extract_rear(test_tuple):
    result = []
    for item in test_tuple:
        if isinstance(item, str) and len(item) > 0:
            result.append(item[-1])
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(extract_rear(('Mers', 'for', 'Vers')), ['s', 'r', 's'])

if __name__ == '__main__':
    unittest.main()