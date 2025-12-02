def count_vowels(test_str):
    count = 0
    vowels = "aeiou"
    for i in range(len(test_str)):
        if test_str[i] in vowels and ((i > 0 and test_str[i-1] in vowels) or (i < len(test_str)-1 and test_str[i+1] in vowels)):
            count += 1
    return count
import unittest

class Test(unittest.TestCase):
    def test_count_vowels(self):
        self.assertEqual(count_vowels('bestinstareels'), 7)

if __name__ == '__main__':
    unittest.main()