def extract_rear(test_tuple):
    if not isinstance(test_tuple, tuple):
        raise TypeError("Input should be a tuple")

    result = []
    for item in test_tuple:
        if not isinstance(item, str):
            raise TypeError("Tuple should only contain strings")
        result.append(item[-1])

    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(extract_rear(('Mers', 'for', 'Vers')), ['s', 'r', 's'])

if __name__ == '__main__':
    unittest.main()