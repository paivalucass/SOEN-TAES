def remove_Occ(s, ch):
    if type(s) != str or len(ch) != 1:
        return "Invalid input"
    if not s:
        return ""
    if ch not in s:
        return s
    s = s.replace(ch, '', 1)
    s = s[::-1].replace(ch, '', 1)[::-1]
    return s
import unittest

class Test(unittest.TestCase):
    def test_remove_Occ(self):
        self.assertEqual(remove_Occ("hello", "l"), "heo")

if __name__ == '__main__':
    unittest.main()