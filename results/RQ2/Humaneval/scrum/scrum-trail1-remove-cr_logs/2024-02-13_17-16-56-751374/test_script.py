def fix_spaces(text):
    text = text.strip()
    text = text.replace(' ', '_')
    if '__' in text:
        text = text.replace('__', '-')
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