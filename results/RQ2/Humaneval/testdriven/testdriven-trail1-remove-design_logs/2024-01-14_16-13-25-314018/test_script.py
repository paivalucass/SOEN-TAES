from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    result = []
    current = ""
    open_brace_count = 0
    for char in paren_string:
        if char == '(': 
            open_brace_count += 1
            if open_brace_count == 1:
                current = ""
            else:
                current += char
        elif char == ')':
            open_brace_count -= 1
            if open_brace_count == 0:
                result.append(current)
                current = ""
            else:
                current += char
    return result
import unittest
from typing import List

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(separate_paren_groups('( ) (( )) (( )( ))'), ['()', '(())', '(()())'])

if __name__ == '__main__':
    unittest.main()