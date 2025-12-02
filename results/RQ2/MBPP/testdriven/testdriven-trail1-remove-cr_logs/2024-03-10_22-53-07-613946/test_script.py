def count_vowels(test_str):
    if not test_str or len(test_str) < 3:
        return 0
    
    vowels = "aeiouAEIOU"
    count = 0
    for i in range(len(test_str)):
        if i > 0 and i < len(test_str) - 1 and test_str[i] in vowels and (test_str[i-1] in vowels or test_str[i+1] in vowels):
            count += 1
    return count
import unittest

class Test(unittest.TestCase):
    def test_count_vowels(self):
        self.assertEqual(count_vowels('bestinstareels'), 7)

if __name__ == '__main__':
    unittest.main()