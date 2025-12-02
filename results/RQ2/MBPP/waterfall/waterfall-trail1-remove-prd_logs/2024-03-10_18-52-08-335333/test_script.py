def min_swaps(str1, str2):
    if len(str1) != len(str2):
        return "Invalid input"
    swaps = sum(1 for char1, char2 in zip(str1, str2) if char1 != char2)
    return swaps
import unittest

class Test(unittest.TestCase):
    def test_min_Swaps(self):
        self.assertEqual(min_Swaps("1101", "1110"), 1)

if __name__ == '__main__':
    unittest.main()