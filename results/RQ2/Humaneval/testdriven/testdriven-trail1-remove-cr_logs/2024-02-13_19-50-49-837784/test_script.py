def get_closest_vowel(word):
    vowels = 'aeiouAEIOU'
    for i in range(len(word)-2, 0, -1):
        if word[i] in vowels and word[i-1] not in vowels and word[i+1] not in vowels:
            return word[i]
    return ''
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