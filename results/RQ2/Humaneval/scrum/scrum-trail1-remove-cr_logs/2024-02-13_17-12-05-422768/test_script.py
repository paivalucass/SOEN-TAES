def get_closest_vowel(word):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    
    if len(word) < 3:
        return ""
    
    for i in range(len(word)-3, -1, -1):
        if word[i] in consonants and word[i+1] in vowels and word[i+2] in consonants:
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