def count_vowels(test_str):
    count = 0
    vowels = 'aeiou'
    test_str = test_str.lower()
    for i in range(1, len(test_str) - 1):
        if test_str[i] in vowels and test_str[i - 1] in vowels:
            count += 1
        elif test_str[i] in vowels and test_str[i + 1] in vowels:
            count += 1
    return count

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_vowels('bestinstareels'), 7)

if __name__ == '__main__':
    unittest.main()