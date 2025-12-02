def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    if not s:
        raise ValueError("Input string cannot be empty")
    
    vowels = set('AEIOU')
    count = sum(1 for i in range(0, len(s), 2) if s[i] in vowels)
    
    return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_upper('aBCdEf'), 1)
        self.assertEqual(count_upper('abcdefg'), 0)
        self.assertEqual(count_upper('dBBE'), 0)

if __name__ == '__main__':
    unittest.main()