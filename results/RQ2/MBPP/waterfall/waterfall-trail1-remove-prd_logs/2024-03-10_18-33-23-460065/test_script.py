def ascii_value(k):
    if len(k) == 1 and k.isalpha():
        return ord(k)
    else:
        return "Error: Input is not a valid character"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(ascii_value('A'), 65)

if __name__ == '__main__':
    unittest.main()