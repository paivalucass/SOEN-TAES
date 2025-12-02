def all_Characters_Same(s):
    return len(set(s)) == 1
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(all_Characters_Same('python'), False)

if __name__ == '__main__':
    unittest.main()