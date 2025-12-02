def all_Characters_Same(s):
    for char in s:
        if char != s[0]:
            return False
    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(all_Characters_Same('python'), False)

if __name__ == '__main__':
    unittest.main()