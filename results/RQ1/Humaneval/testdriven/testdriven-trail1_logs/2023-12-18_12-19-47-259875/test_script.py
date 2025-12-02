from typing import List

def parse_music(music_string: str) -> List[int]:
    valid_notes = set(['o', 'o|', '.|'])
    if not set(music_string.split()) <= valid_notes:
        raise ValueError("Invalid input: music_string contains characters other than 'o', 'o|', and '.|'")

    beats_mapping = {'o': 4, 'o|': 2, '.|': 1}
    parsed_beats = [beats_mapping[note] for note in music_string.split()]
    return parsed_beats
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(parse_music('o o| .| o| o| .| .| .| .| o o'), [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4])

if __name__ == '__main__':
    unittest.main()