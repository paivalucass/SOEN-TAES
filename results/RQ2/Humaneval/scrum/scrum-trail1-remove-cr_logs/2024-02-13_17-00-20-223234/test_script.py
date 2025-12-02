def vowels_count(s):
    count = 0
    vowels = "aeiouy"
    s = s.lower()
    for char in s:
        if char in vowels:
            if char == "y" and s.index(char) != len(s)-1:
                continue
            count += 1
    return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(vowels_count('abcde'), 2)
        self.assertEqual(vowels_count('ACEDY'), 3)
        self.assertEqual(vowels_count('hello'), 2)
        self.assertEqual(vowels_count('python'), 1)

if __name__ == '__main__':
    unittest.main()