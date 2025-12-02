def snake_to_camel(word):
    if word is None:
        return "Error: Input is null"
    if not isinstance(word, str):
        return "Error: Input is not a string"
    
    if '_' not in word:
        return word.capitalize()
    
    words_list = word.split('_')
    camel_word = words_list[0].capitalize()
    for w in words_list[1:]:
        camel_word += w.capitalize()
    return camel_word
import unittest

class Test(unittest.TestCase):
    def test_snake_to_camel(self):
        self.assertEqual(snake_to_camel('android_tv'), 'AndroidTv')

if __name__ == '__main__':
    unittest.main()