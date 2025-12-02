def reverse_words(s):
    if s is None or len(s.strip()) == 0:
        return ""

    words = s.split()
    reversed_words = ' '.join(reversed(words))
    return reversed_words
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(reverse_words('python program'), 'program python')

if __name__ == '__main__':
    unittest.main()