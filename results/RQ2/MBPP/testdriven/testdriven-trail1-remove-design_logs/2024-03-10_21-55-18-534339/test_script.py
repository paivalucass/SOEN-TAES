def remove_Occ(s, ch):
    if s.count(ch) < 2:
        return s.replace(ch, '')
    else:
        first_index = s.find(ch)
        last_index = s.rfind(ch)
        return s[:first_index] + s[first_index+1:last_index] + s[last_index+1:]
import unittest

class Test(unittest.TestCase):
    def test_remove_Occ(self):
        self.assertEqual(remove_Occ("hello", "l"), "heo")

if __name__ == '__main__':
    unittest.main()