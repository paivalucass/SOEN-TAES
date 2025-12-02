def get_closest_vowel(word):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    for i in range(len(word) - 2, 0, -1):
        if word[i] in consonants and word[i+1] in vowels:
            return word[i+1]
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