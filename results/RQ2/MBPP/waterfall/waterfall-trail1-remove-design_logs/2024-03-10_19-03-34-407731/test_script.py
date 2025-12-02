def remove_Occ(original_string, character):
    first_occurrence = original_string.find(character)
    last_occurrence = original_string.rfind(character)
    if first_occurrence != -1 and last_occurrence != -1:
        original_string = original_string[:first_occurrence] + original_string[first_occurrence+1:last_occurrence] + original_string[last_occurrence+1:]
    return original_string
import unittest

class Test(unittest.TestCase):
    def test_remove_Occ(self):
        self.assertEqual(remove_Occ("hello", "l"), "heo")

if __name__ == '__main__':
    unittest.main()