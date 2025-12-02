def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    def count_uppercase_vowels_even_indices(s):
        if len(s) == 0:
            return 0
        vowels = ['A', 'E', 'I', 'O', 'U']
        count = 0
        for i in range(0, len(s), 2):
            if s[i] in vowels:
                count += 1
        return count
    
    return count_uppercase_vowels_even_indices(s)
import unittest

class Test(unittest.TestCase):
    def test_count_upper(self):
        self.assertEqual(count_upper('aBCdEf'), 1)
        self.assertEqual(count_upper('abcdefg'), 0)
        self.assertEqual(count_upper('dBBE'), 0)

if __name__ == '__main__':
    unittest.main()