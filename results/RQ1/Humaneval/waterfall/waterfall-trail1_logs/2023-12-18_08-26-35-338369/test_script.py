def get_closest_vowel(word):
    vowels = "aeiouAEIOU"
    
    closest_vowel_index = -1
    min_distance = float('inf')
    
    for i in range(len(word)-2, 0, -1):
        if word[i] in vowels:
            distance = len(word) - i - 1
            if distance < min_distance:
                closest_vowel_index = i
                min_distance = distance
    
    if closest_vowel_index == -1:
        return ""
    else:
        return word[closest_vowel_index]

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_closest_vowel('yogurt'), 'u')
        self.assertEqual(get_closest_vowel('FULL'), 'U')
        self.assertEqual(get_closest_vowel('quick'), '')
        self.assertEqual(get_closest_vowel('ab'), '')

if __name__ == '__main__':
    unittest.main()