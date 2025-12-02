def remove_Occ(s, ch):
    if len(s) == 0 or ch not in s:
        return "Invalid input"
    
    first_occurrence = s.find(ch)
    last_occurrence = s.rfind(ch)
    
    if first_occurrence == last_occurrence:
        return s
    
    result = s[:first_occurrence] + s[first_occurrence+1:last_occurrence] + s[last_occurrence+1:]
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_Occ("hello", "l"), "heo")

if __name__ == '__main__':
    unittest.main()