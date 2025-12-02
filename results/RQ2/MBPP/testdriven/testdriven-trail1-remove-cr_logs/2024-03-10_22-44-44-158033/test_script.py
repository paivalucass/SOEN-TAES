def split(word):
    if not word:
        raise ValueError("Input string must not be empty")
    
    if not isinstance(word, str):
        raise TypeError("Input must be a string")

    return list(word)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(split('python'), ['p','y','t','h','o','n'])

if __name__ == '__main__':
    unittest.main()