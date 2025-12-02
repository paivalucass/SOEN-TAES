def how_many_times(string: str, substring: str) -> int:
    if not string or not substring:
        return 0

    count = 0
    len_sub = len(substring)
    for i in range(len(string) - len_sub + 1):
        if string[i:i + len_sub] == substring:
            count += 1

    return count
import unittest

class Test(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(how_many_times('', 'a'), 0)
        
    def test_single_substring(self):
        self.assertEqual(how_many_times('aaa', 'a'), 3)

    def test_overlapping_substring(self):
        self.assertEqual(how_many_times('aaaa', 'aa'), 3)

if __name__ == '__main__':
    unittest.main()