def ascii_value(k):
    if len(k) != 1:
        return "Input is empty"
    if not k.isalpha():
        return "Input is not a valid alphabetic character"
    return ord(k)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(ascii_value('A'), 65)

if __name__ == '__main__':
    unittest.main()