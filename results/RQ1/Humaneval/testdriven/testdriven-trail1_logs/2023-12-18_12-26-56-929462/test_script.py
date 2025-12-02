def correct_bracketing(brackets: str):
    bracket_map = {'<': '>', '[': ']', '(': ')', '{': '}'}
    stack = []
    for bracket in brackets:
        if bracket in bracket_map:
            stack.append(bracket)
        elif bracket in bracket_map.values():
            if not stack:
                return False
            opening_bracket = stack.pop()
            if bracket_map[opening_bracket] != bracket:
                return False
    return not stack
import unittest

class Test(unittest.TestCase):
    def test_correct_bracketing(self):
        self.assertEqual(correct_bracketing('<'), False)
        self.assertEqual(correct_bracketing('<>'), True)
        self.assertEqual(correct_bracketing('<<><>>'), True)
        self.assertEqual(correct_bracketing('><<>'), False)

if __name__ == '__main__':
    unittest.main()