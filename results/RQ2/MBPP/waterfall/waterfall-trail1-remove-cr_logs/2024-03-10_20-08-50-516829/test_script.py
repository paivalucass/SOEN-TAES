def split(word):
    if word is None:
        return "Error: Input is null"
    elif not isinstance(word, str):
        return "Error: Input is not a string"
    elif len(word) > 100:
        return "Error: Input string is too long"
    elif not word.isalpha():
        return "Error: Input contains non-alphabetic characters"
    
    return list(word)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(split('python'), ['p','y','t','h','o','n'])

if __name__ == '__main__':
    unittest.main()