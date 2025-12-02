def correct_bracketing(brackets: str) -> bool:
    stack = []
    for b in brackets:
        if b == '(':
            stack.append(b)
        else:
            if not stack:
                return False
            stack.pop()
    return not stack

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(correct_bracketing('('), False)
        self.assertEqual(correct_bracketing('()'), True)
        self.assertEqual(correct_bracketing('(()())'), True)
        self.assertEqual(correct_bracketing(')('), False)

if __name__ == '__main__':
    unittest.main()