def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    if not isinstance(string, str):
        raise ValueError("Input is not a valid string.")
    
    distinct_characters = set(string.lower())
    return len(distinct_characters)
import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(count_distinct_characters('xyzXYZ'), 3)
        
    def test2(self):
        self.assertEqual(count_distinct_characters('Jerry'), 4)

if __name__ == '__main__':
    unittest.main()