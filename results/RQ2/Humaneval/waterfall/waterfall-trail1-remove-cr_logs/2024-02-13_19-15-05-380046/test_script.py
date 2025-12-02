from typing import List

def parse_music(music_string: str) -> List[int]:
    music_dict = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    result = []
    
    notes = music_string.split()
    for note in notes:
        if note in music_dict:
            result.append(music_dict[note])
        else:
            raise ValueError("Error: Invalid note format")
    
    return result
import unittest

class Test(unittest.TestCase):
    def test_parse_music(self):
        self.assertEqual(parse_music('o o| .| o| o| .| .| .| .| o o'), [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4])

if __name__ == '__main__':
    unittest.main()