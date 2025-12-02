def replace_blank(str1, char):
    modified_string = ""
    prev_char = ''
    for i in range(len(str1)):
        if str1[i] == ' ' and prev_char == ' ':
            continue
        elif str1[i] == ' ':
            modified_string += char
        else:
            modified_string += str1[i]
        prev_char = str1[i]
    return modified_string
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(replace_blank('hello people', '@'), 'hello@people')

if __name__ == '__main__':
    unittest.main()