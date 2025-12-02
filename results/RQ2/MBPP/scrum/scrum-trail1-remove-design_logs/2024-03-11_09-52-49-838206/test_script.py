def remove_Occ(s, ch):
    if s == "" or ch not in s:
        return "Invalid input"

    first_occurrence = s.find(ch)
    last_occurrence = s.rfind(ch)

    if first_occurrence != -1 and last_occurrence != -1:
        new_string = s[:first_occurrence] + s[first_occurrence+1:last_occurrence] + s[last_occurrence+1:]
        return new_string
    else:
        return "Character not found in the string"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_Occ("hello", "l"), "heo")

if __name__ == '__main__':
    unittest.main()