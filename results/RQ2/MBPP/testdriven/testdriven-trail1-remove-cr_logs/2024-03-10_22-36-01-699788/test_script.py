def ascii_value(character):
    if len(character) != 1:
        raise ValueError("Input must be a single character")
    ascii_value = ord(character)
    return ascii_value
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(ascii_value('A'), 65)

if __name__ == '__main__':
    unittest.main()