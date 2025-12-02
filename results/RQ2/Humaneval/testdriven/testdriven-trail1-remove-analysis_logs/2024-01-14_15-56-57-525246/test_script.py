def get_closest_vowel(word):
    """
    You are given a word. Your task is to find the closest vowel that stands between 
    two consonants from the right side of the word (case sensitive).
    
    Vowels in the beginning and ending doesn't count. Return empty string if you didn't
    find any vowel met the above condition. 

    You may assume that the given string contains English letter only.

    Example:
    get_closest_vowel("yogurt") ==> "u"
    get_closest_vowel("FULL") ==> "U"
    get_closest_vowel("quick") ==> ""
    get_closest_vowel("ab") ==> ""
    """

    # Find the closest vowel between two consonants from the right side of the word
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    word = word.strip()

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