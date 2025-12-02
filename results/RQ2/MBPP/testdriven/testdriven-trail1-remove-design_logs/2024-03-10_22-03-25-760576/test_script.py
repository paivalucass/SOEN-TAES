def ascii_value(character):
    '''
    Write a function to find the ASCII value of a character.
    - Input: character (string)
    - Output: ASCII value of the character (integer)
    '''
    if len(character) != 1:
        return "Error - Input is not a single character"
    elif not character.isalpha():
        return "Error - Input is not a character"
    else:
        return ord(character)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(ascii_value('A'), 65)

if __name__ == '__main__':
    unittest.main()