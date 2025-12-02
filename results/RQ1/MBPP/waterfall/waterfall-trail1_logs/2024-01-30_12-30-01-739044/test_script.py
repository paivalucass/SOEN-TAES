def snake_to_camel(word: str) -> str:
    word_list = word.split('_')
    camel_case = word_list[0].capitalize() + ''.join([word.capitalize() for word in word_list[1:]])
    return camel_case

assert snake_to_camel('python_program')=='PythonProgram'
assert snake_to_camel('')=='' # additional test case
assert snake_to_camel('singleword')=='Singleword' # additional test case
assert snake_to_camel('special_characters_here')=='SpecialCharactersHere' # additional test case
assert snake_to_camel('multiple__underscores')=='MultipleUnderscores' # additional test case
assert snake_to_camel('_leading_underscores')=='LeadingUnderscores' # additional test case
assert snake_to_camel('trailing_underscores_')=='TrailingUnderscores' # additional test case
import unittest

class TestSnakeToCamel(unittest.TestCase):
    def test_snake_to_camel(self):
        self.assertEqual(snake_to_camel('python_program'), 'PythonProgram')

if __name__ == '__main__':
    unittest.main()