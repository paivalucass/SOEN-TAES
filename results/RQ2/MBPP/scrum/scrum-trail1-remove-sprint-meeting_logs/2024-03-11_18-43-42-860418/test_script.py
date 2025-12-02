def extract_rear(test_tuple):
    if not isinstance(test_tuple, tuple):
        raise TypeError("Input should be a tuple")

    result = []

    for string in test_tuple:
        if not isinstance(string, str):
            raise TypeError("All elements in the tuple should be strings")

        if not string:
            raise ValueError("String within the tuple should not be empty")

        result.append(string[-1])

    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(extract_rear(('Mers', 'for', 'Vers')), ['s', 'r', 's'])

if __name__ == '__main__':
    unittest.main()