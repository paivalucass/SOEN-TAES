def count_distinct_characters(string: str) -> int:
    if not string:
        return 0  # handling empty string case
    distinct_chars = set(string.lower())  # handling case sensitivity
    return len(distinct_chars)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_distinct_characters('xyzXYZ'), 3)
        self.assertEqual(count_distinct_characters('Jerry'), 4)

if __name__ == '__main__':
    unittest.main()