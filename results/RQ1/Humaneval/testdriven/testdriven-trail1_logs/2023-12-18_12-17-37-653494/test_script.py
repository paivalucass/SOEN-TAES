from typing import List
import re

def separate_paren_groups(paren_string: str) -> List[str]:
    if not paren_string:
        return []

    if not all(char in "()" for char in paren_string):
        return ["Invalid Input"]

    paren_string = paren_string.replace(" ", "")
    separate_groups = []

    while paren_string:
        match = re.match(r"\(([^()]+)\)", paren_string)
        if match:
            separate_groups.append(match.group())
            paren_string = paren_string.replace(match.group(), "", 1)
        else:
            return ["Invalid Input"]

    return separate_groups
import unittest
from typing import List

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(separate_paren_groups('( ) (( )) (( )( ))'), ['()', '(())', '(()())'])

if __name__ == '__main__':
    unittest.main()