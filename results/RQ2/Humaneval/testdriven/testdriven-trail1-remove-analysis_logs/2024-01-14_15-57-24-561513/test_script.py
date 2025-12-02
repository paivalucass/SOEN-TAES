def match_parens(lst):
    open_count = 0
    for s in lst:
        for char in s:
            if char == '(': 
                open_count += 1
            elif open_count > 0:
                open_count -= 1
            else:
                return 'No'
    return 'Yes' if open_count == 0 else 'No'
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(function_under_test(['()(', ')']), 'Yes')
        self.assertEqual(function_under_test([')', ')']), 'No')

if __name__ == '__main__':
    unittest.main()