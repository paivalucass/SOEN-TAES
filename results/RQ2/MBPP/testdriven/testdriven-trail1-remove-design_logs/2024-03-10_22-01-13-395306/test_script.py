def replace_blank(str1, char):
    if not str1 or len(char) != 1:
        return "Invalid input"

    return char.join(str1.split())
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(replace_blank('hello people', '@'), 'hello@people')

if __name__ == '__main__':
    unittest.main()