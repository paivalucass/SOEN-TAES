def reverse_vowels(input_string: str) -> str:
    vowels = "aeiouAEIOU"
    input_list = list(input_string)
    i, j = 0, len(input_list) - 1

    while i < j:
        if input_list[i] in vowels and input_list[j] in vowels:
            input_list[i], input_list[j] = input_list[j], input_list[i]
            i += 1
            j -= 1
        elif input_list[i] not in vowels:
            i += 1
        elif input_list[j] not in vowels:
            j -= 1
    
    return "".join(input_list)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(reverse_vowels('Python'), 'Python')

if __name__ == '__main__':
    unittest.main()