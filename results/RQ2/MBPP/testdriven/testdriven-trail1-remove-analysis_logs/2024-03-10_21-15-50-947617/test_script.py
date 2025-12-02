import re
def text_match_two_three(text):
    if isinstance(text, str):
        if re.search(r'ab{2,3}', text):
            return True
        else:
            return False
    else:
        raise ValueError("Input is not a string")

import re
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(text_match_two_three('ac'), False)

if __name__ == '__main__':
    unittest.main()