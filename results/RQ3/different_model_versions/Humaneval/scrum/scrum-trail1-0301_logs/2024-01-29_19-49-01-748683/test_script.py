from typing import List


def parse_music(music_string: str) -> List[int]:
    if not isinstance(music_string, str):
        raise TypeError("The input argument must be a string.")

    note_duration_dict = {'o': 4, 'o|': 2, '.|': 1}
    note_durations = [note_duration_dict[note] for note in music_string.split()]
    
    return note_durations

# Test Cases:
{
"requirement analysis":"Test the parse_music function with various input data and edge cases to ensure it correctly parses the musical notes and returns the expected output.",
"test_cases":[
{"Test Title":"Test empty string input","Input Data":"","Expected Output":[]},
{"Test Title":"Test valid input with one whole note","Input Data":"'o'","Expected Output":[4]},
{"Test Title":"Test valid input with one half note","Input Data":"'o|'","Expected Output":[2]},
{"Test Title":"Test valid input with one quarter note","Input Data":"'.'","Expected Output":[1]},
{"Test Title":"Test valid input with multiple notes","Input Data":"'o o| .| o| o| .| .| .| .| o o'","Expected Output":[4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]},
{"Test Title":"Test invalid input with invalid note","Input Data":"'x'","Expected Output":"ValueError: Invalid note in input string."},
{"Test Title":"Test invalid input with invalid format","Input Data":"'o o o'","Expected Output":"ValueError: Invalid input format."}
]
}
import unittest
from typing import List

class Test(unittest.TestCase):
    def test_parse_music(self):
        self.assertEqual(parse_music('o o| .| o| o| .| .| .| .| o o'), [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4])
        self.assertEqual(parse_music('o o| o|'), [4, 2, 2])
        self.assertEqual(parse_music('o .| o| .|'), [4, 1, 2, 1])

if __name__ == '__main__':
    unittest.main()