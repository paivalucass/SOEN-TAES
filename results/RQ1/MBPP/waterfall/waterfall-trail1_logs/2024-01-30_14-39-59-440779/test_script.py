def split(word):
    if not isinstance(word, str) or not word:
        return "Error: Empty input string"

    characters = list(word)

    return characters
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(split('python'), ['p','y','t','h','o','n'])

if __name__ == '__main__':
    unittest.main()