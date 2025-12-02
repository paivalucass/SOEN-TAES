def min_swaps(str1: str, str2: str) -> int:
    if not all(char in '01' for char in str1) or not all(char in '01' for char in str2):
        raise ValueError("Input strings must be valid binary numbers")

    if len(str1) != len(str2):
        raise ValueError("Input strings must have the same length")

    min_swaps_count = sum(1 for i in range(len(str1)) if str1[i] != str2[i])
    return min_swaps_count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(min_Swaps('1101', '1110'), 1)

if __name__ == '__main__':
    unittest.main()