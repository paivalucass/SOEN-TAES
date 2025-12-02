def remove_Occ(s, ch):
    if s == "" or ch == "":
        return "Input string and character to remove cannot be empty"
    
    s = s.lower()
    ch = ch.lower()
    
    first_occurrence = s.find(ch)
    last_occurrence = s.rfind(ch)
    
    modified_string = s[:first_occurrence] + s[first_occurrence+1:last_occurrence] + s[last_occurrence+1:]
    
    return modified_string
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_Occ('hello', 'l'), 'heo')

if __name__ == '__main__':
    unittest.main()