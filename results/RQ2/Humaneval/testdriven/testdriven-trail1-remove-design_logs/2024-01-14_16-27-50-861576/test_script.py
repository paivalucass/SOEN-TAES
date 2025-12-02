def fix_spaces(text):
    import re
    result = re.sub(r'\s{2,}', '-', text.strip().replace(' ', '_'))
    return result
import unittest

class Test(unittest.TestCase):
    def test_fix_spaces(self):
        self.assertEqual(fix_spaces("Example"), "Example")
        self.assertEqual(fix_spaces("Example 1"), "Example_1")
        self.assertEqual(fix_spaces(" Example 2"), "_Example_2")
        self.assertEqual(fix_spaces(" Example   3"), "_Example-3")

if __name__ == '__main__':
    unittest.main()