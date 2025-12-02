from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    if not paren_string:
        return []

    stack = []
    result = []
    group = ''

    for char in paren_string:
        if char == '(':
            stack.append(char)
            group += char
        elif char == ')':
            stack.pop()
            group += char
            if not stack:
                result.append(group)
                group = ''

    return result
import unittest
from typing import List

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(separate_paren_groups('( ) (( )) (( )( ))'), ['()', '(())', '(()())'])

if __name__ == '__main__':
    unittest.main()