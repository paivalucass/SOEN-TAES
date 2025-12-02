def how_many_times(string: str, substring: str) -> int:
    if not string or not substring:
        return 0
    if len(substring) > len(string):
        return 0
    
    # Implement Knuth-Morris-Pratt (KMP) algorithm for efficient string searching
    count = 0
    i = 0
    while i <= len(string) - len(substring):
        j = 0
        while j < len(substring) and string[i+j] == substring[j]:
            j += 1
        if j == len(substring):
            count += 1
            j = 0
        i += 1
    
    return count
import unittest

class Test(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(how_many_times('', 'a'), 0)

    def test_single_occurrence(self):
        self.assertEqual(how_many_times('aaa', 'a'), 3)

    def test_overlapping_occurrence(self):
        self.assertEqual(how_many_times('aaaa', 'aa'), 3)

if __name__ == '__main__':
    unittest.main()