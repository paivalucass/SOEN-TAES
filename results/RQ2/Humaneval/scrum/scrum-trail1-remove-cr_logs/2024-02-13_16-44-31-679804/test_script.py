from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    stack = []
    result = []
    temp = ''
    for char in paren_string:
        if char == '(': 
            if temp:
                result.append(temp)
            stack.append('(')
            temp = '(' 
        elif char == ')':
            stack.pop()
            temp += ')'
            if not stack:
                result.append(temp)
                temp = ''
    return result
import unittest
from typing import List

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(separate_paren_groups('( ) (( )) (( )( ))'), ['()', '(())', '(()())'])

if __name__ == '__main__':
    unittest.main()