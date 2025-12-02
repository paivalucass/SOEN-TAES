from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    
    stack = []
    result = []
    for i in range(len(paren_string)):
        if paren_string[i] == '(':  # if open bracket, add to stack
            stack.append(i)
        elif paren_string[i] == ')' and stack:  # if closing bracket and stack not empty, add to result
            start = stack.pop()
            if not stack:  # if stack empty, balance found
                result.append(paren_string[start:i+1])
    return result
import unittest

from typing import List

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(separate_paren_groups('( ) (( )) (( )( ))'), ['()', '(())', '(()())'])

if __name__ == '__main__':
    unittest.main()