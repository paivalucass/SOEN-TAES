import re

def find_literals(text, pattern):
    if not text or not pattern:
        return "Error: text and pattern cannot be empty or None"
    
    try:
        match = re.search(pattern, text)
        if match:
            return (match.group(), match.start(), match.end())
        else:
            return f"Error: No match found for pattern: {pattern}"
    except re.error as e:
        return f"Error: {e}"

import re
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_literals('The quick brown fox jumps over the lazy dog.', 'fox'), ('fox', 16, 19))

if __name__ == '__main__':
    unittest.main()