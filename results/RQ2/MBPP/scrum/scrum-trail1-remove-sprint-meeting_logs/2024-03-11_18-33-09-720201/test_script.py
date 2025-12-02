def ascii_value(k):
    try:
        if len(k) != 1 or not k.isalpha():
            raise ValueError("Invalid input: Please provide a single alphabetic character.")
        return ord(k)
    except ValueError as e:
        return str(e)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(ascii_value('A'), 65)

if __name__ == '__main__':
    unittest.main()