def correct_bracketing(brackets: str) -> bool:
    stack = []
    for bracket in brackets:
        if bracket == '<':
            stack.append(bracket)
        elif bracket == '>' and stack:
            stack.pop()
        else:
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