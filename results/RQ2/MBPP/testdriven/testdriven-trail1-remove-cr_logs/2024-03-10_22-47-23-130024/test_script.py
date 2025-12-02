import re

def find_literals(text, pattern):
    match = re.search(pattern, text)
    if match:
        return (match.group(), match.start(), match.end())
    else:
        return None
import re
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_literals('The quick brown fox jumps over the lazy dog.', 'fox'), ('fox', 16, 19))

if __name__ == '__main__':
    unittest.main()