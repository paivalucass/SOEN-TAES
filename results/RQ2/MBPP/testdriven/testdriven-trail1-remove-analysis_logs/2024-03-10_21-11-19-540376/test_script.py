def reverse_vowels(str1):
    vowels = set('aeiouAEIOU')
    str_list = list(str1)
    i, j = 0, len(str_list) - 1
    while i < j:
        if str_list[i] in vowels and str_list[j] in vowels:
            str_list[i], str_list[j] = str_list[j], str_list[i]
            i += 1
            j -= 1
        elif str_list[i] in vowels:
            j -= 1
        elif str_list[j] in vowels:
            i += 1
        else:
            i += 1
            j -= 1
    return ''.join(str_list)

# Test Case
assert reverse_vowels("Python") == "Python"
import unittest

class Test(unittest.TestCase):
    def test_reverse_vowels(self):
        self.assertEqual(reverse_vowels('Python'), 'Python')
        self.assertEqual(reverse_vowels('hello'), 'holle')
        self.assertEqual(reverse_vowels('apple'), 'eppla')

if __name__ == '__main__':
    unittest.main()