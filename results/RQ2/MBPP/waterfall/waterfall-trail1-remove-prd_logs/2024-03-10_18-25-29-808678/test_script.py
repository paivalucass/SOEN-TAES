def remove_Occ(input_string, character):
    if input_string is None or len(input_string) == 0:
        return "Error: Input string is null or empty"

    if character not in input_string:
        return "Error: Character not found in input string"

    first_occurrence = input_string.find(character)
    last_occurrence = input_string.rfind(character)
    
    if first_occurrence != -1 and last_occurrence != -1:
        modified_string = input_string[:first_occurrence] + input_string[first_occurrence+1:last_occurrence] + input_string[last_occurrence+1:]
        return modified_string

    return input_string

# Test Cases:
assert remove_Occ("hello", "l") == "heo"
assert remove_Occ("hello", "x") == "Error: Character not found in input string"
assert remove_Occ("", "x") == "Error: Input string is null or empty"
import unittest

class Test(unittest.TestCase):
    def test_remove_occ(self):
        self.assertEqual(remove_Occ("hello", "l"), "heo")

if __name__ == '__main__':
    unittest.main()