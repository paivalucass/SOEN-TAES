def snake_to_camel(word):
    words = word.split('_')
    return words[0].capitalize() + ''.join(x.capitalize() or x for x in words[1:])
import unittest

class Test(unittest.TestCase):
    def test_snake_to_camel(self):
        self.assertEqual(snake_to_camel('android_tv'), 'AndroidTv')

if __name__ == '__main__':
    unittest.main()