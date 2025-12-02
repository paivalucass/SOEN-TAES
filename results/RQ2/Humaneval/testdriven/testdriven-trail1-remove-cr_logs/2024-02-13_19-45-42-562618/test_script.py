def correct_bracketing(brackets: str) -> bool:
    stack = []
    opening_brackets = ["<", "[", "{", "("]
    closing_brackets = [">", "]", "}", ")"]
    
    for bracket in brackets:
        if bracket in opening_brackets:
            stack.append(bracket)
        elif bracket in closing_brackets:
            if not stack:
                return False
            else:
                if opening_brackets.index(stack.pop()) != closing_brackets.index(bracket):
                    return False
    
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