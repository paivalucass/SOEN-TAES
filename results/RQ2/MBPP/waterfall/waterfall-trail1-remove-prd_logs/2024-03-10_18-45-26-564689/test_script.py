import re

def remove_parenthesis(items):
    result = [re.sub(r"\([^)]*\)", "", string).strip().replace(' ', '') for string in items]
    return result[0]
import unittest

class Test(unittest.TestCase):
    def test_remove_parenthesis(self):
        self.assertEqual(remove_parenthesis("python (chrome)"), "python")

if __name__ == '__main__':
    unittest.main()