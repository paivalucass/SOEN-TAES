from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    result = []
    current_group = ''
    open_count = 0
    for char in paren_string:
        if char == '(': 
            open_count += 1
            current_group += char
        elif char == ')':
            open_count -= 1
            current_group += char
            if open_count == 0:
                result.append(current_group)
                current_group = ''
    return result
import unittest

from typing import List

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(separate_paren_groups('( ) (( )) (( )( ))'), ['()', '(())', '(()())'])

if __name__ == '__main__':
    unittest.main()