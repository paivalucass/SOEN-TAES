def vowels_count(s):
    vowels = 'aeiouy'
    count = 0
    for char in s.lower():
        if char in vowels:
            count += 1
    return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(vowels_count('abcde'), 2)
        self.assertEqual(vowels_count('ACEDY'), 3)
        # Add more test cases
        self.assertEqual(vowels_count('hello'), 2)
        self.assertEqual(vowels_count('python'), 2)
        self.assertEqual(vowels_count('elephant'), 3)

if __name__ == '__main__':
    unittest.main()