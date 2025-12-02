def correct_bracketing(brackets: str):
    stack = []
    for b in brackets:
        if b == '(':
            stack.append(b)
        elif b == ')':
            if len(stack) == 0:
                return False
            stack.pop()
    
    return len(stack) == 0
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(correct_bracketing('('), False)
        self.assertEqual(correct_bracketing('()'), True)
        self.assertEqual(correct_bracketing('(()())'), True)
        self.assertEqual(correct_bracketing(')('), False)

if __name__ == '__main__':
    unittest.main()