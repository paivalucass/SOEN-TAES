def capital_words_spaces(input_string):
    modified_string = ""
    for i in range(len(input_string)):
        if i > 0 and input_string[i].isupper() and not input_string[i-1].isspace():
            modified_string += " "
        modified_string += input_string[i]
    return modified_string
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(capital_words_spaces('Python'), 'Python')

if __name__ == '__main__':
    unittest.main()