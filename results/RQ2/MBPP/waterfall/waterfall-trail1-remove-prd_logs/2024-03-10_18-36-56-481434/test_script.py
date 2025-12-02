def snake_to_camel(word):
    if not word or word.count("_") == len(word) or word.startswith("_") or word.endswith("_"):
        return "Error: Input string is empty or contains only underscores, or starts/ends with an underscore"

    words = word.split('_')
    camel_case = ''.join([words[0].capitalize()] + [x.capitalize() for x in words[1:]])
    return camel_case
import unittest

class Test(unittest.TestCase):
    def test_snake_to_camel(self):
        self.assertEqual(snake_to_camel('android_tv'), 'AndroidTv')

if __name__ == '__main__':
    unittest.main()