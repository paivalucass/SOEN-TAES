def word_len(s):
    if s is None:
        return "Error: Null input"
    elif len(s) == 0:
        return "Error: Empty input"
    elif not s.isalpha():
        return "Error: Special characters input"
    else:
        return len(s) % 2 != 0
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(word_len('Hadoop'), False)

if __name__ == '__main__':
    unittest.main()