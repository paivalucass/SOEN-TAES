def fix_spaces(text):
    if not isinstance(text, str):
        raise ValueError("Input text must be a string")

    text = text.replace(" ", "_")
    while "__" in text:
        text = text.replace("__", "-")
    while "  " in text:
        text = text.replace("  ", "-")

    return text
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(fix_spaces("Example"), "Example")
        self.assertEqual(fix_spaces("Example 1"), "Example_1")
        self.assertEqual(fix_spaces(" Example 2"), "_Example_2")
        self.assertEqual(fix_spaces(" Example   3"), "_Example-3")

if __name__ == '__main__':
    unittest.main()