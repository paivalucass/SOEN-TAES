import re
import unittest

def text_lowercase_underscore(text: str) -> bool:
    return bool(re.match('^[a-z]+(_[a-z]+)*$', text))

if __name__ == '__main__':
    unittest.main()
import re

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(text_lowercase_underscore('aab_cbbbc'), True)

if __name__ == '__main__':
    unittest.main()