from typing import List
import re

def separate_paren_groups(paren_string: str) -> List[str]:
    pattern = r'\([^()]*\)'
    separated_groups = re.findall(pattern, paren_string)
    return separated_groups

import unittest
from typing import List

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(separate_paren_groups('( ) (( )) (( )( ))'), ['()', '(())', '(()())'])

if __name__ == '__main__':
    unittest.main()