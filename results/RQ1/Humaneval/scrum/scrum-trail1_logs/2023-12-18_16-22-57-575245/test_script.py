def count_upper(s):
    count = 0
    vowels = "AEIOUaeiou"
    for i in range(0, len(s), 2):
        if s[i] in vowels and s[i].isupper():
            count += 1
    return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_upper('aBCdEf'), 1)
        self.assertEqual(count_upper('abcdefg'), 0)
        self.assertEqual(count_upper('dBBE'), 0)

if __name__ == '__main__':
    unittest.main()