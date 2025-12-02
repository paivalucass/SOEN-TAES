def snake_to_camel(word):
    return ''.join(x.capitalize() or '_' for x in word.split('_'))
    
# Test Cases:
assert snake_to_camel('android_tv') == 'AndroidTv'
import unittest

class TestSnakeToCamel(unittest.TestCase):
    def test_snake_to_camel(self):
        self.assertEqual(snake_to_camel('android_tv'), 'AndroidTv')

if __name__ == '__main__':
    unittest.main()