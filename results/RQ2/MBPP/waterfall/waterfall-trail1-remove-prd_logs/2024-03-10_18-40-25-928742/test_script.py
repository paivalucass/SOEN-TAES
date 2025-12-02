def replace_char(str1, ch, newch):
    if len(str1) == 0 or len(ch) != 1 or len(newch) != 1:
        return "Invalid input"

    if not str1.strip() or ch.isspace() or newch.isspace():
        return "Invalid input"

    import re
    modified_str = re.sub(r'(?<!\\S)' + re.escape(ch) + r'(?!\\S)', newch, str1)
    return modified_str
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(replace_char("polygon",'y','l'), "pollgon")

if __name__ == '__main__':
    unittest.main()