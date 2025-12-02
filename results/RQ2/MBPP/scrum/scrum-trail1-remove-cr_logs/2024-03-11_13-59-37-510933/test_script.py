def text_match_zero_one(text):
    import re
    pattern = 'ab+'
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    
    match = re.search(pattern, text)
    if match:
        return True
    else:
        return False
import re
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(text_match_zero_one('ac'), False)

if __name__ == '__main__':
    unittest.main()