def count_upper(s):
    if not isinstance(s, str):
        raise TypeError("Input should be a string")
    
    count = 0
    for i in range(0, len(s), 2):
        if s[i].isupper() and s[i] in ['A', 'E', 'I', 'O', 'U']:
            count += 1
    
    return count
import unittest

class Test(unittest.TestCase):
    def test_count_upper(self):
        self.assertEqual(count_upper('aBCdEf'), 1)
        self.assertEqual(count_upper('abcdefg'), 0)
        self.assertEqual(count_upper('dBBE'), 0)

if __name__ == '__main__':
    unittest.main()