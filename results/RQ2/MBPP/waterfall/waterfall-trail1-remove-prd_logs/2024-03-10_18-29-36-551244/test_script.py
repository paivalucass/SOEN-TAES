def reverse_vowels(str1):
    vowels = set('aeiouAEIOU')
    vowel_list = [char for char in str1 if char in vowels]
    if len(vowel_list) == 0:
        return str1
    else:
        vowel_list.reverse()
        result = ''
        idx = 0
        for char in str1:
            if char in vowels:
                result += vowel_list[idx]
                idx += 1
            else:
                result += char
        return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(reverse_vowels('Python'), 'Python')

if __name__ == '__main__':
    unittest.main()