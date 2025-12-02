def remove_Occ(s, ch):
    return s.replace(ch, '', 1).rsplit(ch, 1)[0] + s.rsplit(ch, 1)[-1] if s.count(ch) > 1 else s
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_Occ("hello", "l"), "heo")

if __name__ == '__main__':
    unittest.main()