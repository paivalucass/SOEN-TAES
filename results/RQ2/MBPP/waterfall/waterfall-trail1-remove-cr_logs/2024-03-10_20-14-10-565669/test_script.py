import re

def remove_parenthesis(items):
    modified_list = []
    for item in items:
        modified_item = re.sub(r"\([^)]*\)", "", item).strip()
        modified_list.append(modified_item)
    return modified_list
import unittest

class Test(unittest.TestCase):
    def test_remove_parenthesis(self):
        self.assertEqual(remove_parenthesis("python (chrome)"), "python")

if __name__ == '__main__':
    unittest.main()