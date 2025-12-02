def snake_to_camel(word):
    if not word:
        return "Error: Empty input"
    
    if not isinstance(word, str):
        return "Error: Invalid input"
    
    import re
    if not re.match("^[a-zA-Z_]*$", word):
        return "Error: Invalid input"
    
    if len(word) > 1000:
        return "Error: Maximum input length exceeded"
    
    words = word.split('_')
    camel_case = words[0] + ''.join(word.title() for word in words[1:])
    return camel_case.capitalize()
import unittest

class TestSnakeToCamel(unittest.TestCase):
    def test_snake_to_camel(self):
        self.assertEqual(snake_to_camel('android_tv'), 'AndroidTv')

if __name__ == '__main__':
    unittest.main()