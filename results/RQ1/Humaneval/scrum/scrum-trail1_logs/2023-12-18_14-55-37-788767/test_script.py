def count_distinct_characters(string: str) -> int:
    if not isinstance(string, str):
        raise TypeError("Input should be a string")

    if len(string) == 0:
        return 0

    string = string.lower()
    distinct_chars = set(string)
    return len(distinct_chars)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_distinct_characters('xyzXYZ'), 3)
        self.assertEqual(count_distinct_characters('Jerry'), 4)

if __name__ == '__main__':
    unittest.main()