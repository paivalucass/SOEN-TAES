def reverse_vowels(str1):
    vowels = "aeiouAEIOU"
    str_list = list(str1)
    left, right = 0, len(str_list) - 1
    while left < right:
        while str_list[left] not in vowels and left < right:
            left += 1
        while str_list[right] not in vowels and left < right:
            right -= 1
        str_list[left], str_list[right] = str_list[right], str_list[left]
        left += 1
        right -= 1
    return ''.join(str_list)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(reverse_vowels('Python'), 'Python')

if __name__ == '__main__':
    unittest.main()