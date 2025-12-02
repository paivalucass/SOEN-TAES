def how_many_times(string: str, substring: str) -> int:
    if not string or not substring:
        return 0
    
    if not isinstance(string, str) or not isinstance(substring, str):
        raise TypeError("string and substring must be of type str")
    
    count = 0
    start = 0
    while True:
        start = string.find(substring, start)  # Find the next occurrence of substring
        if start == -1:
            break
        count += 1
        start += 1  # Move start index to search for overlapping cases
    
    return count
import unittest

class Test(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(how_many_times('', 'a'), 0)

    def test_non_overlapping_substring(self):
        self.assertEqual(how_many_times('aaa', 'a'), 3)

    def test_overlapping_substring(self):
        self.assertEqual(how_many_times('aaaa', 'aa'), 3)

if __name__ == '__main__':
    unittest.main()