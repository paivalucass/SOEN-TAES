def snake_to_camel(word):
    if '_' in word:
        word_list = word.split('_')
        camel_case_string = word_list[0] + ''.join(x.title() for x in word_list[1:])
    else:
        camel_case_string = word.title()

    return camel_case_string.capitalize()
import unittest

class TestSnakeToCamel(unittest.TestCase):
    def test_snake_to_camel(self):
        self.assertEqual(snake_to_camel('android_tv'), 'AndroidTv')

if __name__ == '__main__':
    unittest.main()