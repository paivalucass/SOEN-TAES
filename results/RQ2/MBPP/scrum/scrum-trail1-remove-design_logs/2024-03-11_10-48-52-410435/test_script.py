def split(word):
    if not isinstance(word, str) or word == "":
        return "Error: Input must be a non-empty string"
    else:
        return list(word)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(split('python'), ['p','y','t','h','o','n'])

if __name__ == '__main__':
    unittest.main()