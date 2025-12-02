def min_swaps(str1, str2):
    def is_valid_input(s):
        return len(s) == 0 or (len(s) % 2 == 0 and all(c in '01' for c in s))
    
    def count_swaps(s1, s2):
        return sum(c1 != c2 for c1, c2 in zip(s1, s2))
    
    if not is_valid_input(str1) or not is_valid_input(str2):
        return 'Invalid input'
    
    return count_swaps(str1, str2)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(min_Swaps("1101", "1110"), 1)

if __name__ == '__main__':
    unittest.main()