def correct_bracketing(brackets: str) -> bool:
    OPENING_BRACKETS = ["(", "[", "{"]
    CLOSING_BRACKETS = [")", "]", "}"]
    stack = []
    for bracket in brackets:
        if bracket in OPENING_BRACKETS:
            stack.append(bracket)
        elif bracket in CLOSING_BRACKETS:
            if not stack:
                return False
            top = stack.pop()
            if (bracket == ")" and top != "(") or (bracket == "]" and top != "[") or (bracket == "}" and top != "{"):
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