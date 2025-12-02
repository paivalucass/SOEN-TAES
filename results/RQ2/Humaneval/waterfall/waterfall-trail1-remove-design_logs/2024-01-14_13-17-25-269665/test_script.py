def get_closest_vowel(word):
    vowels = "aeiouAEIOU"
    if not any(char in vowels for char in word[1:-1]):
        return ""
    
    for i in range(len(word) - 3, 0, -1):
        if word[i] in vowels:
            return word[i]

    return ""
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_closest_vowel('yogurt'), 'u')
        self.assertEqual(get_closest_vowel('FULL'), 'U')
        self.assertEqual(get_closest_vowel('quick'), '')
        self.assertEqual(get_closest_vowel('ab'), '')

if __name__ == '__main__':
    unittest.main()