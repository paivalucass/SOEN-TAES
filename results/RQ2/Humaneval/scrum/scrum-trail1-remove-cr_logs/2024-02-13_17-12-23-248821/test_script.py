def match_parens(lst):
    open_count = 0
    for s in lst:
        for char in s:
            if char == '(': 
                open_count += 1
            else:
                if open_count == 0:
                    return 'No'
                open_count -= 1
    if open_count == 0:
        return 'Yes'
    else:
        return 'No'
import unittest

class Test(unittest.TestCase):
    def test_match_parens(self):
        self.assertEqual(match_parens(['()(', ')']), 'Yes')
        self.assertEqual(match_parens([')', ')']), 'No')

if __name__ == '__main__':
    unittest.main()