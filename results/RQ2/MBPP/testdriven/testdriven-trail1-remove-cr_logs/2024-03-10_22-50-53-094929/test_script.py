def all_Characters_Same(s) :
    if len(s) == 0 or len(set(s)) == 1:
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(all_Characters_Same("python"), False)

if __name__ == '__main__':
    unittest.main()