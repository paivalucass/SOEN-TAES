import re

def fix_spaces(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")

    if len(text) == 0:
        return ""

    # Replace all spaces with underscores
    modified_text = re.sub(r'\s+', '_', text)

    # Replace more than 2 consecutive spaces with -
    modified_text = re.sub(r'_{3,}', '-', modified_text)

    return modified_text
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(fix_spaces("Example"), "Example")
        self.assertEqual(fix_spaces("Example 1"), "Example_1")
        self.assertEqual(fix_spaces(" Example 2"), "_Example_2")
        self.assertEqual(fix_spaces(" Example   3"), "_Example-3")

if __name__ == '__main__':
    unittest.main()