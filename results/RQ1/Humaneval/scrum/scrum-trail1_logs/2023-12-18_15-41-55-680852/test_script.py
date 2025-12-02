def is_string_balanced(s):
    open_count = 0
    for char in s:
        if char == '(':
            open_count += 1
        elif char == ')':
            if open_count == 0:
                return False
            open_count -= 1
    return open_count == 0

def can_form_balanced_string(lst):
    s1, s2 = lst
    if not all(c in '()' for c in s1 + s2):
        return 'No'
    return 'Yes' if is_string_balanced(s1 + s2) or is_string_balanced(s2 + s1) else 'No'

def match_parens(lst):
    s1, s2 = lst
    if not all(c in '()' for c in s1 + s2):
        return 'No'
    return 'Yes' if is_string_balanced(s1 + s2) or is_string_balanced(s2 + s1) else 'No'
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(match_parens(['()(', ')']), 'Yes')
        self.assertEqual(match_parens([')', ')']), 'No')

if __name__ == '__main__':
    unittest.main()