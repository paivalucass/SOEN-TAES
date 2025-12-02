def reverse_words(s):
    if s is None:
        return "Error: Null input"
    elif s == "":
        return ""
    elif len(s) > 255:
        return "Error: Exceeds maximum input length"
    else:
        words = s.split()
        reversed_string = ' '.join(words[::-1])
        return reversed_string
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(reverse_words('python program'), 'program python')

if __name__ == '__main__':
    unittest.main()