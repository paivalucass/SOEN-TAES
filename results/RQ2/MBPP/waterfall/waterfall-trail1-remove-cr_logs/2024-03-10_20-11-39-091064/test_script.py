def reverse_words(s):
    if not s:
        return ""

    words = s.split()

    reversed_words = words[::-1]

    return ' '.join(reversed_words)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(reverse_words('python program'), 'program python')

if __name__ == '__main__':
    unittest.main()