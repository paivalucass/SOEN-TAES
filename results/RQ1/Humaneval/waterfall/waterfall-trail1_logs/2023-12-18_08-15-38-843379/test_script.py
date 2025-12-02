def correct_bracketing(brackets: str) -> bool:
    stack = []

    for bracket in brackets:
        if bracket == '<':
            stack.append(bracket)
        elif bracket == '>':
            if not stack:
                return False
            stack.pop()
        else:
            raise ValueError("Invalid character in input")

    if stack:
        return False
    return True
import unittest

class Test(unittest.TestCase):
    def test_correct_bracketing(self):
        self.assertFalse(correct_bracketing("<"))
        self.assertTrue(correct_bracketing("<>"))
        self.assertTrue(correct_bracketing("<<><>>"))
        self.assertFalse(correct_bracketing("><<>>"))

if __name__ == '__main__':
    unittest.main()