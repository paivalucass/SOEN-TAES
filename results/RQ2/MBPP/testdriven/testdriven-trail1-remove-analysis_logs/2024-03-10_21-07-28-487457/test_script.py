def remove_Occ(s, ch):
    if ch not in s:
        return s
    else:
        first_occ = s.find(ch)
        last_occ = s.rfind(ch)
        if first_occ == last_occ:
            return s.replace(ch, "")
        else:
            new_str = s[:first_occ] + s[first_occ+1:last_occ] + s[last_occ+1:]
            return new_str
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_Occ('hello', 'l'), 'heo')

if __name__ == '__main__':
    unittest.main()