def fix_spaces(text):
    if text is None or len(text) == 0:
        return "Invalid input"
    else:
        text = text.replace(" ", "_")
        while "  " in text:
            text = text.replace("  ", "-")
        return text
import unittest

class Test(unittest.TestCase):
    def test_fix_spaces(self):
        self.assertEqual(fix_spaces("Example"), "Example")
        self.assertEqual(fix_spaces("Example 1"), "Example_1")
        self.assertEqual(fix_spaces(" Example 2"), "_Example_2")
        self.assertEqual(fix_spaces(" Example   3"), "_Example-3")

if __name__ == '__main__':
    unittest.main()