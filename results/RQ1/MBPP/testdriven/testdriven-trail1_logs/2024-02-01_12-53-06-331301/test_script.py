def replace_char(str1, ch, newch):
    if not isinstance(str1, str) or not isinstance(ch, str) or not isinstance(newch, str):
        raise TypeError("Input parameters must be of type string")

    if len(ch) != 1 or len(newch) != 1:
        raise ValueError("Parameters 'ch' and 'newch' must be single characters")

    modified_str = str1.replace(ch, newch)
    return modified_str
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(replace_char('polygon', 'y', 'l'), 'pollgon')

if __name__ == '__main__':
    unittest.main()