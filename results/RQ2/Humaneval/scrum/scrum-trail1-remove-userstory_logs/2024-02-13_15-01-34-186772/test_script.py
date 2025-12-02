def strlen(string: str) -> int:
    if string is None or len(string) == 0:
        return 0
    else:
        return len(string)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(strlen(''), 0)
        self.assertEqual(strlen('abc'), 3)

if __name__ == '__main__':
    unittest.main()