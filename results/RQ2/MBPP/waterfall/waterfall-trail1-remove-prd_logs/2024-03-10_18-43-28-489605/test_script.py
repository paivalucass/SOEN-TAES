def reverse_words(s):
    if not s:
        return ""
    words = s.split()
    if not words:
        return "Input string contains no words"
    reversed_words = " ".join(reversed(words))
    return reversed_words
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(reverse_words('python program'), 'program python')

if __name__ == '__main__':
    unittest.main()