def correct_bracketing(brackets: str):
    """
    brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("<")
    False
    >>> correct_bracketing("<>")
    True
    >>> correct_bracketing("<<><>>")
    True
    >>> correct_bracketing("><<>>")
    False
    """

    stack = []
    opening_brackets = "<({["
    closing_brackets = ">)}]"

    bracket_map = {">": "<", "}": "{", ")": "(", "]": "["}

    for bracket in brackets:
        if bracket in opening_brackets:
            stack.append(bracket)
        elif bracket in closing_brackets:
            if not stack or stack[-1] != bracket_map[bracket]:
                return False
            stack.pop()

    return not stack
import unittest

class Test(unittest.TestCase):
    def test_correct_bracketing(self):
        self.assertEqual(correct_bracketing("<"), False)
        self.assertEqual(correct_bracketing("<>"), True)
        self.assertEqual(correct_bracketing("<<><>>"), True)
        self.assertEqual(correct_bracketing("><<>"), False)

if __name__ == '__main__':
    unittest.main()