def all_Characters_Same(s):
    if not isinstance(s, str) or not s:
        return False
    return all(char == s[0] for char in s)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertFalse(all_Characters_Same("python"))

if __name__ == '__main__':
    unittest.main()