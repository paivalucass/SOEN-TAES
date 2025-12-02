def correct_bracketing(brackets: str) -> bool:
    """
    brackets is a string of "(" and ")".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("(")
    False
    >>> correct_bracketing("()")
    True
    >>> correct_bracketing("(()())")
    True
    >>> correct_bracketing(")()")
    False
    """
    stack = []
    for char in brackets:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            if stack[-1] == '(':
                stack.pop()
            else:
                return False
    return not stack
import unittest

class Test(unittest.TestCase):
    def test_correct_bracketing(self):
        self.assertEqual(correct_bracketing('('), False)
        self.assertEqual(correct_bracketing('()'), True)
        self.assertEqual(correct_bracketing('(()())'), True)
        self.assertEqual(correct_bracketing(')('), False)

if __name__ == '__main__':
    unittest.main()