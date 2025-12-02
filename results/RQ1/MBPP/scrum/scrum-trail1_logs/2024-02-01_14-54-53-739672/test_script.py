def replace_blank(str1, char):
    if not str1:
        return str1
    else:
        return str1.replace(' ', char)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(replace_blank('hello people', '@'), 'hello@people')

if __name__ == '__main__':
    unittest.main()