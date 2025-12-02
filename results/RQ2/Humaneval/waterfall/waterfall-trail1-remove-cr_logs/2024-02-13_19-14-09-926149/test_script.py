from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    if not paren_string:
        return []

    stack = []
    result = []

    for group in paren_string.split():
        level = 0
        for char in group:
            if char == '(':
                stack.append(char)
                level = max(level, len(stack))
            elif char == ')':
                if not stack:
                    return "Invalid parentheses sequence"
                else:
                    stack.pop()
        result.append(level)

    if stack:
        return "Invalid parentheses sequence"
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(parse_nested_parens('(()()) ((())) () ((())()())'), [2, 3, 1, 3])

if __name__ == '__main__':
    unittest.main()