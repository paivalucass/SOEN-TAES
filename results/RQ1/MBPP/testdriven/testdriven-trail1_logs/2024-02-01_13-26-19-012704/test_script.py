def check_expression(exp):
    bracket_pairs = {'{': '}', '[': ']', '(': ')'}
    stack = []

    for char in exp:
        if char in bracket_pairs.keys():
            stack.append(char)
        elif char in bracket_pairs.values():
            if not stack:
                return False
            last_opening_bracket = stack.pop()
            if char != bracket_pairs[last_opening_bracket]:
                return False

    return not stack
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_expression('{()}[{}]'), True)

if __name__ == '__main__':
    unittest.main()