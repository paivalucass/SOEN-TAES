from typing import List

def parse_music(music_string: str) -> List[int]:
    beats_mapping = {'o': 4, 'o|': 2, '.|': 1}
    beats = [beats_mapping.get(note, f"Error: Invalid note '{note}'") for note in music_string.split()]
    return [beat if isinstance(beat, int) else beat for beat in beats]
import unittest

from typing import List


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(parse_music('o o| .| o| o| .| .| .| .| o o'), [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4])


if __name__ == '__main__':
    unittest.main()