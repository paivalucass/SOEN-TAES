from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    result = []
    count = 0
    current = ''
    for char in paren_string:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
        if char != ' ':
            current += char
        if count == 0 and current:
            result.append(current)
            current = ''
    return result

import unittest
from typing import List

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(separate_paren_groups('( ) (( )) (( )( ))'), ['()', '(())', '(()())'])

if __name__ == '__main__':
    unittest.main()