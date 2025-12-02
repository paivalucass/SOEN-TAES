def strlen(string: str) -> int:
    return len(string)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(strlen(''), 0)
        self.assertEqual(strlen('abc'), 3)

if __name__ == '__main__':
    unittest.main()