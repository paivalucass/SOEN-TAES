def validate_input(input_string: str) -> bool:
    for char in input_string:
        if char not in ['<', '>']:
            return False
    return True

def correct_bracketing(brackets: str) -> bool:
    if not validate_input(brackets):
        return False
    
    stack = []
    
    for char in brackets:
        if char == '<':
            stack.append(char)
        elif char == '>':
            if stack and stack[-1] == '<':
                stack.pop()
            else:
                return False
        else:
            continue
    
    if stack:
        return False
    
    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertFalse(correct_bracketing("<"))
        self.assertTrue(correct_bracketing("<>"))
        self.assertTrue(correct_bracketing("<<><>>"))
        self.assertFalse(correct_bracketing("><<>"))

if __name__ == '__main__':
    unittest.main()