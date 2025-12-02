def reverse_vowels(str1):
    vowels = "aeiouAEIOU"
    str_list = list(str1)
    left = 0
    right = len(str_list) - 1
    while left < right:
        if str_list[left] not in vowels:
            left += 1
        elif str_list[right] not in vowels:
            right -= 1
        else:
            str_list[left], str_list[right] = str_list[right], str_list[left]
            left += 1
            right -= 1
    return ''.join(str_list)
import unittest

class Test(unittest.TestCase):
    def test_reverse_vowels(self):
        self.assertEqual(reverse_vowels('Python'), 'Python')

if __name__ == '__main__':
    unittest.main()