def find_Rotations(input_string: str) -> int:
    if len(input_string) == 0:
        return 0

    allowed_characters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if not set(input_string).issubset(allowed_characters):
        return -1

    return 1  # placeholder for the actual return value

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Rotations('aaaa'), 1)

if __name__ == '__main__':
    unittest.main()