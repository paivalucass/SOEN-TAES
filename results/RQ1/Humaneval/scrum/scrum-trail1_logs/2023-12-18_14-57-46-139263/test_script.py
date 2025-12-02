def strlen(string: str) -> int:
    if string is None:
        return 0
    elif isinstance(string, str):
        return len(string)
    else:
        return "Invalid input"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(strlen(''), 0)
        self.assertEqual(strlen('abc'), 3)

if __name__ == '__main__':
    unittest.main()