def snake_to_camel(word):
    if not isinstance(word, str):
        raise ValueError("Input word must be a valid string")

    if not word:
        return ""

    if "_" not in word:
        return word

    words = word.split("_")
    camel_case_word = words[0] + ''.join(word.title() for word in words[1:])
    return camel_case_word

import unittest

class Test(unittest.TestCase):
    def test_snake_to_camel(self):
        self.assertEqual(snake_to_camel('python_program'), 'PythonProgram')

if __name__ == '__main__':
    unittest.main()