from typing import List

notes_duration = {
    'o': 4,
    'o|': 2,
    '.|': 1
}

def parse_music(music_string: str) -> List[int]:
    parsed_notes = []
    for note in music_string.split():
        parsed_notes.append(notes_duration.get(note, 0))
    
    return parsed_notes
import unittest

class Test(unittest.TestCase):
    def test_parse_music(self):
        self.assertEqual(parse_music('o o| .| o| o| .| .| .| .| o o'), [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4])

if __name__ == '__main__':
    unittest.main()