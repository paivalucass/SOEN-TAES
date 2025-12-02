def remove_Occ(s, ch):
    first_occurrence = s.find(ch)
    last_occurrence = s.rfind(ch)
    if first_occurrence != -1 and last_occurrence != -1:
        s = s[:first_occurrence] + s[first_occurrence+1:last_occurrence] + s[last_occurrence+1:]
    return s
import unittest

class Test(unittest.TestCase):
    def test_remove_Occ(self):
        self.assertEqual(remove_Occ("hello", "l"), "heo")

if __name__ == '__main__':
    unittest.main()