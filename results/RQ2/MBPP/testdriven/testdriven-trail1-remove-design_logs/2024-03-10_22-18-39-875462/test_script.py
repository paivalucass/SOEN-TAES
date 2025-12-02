def check_expression(exp):
    '''
    Write a function to check if the given expression is balanced or not. 
    https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-an-expression/
    assert check_expression("{()}[{}]") == True
    '''

    # stack to store opening brackets
    stack = []

    # set of opening brackets
    opening_brackets = set(['(', '[', '{'])

    # set of closing brackets
    closing_brackets = set([')', ']', '}'])

    # dictionary to store bracket pairs
    bracket_pairs = {'(': ')', '[': ']', '{': '}'}

    # iterate through each character in the expression
    for char in exp:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            # check if the stack is empty
            if not stack:
                return False
            # check if the closing bracket matches the last opening bracket
            if bracket_pairs[stack.pop()] != char:
                return False

    # check if the stack is empty
    return not stack
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_expression("{()}[{}]"), True)

if __name__ == '__main__':
    unittest.main()