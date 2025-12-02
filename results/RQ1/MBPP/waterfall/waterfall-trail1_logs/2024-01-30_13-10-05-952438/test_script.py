def snake_to_camel(word):
    if not word or len(word) == 0:
        raise ValueError("Input cannot be null or empty")

    words = word.split('_')
    camelCase = words[0].capitalize() + ''.join([w.capitalize() for w in words[1:]])

    return camelCase
import unittest

class TestSnakeToCamel(unittest.TestCase):
    def test_snake_to_camel(self):
        self.assertEqual(snake_to_camel('android_tv'), 'AndroidTv')

if __name__ == '__main__':
    unittest.main()