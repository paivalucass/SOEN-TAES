def replace_char(str1, ch, newch):
    if not str1 or len(ch) != 1:
        return "Invalid input"

    modified_str = str1.replace(ch, newch)

    return modified_str
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(replace_char("polygon", 'y', 'l'), "pollgon")

if __name__ == '__main__':
    unittest.main()