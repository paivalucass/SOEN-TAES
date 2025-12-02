def min_Swaps(str1, str2):
    swap_count = 0
    for char1, char2 in zip(str1, str2):
        if char1 != char2:
            swap_count += 1
    return swap_count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(min_Swaps("1101", "1110"), 1)

if __name__ == '__main__':
    unittest.main()