def strlen(string: str) -> int:
    if not isinstance(string, str):
        raise TypeError("Input is not a string type")
    if string is None:
        return 0
    if string == "":
        return 0
    return len(string)
import unittest

class Test(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(strlen(''), 0)

    def test_non_empty_string(self):
        self.assertEqual(strlen('abc'), 3)

if __name__ == '__main__':
    unittest.main()