def match_parens(lst):
    open_paren_count = 0
    for string in lst:
        for char in string:
            if char == '(': open_paren_count += 1
            else:
                if open_paren_count == 0: return 'No'
                open_paren_count -= 1
    return 'Yes' if open_paren_count == 0 else 'No'

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(function_under_test(['()(', ')']), 'Yes')
        self.assertEqual(function_under_test([')', ')']), 'No')

if __name__ == '__main__':
    unittest.main()