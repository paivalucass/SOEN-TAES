from typing import List
import re

def separate_paren_groups(paren_string: str) -> List[str]:
    clean_string = re.sub(r'\s+', '', paren_string)
    pattern = r'\([^()]*\)'
    groups = re.findall(pattern, clean_string)
    return groups
import unittest
from typing import List

class Test(unittest.TestCase):
    def test_separate_paren_groups(self):
        self.assertEqual(separate_paren_groups('( ) (( )) (( )( ))'), ['()', '(())', '(()())'])

if __name__ == '__main__':
    unittest.main()