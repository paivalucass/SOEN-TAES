def ascii_value(character):
    if len(character) != 1:
        return "Invalid input"
    return ord(character)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(ascii_value('A'), 65)

if __name__ == '__main__':
    unittest.main()