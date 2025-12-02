def text_match_three(text):
    import re
    # Function to match a string that has an 'a' followed by three 'b's
    # Regular expression pattern: 'ab{3}'
    if text is None or len(text) < 4:
        return False
    else:
        pattern = 'ab{3}'
        if re.search(pattern, text):
            return True
        else:
            return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(text_match_three('ac'), False)

if __name__ == '__main__':
    unittest.main()