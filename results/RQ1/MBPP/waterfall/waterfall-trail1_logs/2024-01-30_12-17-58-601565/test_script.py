def remove_Occ(input_string, character):
    if input_string == "" or character not in input_string:
        return "Invalid input"

    first_occurrence = input_string.find(character)
    last_occurrence = input_string.rfind(character)

    modified_string = input_string[:first_occurrence] + input_string[first_occurrence+1:last_occurrence] + input_string[last_occurrence+1:]
    return modified_string
import unittest

class Test(unittest.TestCase):
    def test_remove_occ(self):
        self.assertEqual(remove_Occ("hello", "l"), "heo")

if __name__ == '__main__':
    unittest.main()