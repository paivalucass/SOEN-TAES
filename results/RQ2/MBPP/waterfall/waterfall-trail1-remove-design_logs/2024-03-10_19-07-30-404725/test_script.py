def reverse_vowels(input_string):
    vowels = "aeiouAEIOU"
    string_list = list(input_string)
    i, j = 0, len(string_list) - 1
    while i < j:
        if string_list[i] not in vowels:
            i += 1
            continue
        if string_list[j] not in vowels:
            j -= 1
            continue
        string_list[i], string_list[j] = string_list[j], string_list[i]
        i += 1
        j -= 1
    return ''.join(string_list)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(reverse_vowels('Python'), 'Python')

if __name__ == '__main__':
    unittest.main()