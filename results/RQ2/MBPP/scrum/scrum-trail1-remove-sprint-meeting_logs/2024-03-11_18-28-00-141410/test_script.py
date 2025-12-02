def replace_blank(str1, char):
    if str1 == "" or char == "":
        return "Invalid input"
    else:
        str1 = " ".join(str1.split())
        str1 = str1.replace(" ", char)
        return str1
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(replace_blank('hello people', '@'), 'hello@people')

if __name__ == '__main__':
    unittest.main()