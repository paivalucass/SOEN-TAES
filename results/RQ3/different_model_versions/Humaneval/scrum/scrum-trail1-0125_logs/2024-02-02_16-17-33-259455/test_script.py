def correct_bracketing(brackets: str) -> bool:
    stack = []

    bracket_map = {
        ")": "(",
        "}": "{",
        "]": "["
    }

    for bracket in brackets:
        if bracket in bracket_map.values():
            stack.append(bracket)
        elif bracket in bracket_map.keys():
            if not stack:
                return False
            if stack[-1] == bracket_map[bracket]:
                stack.pop()
            else:
                return False

    return len(stack) == 0
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertFalse(correct_bracketing("("))
        self.assertTrue(correct_bracketing("()"))
        self.assertTrue(correct_bracketing("(()())"))
        self.assertFalse(correct_bracketing(")()"))

if __name__ == '__main__':
    unittest.main()