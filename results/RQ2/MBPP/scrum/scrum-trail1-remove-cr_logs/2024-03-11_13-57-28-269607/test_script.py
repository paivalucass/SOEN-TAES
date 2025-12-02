def all_Characters_Same(s) :
    if not s.strip():
        return False
    first_char = s[0]
    for char in s[1:]:
        if char != first_char:
            return False
    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(all_Characters_Same('python'), False)

if __name__ == '__main__':
    unittest.main()