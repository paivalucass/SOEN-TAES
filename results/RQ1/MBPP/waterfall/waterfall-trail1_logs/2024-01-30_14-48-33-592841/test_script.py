def reverse_words(s):
    words = s.split()
    words = list(reversed(words))
    return ' '.join(words)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(reverse_words('python program'), 'program python')

if __name__ == '__main__':
    unittest.main()