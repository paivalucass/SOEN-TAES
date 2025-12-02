def split(word):
    if not isinstance(word, str):
        raise ValueError("Input must be a string")

    if len(word) == 0:
        raise ValueError("Input string cannot be empty")

    return list(word)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(split('python'), ['p','y','t','h','o','n'])

if __name__ == '__main__':
    unittest.main()