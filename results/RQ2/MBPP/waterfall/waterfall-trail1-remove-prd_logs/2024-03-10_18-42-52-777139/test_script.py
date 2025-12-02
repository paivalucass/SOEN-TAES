def min_swaps(str1, str2):
    if len(str1) != len(str2):
        return "Error: Input strings must have the same length"
    
    if not all(c in {'0', '1'} for c in str1) or not all(c in {'0', '1'} for c in str2):
        return "Error: Input strings can only contain binary characters"
    
    diff_count = sum(1 for i in range(len(str1)) if str1[i] != str2[i])
    return diff_count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(min_Swaps("1101", "1110"), 1)

if __name__ == '__main__':
    unittest.main()