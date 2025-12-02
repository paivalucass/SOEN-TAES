def remove_parenthesis(items):
    import re
    modified_items = [re.sub(r"\([^)]*\)", "", item).strip() for item in items]
    return ''.join(modified_items)

import unittest

class Test(unittest.TestCase):
    def test_remove_parenthesis(self):
        self.assertEqual(remove_parenthesis("python (chrome)"), "python")

if __name__ == '__main__':
    unittest.main()