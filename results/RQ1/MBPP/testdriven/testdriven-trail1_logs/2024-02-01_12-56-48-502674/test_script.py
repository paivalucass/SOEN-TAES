def split(word):
    if not word.isalpha() or len(word) == 0:
        return "Invalid input"

    return list(word)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(split('python'), ['p','y','t','h','o','n'])

if __name__ == '__main__':
    unittest.main()