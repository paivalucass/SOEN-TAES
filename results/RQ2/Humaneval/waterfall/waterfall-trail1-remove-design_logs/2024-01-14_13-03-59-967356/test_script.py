from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    result = []
    stack = 0
    temp = ""
    for s in paren_string:
        if s == '(':
            stack += 1
            temp += s
        elif s == ')':
            if stack > 0:
                stack -= 1
                temp += s
                if stack == 0:
                    result.append(temp)
                    temp = ""
            else:
                raise ValueError("Unbalanced parentheses")
    if stack > 0:
        raise ValueError("Unbalanced parentheses")
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(separate_paren_groups('( ) (( )) (( )( ))'), ['()', '(())', '(()())'])

if __name__ == '__main__':
    unittest.main()