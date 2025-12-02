def snake_to_camel(word):
    words = word.split('_')
    camel_case = ''.join([w.capitalize() for w in words])
    return camel_case
import unittest

class Test(unittest.TestCase):
    def test_snake_to_camel(self):
        self.assertEqual(snake_to_camel('android_tv'), 'AndroidTv')

if __name__ == '__main__':
    unittest.main()