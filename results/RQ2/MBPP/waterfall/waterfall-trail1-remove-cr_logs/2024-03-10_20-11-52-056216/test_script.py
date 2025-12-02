def find_literals(text, pattern):
    if text is None or pattern is None or text == '' or pattern == '':
        return "Input validation error: text and pattern cannot be empty or null"
    
    import re
    match = re.search(pattern, text)
    if match:
        return (match.group(), match.start(), match.end())
    else:
        return "Pattern not found in text"
import re
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_literals('The quick brown fox jumps over the lazy dog.', 'fox'), ('fox', 16, 19))

if __name__ == '__main__':
    unittest.main()