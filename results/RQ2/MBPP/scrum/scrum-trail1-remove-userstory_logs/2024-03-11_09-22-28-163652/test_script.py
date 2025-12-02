def remove_parenthesis(items):
    return items.split('(')[0].strip()
import unittest

class Test(unittest.TestCase):
    def test_remove_parenthesis(self):
        self.assertEqual(remove_parenthesis("python (chrome)"), "python")

if __name__ == '__main__':
    unittest.main()