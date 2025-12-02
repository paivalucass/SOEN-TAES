def reverse_words(s):
    if not s or not isinstance(s, str):
        raise ValueError("Invalid input")

    words = s.split()
    reversed_words = " ".join(reversed(words))

    return reversed_words
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(reverse_words('python program'), 'program python')

if __name__ == '__main__':
    unittest.main()