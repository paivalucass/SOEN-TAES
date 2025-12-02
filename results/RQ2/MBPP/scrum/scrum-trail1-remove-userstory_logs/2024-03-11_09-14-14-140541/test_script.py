def replace_char(originalString, charToReplace, newChar):
    if not isinstance(originalString, str) or not isinstance(charToReplace, str) or not isinstance(newChar, str):
        return "Error: Invalid input type"

    if not originalString:
        return originalString

    newString = originalString.replace(charToReplace, newChar)
    return newString
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(replace_char("polygon", 'y', 'l'), "pollgon")

if __name__ == '__main__':
    unittest.main()