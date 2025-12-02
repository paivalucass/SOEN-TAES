from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    levels = []
    count = 0
    max_level = 0
    result = []
    for char in paren_string:
        if char == '(': count += 1
        elif char == ')': count -= 1
        max_level = max_level + 1 if char in ['(', ')'] else max_level
        if len(levels) >= max_level:
            levels[max_level - 1] = count
        else:
            levels.append(count)
    for i in range(len(levels)):
        result.append(levels[i])
    return result
import unittest
from typing import List

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(parse_nested_parens('(()()) ((())) () ((())()())'), [2, 3, 1, 3])

if __name__ == '__main__':
    unittest.main()