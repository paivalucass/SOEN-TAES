def count_upper(s):
    def is_uppercase_vowel(char):
        vowels = ['A', 'E', 'I', 'O', 'U']
        return char in vowels

    def count_upper_efficient(s):
        if not isinstance(s, str):
            raise TypeError("Input must be a valid string")
        count = 0
        for i, char in enumerate(s):
            if i % 2 == 0 and is_uppercase_vowel(char):
                count += 1
        return count

    return count_upper_efficient(s)
import unittest

class Test(unittest.TestCase):
    def test_count_upper(self):
        self.assertEqual(count_upper('aBCdEf'), 1)
        self.assertEqual(count_upper('abcdefg'), 0)
        self.assertEqual(count_upper('dBBE'), 0)

if __name__ == '__main__':
    unittest.main()