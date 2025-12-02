from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    if not isinstance(string, str):
        return "Error: Invalid input data type"
    elif string == '':
        return []
    else:
        prefixes = [string[:i+1] for i in range(len(string))]
        return prefixes
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(all_prefixes('abc'), ['a', 'ab', 'abc'])

if __name__ == '__main__':
    unittest.main()