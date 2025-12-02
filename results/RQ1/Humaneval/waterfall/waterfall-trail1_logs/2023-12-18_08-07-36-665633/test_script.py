from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    result = []
    stack = []
    group = ""

    for char in paren_string:
        if char == "(":
            stack.append(char)
            group += char
        elif char == ")":
            if stack:
                stack.pop()
                group += char
                if not stack:
                    result.append(group)
                    group = ""
            else:
                return ["Invalid input: Unbalanced parentheses"]
    
    if stack:
        return ["Invalid input: Unbalanced parentheses"]

    return result
import unittest
from typing import List

class Test(unittest.TestCase):
    def test_separate_paren_groups(self):
        self.assertEqual(separate_paren_groups('( ) (( )) (( )( ))'), ['()', '(())', '(()())'])

if __name__ == '__main__':
    unittest.main()