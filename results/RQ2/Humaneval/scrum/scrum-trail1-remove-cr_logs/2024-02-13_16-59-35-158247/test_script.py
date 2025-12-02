def correct_bracketing(brackets: str) -> bool:
    stack = []
    opening_brackets = ['(']
    closing_brackets = [')']
    
    for bracket in brackets:
        if bracket in opening_brackets:
            stack.append(bracket)
        elif bracket in closing_brackets:
            if len(stack) == 0:
                return False
            else:
                stack.pop()
        else:
            return False
    
    if len(stack) == 0:
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(correct_bracketing('('), False)
        self.assertEqual(correct_bracketing('()'), True)
        self.assertEqual(correct_bracketing('(()())'), True)
        self.assertEqual(correct_bracketing(')('), False)

if __name__ == '__main__':
    unittest.main()