def min_swaps(str1, str2):
    if len(str1) != len(str2):
        raise ValueError("Input strings must be of the same length")
    
    count = sum(1 for s1, s2 in zip(str1, str2) if s1 != s2)
    return count

assert min_swaps("1101", "1110") == 1
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(min_Swaps("1101", "1110"), 1)

if __name__ == '__main__':
    unittest.main()