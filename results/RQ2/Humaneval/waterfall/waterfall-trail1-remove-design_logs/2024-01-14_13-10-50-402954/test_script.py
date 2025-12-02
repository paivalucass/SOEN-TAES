from typing import List

def correct_bracketing(brackets: str) -> bool:
    stack = []

    for bracket in brackets:
        if bracket == "(":
            stack.append(bracket)
        else:
            if not stack:
                return False
            stack.pop()

    return len(stack) == 0

import unittest

class Test(unittest.TestCase):
    def test_correct_bracketing(self):
        self.assertEqual(correct_bracketing('('), False)
        self.assertEqual(correct_bracketing('()'), True)
        self.assertEqual(correct_bracketing('(()())'), True)
        self.assertEqual(correct_bracketing(')('), False)

if __name__ == '__main__':
    unittest.main()