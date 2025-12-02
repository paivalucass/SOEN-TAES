def vowels_count(s):
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    count = 0
    for char in s:
        if char.lower() in vowels:
            count += 1
    if s[-1].lower() == 'y':
        count -= 1
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