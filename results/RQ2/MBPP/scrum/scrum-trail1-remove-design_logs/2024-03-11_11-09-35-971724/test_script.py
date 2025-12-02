def all_Characters_Same(s):
    return len(set(s)) == 1 if s else False
import unittest

class Test(unittest.TestCase):
    def test_all_characters_same(self):
        self.assertEqual(all_Characters_Same('python'), False)

if __name__ == '__main__':
    unittest.main()