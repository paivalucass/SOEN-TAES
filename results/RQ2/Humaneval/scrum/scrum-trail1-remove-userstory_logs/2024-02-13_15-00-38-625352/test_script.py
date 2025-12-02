from typing import List

def parse_music(music_string: str) -> List[int]:
    beats = []
    for note in music_string.split():
        if note == 'o':
            beats.append(4)
        elif note == 'o|':
            beats.append(2)
        elif note == '.|':
            beats.append(1)
    return beats
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(parse_music('o o| .| o| o| .| .| .| .| o o'), [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4])

if __name__ == '__main__':
    unittest.main()