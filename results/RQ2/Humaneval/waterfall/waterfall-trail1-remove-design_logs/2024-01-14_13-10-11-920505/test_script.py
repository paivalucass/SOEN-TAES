def correct_bracketing(brackets: str):
    stack = []
    for bracket in brackets:
        if bracket == "<":
            stack.append(bracket)
        elif bracket == ">" and stack:
            stack.pop()
        else:
            return False

    return len(stack) == 0

# Test cases
def test_correct_bracketing():
    assert correct_bracketing("") == True
    assert correct_bracketing("<>") == True
    assert correct_bracketing("<>>") == False
    assert correct_bracketing("<<>>><<") == False
    assert correct_bracketing("<><><>") == True

test_correct_bracketing()
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertFalse(correct_bracketing("<"))
        self.assertTrue(correct_bracketing("<>"))
        self.assertTrue(correct_bracketing("<<><>>"))
        self.assertFalse(correct_bracketing("><<>"))

if __name__ == '__main__':
    unittest.main()