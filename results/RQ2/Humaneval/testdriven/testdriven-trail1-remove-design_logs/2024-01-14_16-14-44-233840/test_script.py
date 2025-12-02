def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # convert the string to lower case and then find the set of characters
    distinct_chars = set(string.lower())
    # return the length of the set which gives the count of distinct characters
    return len(distinct_chars)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_distinct_characters('xyzXYZ'), 3)
        self.assertEqual(count_distinct_characters('Jerry'), 4)

if __name__ == '__main__':
    unittest.main()