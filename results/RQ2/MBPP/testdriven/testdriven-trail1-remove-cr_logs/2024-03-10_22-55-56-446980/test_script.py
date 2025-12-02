def min_swaps(str1, str2):
    if len(str1) != len(str2):
        return 'Error: Input binary numbers are of unequal length'
    
    swap_count = 0
    for char1, char2 in zip(str1, str2):
        if char1 != char2:
            swap_count += 1
    
    return swap_count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(min_Swaps('1101', '1110'), 1)

if __name__ == '__main__':
    unittest.main()