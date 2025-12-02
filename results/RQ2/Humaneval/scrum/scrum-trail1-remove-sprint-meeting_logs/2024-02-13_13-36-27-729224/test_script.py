from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    def max_nested_level(paren_group: str) -> int:
        stack = []
        max_level = 0
        current_level = 0

        for char in paren_group:
            if char == '(':
                stack.append(char)
                current_level += 1
                max_level = max(max_level, current_level)
            elif char == ')':
                if not stack:
                    raise ValueError("Invalid input: unbalanced parentheses")
                stack.pop()
                current_level -= 1
        
        if stack:
            raise ValueError("Invalid input: unbalanced parentheses")
        
        return max_level

    groups = paren_string.split()
    result = [max_nested_level(group) for group in groups]
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(parse_nested_parens('(()()) ((())) () ((())()())'), [2, 3, 1, 3])

if __name__ == '__main__':
    unittest.main()