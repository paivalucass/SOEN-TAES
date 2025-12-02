def correct_bracketing(brackets: str):
    stack = []

    for bracket in brackets:
        if bracket == "(":
            stack.append(bracket)
        elif bracket == ")":
            if not stack or stack.pop() != "(":
                return False
    
    if stack:
        return False
    
    return True
import unittest

class Test(unittest.TestCase):
    def test_correct_bracketing(self):
        self.assertEqual(correct_bracketing('('), False)
        self.assertEqual(correct_bracketing('()'), True)
        self.assertEqual(correct_bracketing('(()())'), True)
        self.assertEqual(correct_bracketing(')()('), False)

if __name__ == '__main__':
    unittest.main()