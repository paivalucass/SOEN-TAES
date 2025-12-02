from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    result = []
    stack = []
    for char in paren_string:
        if char == '(': 
            stack.append('')
        elif char == ')':
            group = stack.pop()
            if stack:
                stack[-1] += group + char
            else:
                result.append(group + char)
    return result

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(separate_paren_groups('( ) (( )) (( )( ))'), ['()', '(())', '(()())'])

if __name__ == '__main__':
    unittest.main()