def count_distinct_characters(string: str) -> int:
    distinct_chars = set(string.lower())
    distinct_chars.discard(' ')
    return len(distinct_chars)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_distinct_characters('xyzXYZ'), 3)
        self.assertEqual(count_distinct_characters('Jerry'), 4)

if __name__ == '__main__':
    unittest.main()