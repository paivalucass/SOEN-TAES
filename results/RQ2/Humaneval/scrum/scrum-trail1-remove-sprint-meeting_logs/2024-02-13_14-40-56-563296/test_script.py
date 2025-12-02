def fix_spaces(text):
    import re

    try:
        if not isinstance(text, str) or len(text) == 0:
            raise ValueError("Input must be a non-empty string")
    except (TypeError, ValueError) as e:
        return str(e)

    text = text.replace(" ", "_")
    text = re.sub(r'_{2,}', '-', text)

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