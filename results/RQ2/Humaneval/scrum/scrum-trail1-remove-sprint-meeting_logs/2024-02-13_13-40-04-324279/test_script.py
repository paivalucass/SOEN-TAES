def how_many_times(string: str, substring: str) -> int:
    if not string or not substring:
        return 0
    count = 0
    start = 0
    while True:
        start = string.find(substring, start) + 1
        if start > 0:
            count += 1
        else:
            break
    return count
import unittest

class Test(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(how_many_times('', 'a'), 0)

    def test_single_substring(self):
        self.assertEqual(how_many_times('aaa', 'a'), 3)

    def test_multiple_substring(self):
        self.assertEqual(how_many_times('aaaa', 'aa'), 3)

if __name__ == '__main__':
    unittest.main()