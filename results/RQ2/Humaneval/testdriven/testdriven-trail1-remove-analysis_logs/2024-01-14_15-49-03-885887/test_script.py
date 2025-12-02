def correct_bracketing(brackets: str) -> bool:
    """
    brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("<")
    False
    >>> correct_bracketing("<>")
    True
    >>> correct_bracketing("<<><>>")
    True
    >>> correct_bracketing("><<>")
    False
    """

    stack = []  # stack to store opening brackets
    for char in brackets:
        if char == '<':
            stack.append(char)
        elif char == '>':
            if len(stack) == 0:  # no matching opening bracket
                return False
            stack.pop()  # remove the matching opening bracket
        else:
            return False  # invalid character

    return len(stack) == 0  # check if all opening brackets have matching closing brackets
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(correct_bracketing('<'), False)
        self.assertEqual(correct_bracketing('<>'), True)
        self.assertEqual(correct_bracketing('<<><>>'), True)
        self.assertEqual(correct_bracketing('><<>'), False)

if __name__ == '__main__':
    unittest.main()