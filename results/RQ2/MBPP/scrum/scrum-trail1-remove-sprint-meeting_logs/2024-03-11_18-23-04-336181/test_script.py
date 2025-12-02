def reverse_vowels(str1):
    vowels = "aeiouAEIOU"
    str_list = list(str1)
    i, j = 0, len(str_list) - 1
    while i < j:
        if str_list[i] not in vowels:
            i += 1
        elif str_list[j] not in vowels:
            j -= 1
        else:
            str_list[i], str_list[j] = str_list[j], str_list[i]
            i += 1
            j -= 1
    return "".join(str_list)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(reverse_vowels('Python'), 'Python')

if __name__ == '__main__':
    unittest.main()