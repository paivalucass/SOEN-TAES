from typing import List

# A dictionary mapping note strings to their respective durations
note_durations = {
    'o': 4,
    'o|': 2,
    '.|': 1
}

def parse_music(music_string: str) -> List[int]:
    try:
        notes = music_string.split()
        durations = [note_durations[note] for note in notes]
        return durations
    except KeyError:
        raise ValueError("Invalid note found in the input string.")
    except Exception as e:
        raise Exception("An error occurred while parsing the music string.")

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(parse_music('o o| .| o| o| .| .| .| .| o o'), [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4])

if __name__ == '__main__':
    unittest.main()