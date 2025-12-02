from typing import List

def parse_music(music_string: str) -> List[int]:
    if not music_string:
        raise ValueError("Input music_string is empty")

    duration_list = []

    note_list = music_string.split()

    for note in note_list:
        if note == 'o':
            duration_list.append(4)
        elif note == 'o|':
            duration_list.append(2)
        elif note == '.|':
            duration_list.append(1)
        else:
            raise ValueError("Invalid note format: " + note)

    return duration_list
import unittest

class Test(unittest.TestCase):
    def test_parse_music(self):
        self.assertEqual(parse_music('o o| .| o| o| .| .| .| .| o o'), [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4])

if __name__ == '__main__':
    unittest.main()