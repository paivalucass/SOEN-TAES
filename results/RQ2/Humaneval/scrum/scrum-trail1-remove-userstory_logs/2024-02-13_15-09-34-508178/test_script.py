def correct_bracketing(brackets: str):
    stack = []
    for char in brackets:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            else:
                stack.pop()
    if stack:
        return False
    else:
        return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(correct_bracketing('('), False)
        self.assertEqual(correct_bracketing('()'), True)
        self.assertEqual(correct_bracketing('(()())'), True)
        self.assertEqual(correct_bracketing(')('), False)

if __name__ == '__main__':
    unittest.main()