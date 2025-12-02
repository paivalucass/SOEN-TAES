def count_distinct_characters(string: str) -> int:
    if string is None or len(string) == 0:
        raise ValueError("Input string is empty or null")

    distinct_characters = set(string.lower())
    distinct_characters.discard(' ')  # Discard spaces if needed

    return len(distinct_characters)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_distinct_characters('xyzXYZ'), 3)
        self.assertEqual(count_distinct_characters('Jerry'), 4)

if __name__ == '__main__':
    unittest.main()