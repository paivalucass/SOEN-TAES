def validate_input(word):
    if not word:
        return "Error: Invalid input"
    if "_" not in word:
        return "Error: Invalid input"
    if len(word) > 255:
        return "Error: Invalid input"
    if not word.islower():
        return "Error: Invalid input"
    if "__" in word:
        return "Error: Invalid input"
    if any(char in word for char in "@!#$%^&*()+=-[]{};:'\"<>,.?/"):
        return "Error: Invalid input"
    return None

def snake_to_camel(word):
    validation_result = validate_input(word)
    if validation_result:
        return validation_result
    
    words = word.split('_')
    camel_word = words[0].capitalize() + ''.join(w.capitalize() for w in words[1:])
    return camel_word
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(snake_to_camel('android_tv'), 'AndroidTv')

if __name__ == '__main__':
    unittest.main()