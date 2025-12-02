from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    levels = []
    current_level = 0
    max_level = 0
    stack = []
    
    for char in paren_string:
        if char == '(':
            stack.append('(')
            current_level += 1
            max_level = max(max_level, current_level)
        elif char == ')':
            stack.pop()
            current_level -= 1
        elif char == ' ':
            levels.append(max_level)
            max_level = 0
    
    levels.append(max_level)
    return levels
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(parse_nested_parens('(()()) ((())) () ((())()())'), [2, 3, 1, 3])

if __name__ == '__main__':
    unittest.main()