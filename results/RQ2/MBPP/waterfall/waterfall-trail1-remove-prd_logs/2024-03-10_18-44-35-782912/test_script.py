def is_upper(string: str) -> str:
    if not isinstance(string, str):
        raise TypeError("Input is not a valid string type")

    if not string:
        raise ValueError("Input string is empty")

    return string.upper()
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_upper('person'), 'PERSON')

if __name__ == '__main__':
    unittest.main()