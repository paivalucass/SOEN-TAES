def find_Rotations(input_str: str) -> int:
    min_rotations = len(input_str)
    for i in range(1, len(input_str)):
        rotated_str = input_str[i:] + input_str[:i]
        if rotated_str == input_str:
            min_rotations = i
            break
    return min_rotations
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Rotations('aaaa'), 1)

if __name__ == '__main__':
    unittest.main()