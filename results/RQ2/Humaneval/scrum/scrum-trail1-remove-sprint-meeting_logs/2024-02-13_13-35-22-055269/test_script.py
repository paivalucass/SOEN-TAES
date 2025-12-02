from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    paren_list = []
    temp = ""
    open_count = 0

    for char in paren_string:
        if char == "(":
            open_count += 1
            temp += char
        elif char == ")":
            open_count -= 1
            temp += char
            if open_count == 0:
                paren_list.append(temp)
                temp = ""

    return paren_list
import unittest
from typing import List

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(separate_paren_groups('( ) (( )) (( )( ))'), ['()', '(())', '(()())'])

if __name__ == '__main__':
    unittest.main()