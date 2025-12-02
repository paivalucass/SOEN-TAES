from typing import List

def parse_music(music_string: str) -> List[int]:
    durations = {'o': 4, 'o|': 2, '.|': 1}
    notes = music_string.split()
    result = [durations[note] for note in notes]
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(parse_music('o o| .| o| o| .| .| .| .| o o'), [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4])

if __name__ == '__main__':
    unittest.main()