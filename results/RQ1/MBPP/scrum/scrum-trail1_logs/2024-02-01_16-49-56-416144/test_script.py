def check_expression(exp):
    stack = []
    opening_brackets = set(['(', '{', '['])
    closing_brackets = set([')', '}', ']'])
    bracket_map = {')': '(', '}': '{', ']': '['}

    for char in exp:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack:
                return False
            if stack[-1] == bracket_map[char]:
                stack.pop()
            else:
                return False

    return not stack

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_expression('{()}[{}]'), True)

if __name__ == '__main__':
    unittest.main()