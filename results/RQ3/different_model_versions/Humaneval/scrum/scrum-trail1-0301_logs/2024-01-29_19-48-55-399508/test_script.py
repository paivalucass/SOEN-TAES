def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of.
    :param string: the input string
    :type string: str
    :return: the number of distinct characters in the string
    :rtype: int
    """
    if not isinstance(string, str):
        raise TypeError("Input must be a string")

    if len(string) == 0:
        return 0
    
    string = string.lower()
    distinct_chars = set(string)
    return len(distinct_chars)
import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(count_distinct_characters('xyzXYZ'), 3)
    def test2(self):
        self.assertEqual(count_distinct_characters('Jerry'), 4)
    def test3(self):
        self.assertEqual(count_distinct_characters('Hello World'), 8)
    
if __name__ == '__main__':
    unittest.main()