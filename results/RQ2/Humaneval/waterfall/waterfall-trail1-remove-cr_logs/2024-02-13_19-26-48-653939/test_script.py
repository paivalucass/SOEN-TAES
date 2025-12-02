def get_closest_vowel(word):
    vowels = "AEIOUaeiou"
    consonants = "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"
    for i in range(len(word) - 3, 0, -1):
        if word[i] in consonants and word[i-1] in vowels and word[i-2] in consonants:
            return word[i-1]
    return ""
import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(get_closest_vowel('yogurt'), 'u')
    
    def test2(self):
        self.assertEqual(get_closest_vowel('FULL'), 'U')
    
    def test3(self):
        self.assertEqual(get_closest_vowel('quick'), '')
    
    def test4(self):
        self.assertEqual(get_closest_vowel('ab'), '')

if __name__ == '__main__':
    unittest.main()