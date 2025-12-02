def how_many_times(string: str, substring: str) -> int:
    count = 0
    if len(substring) == 0:
        return 0
    for i in range(len(string)):
        if string[i:i+len(substring)] == substring:
            count += 1
    return count
import unittest

class Test(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(how_many_times('', 'a'), 0)
    
    def test_single_character_substring(self):
        self.assertEqual(how_many_times('aaa', 'a'), 3)
        
    def test_multiple_character_substring(self):
        self.assertEqual(how_many_times('aaaa', 'aa'), 3)

if __name__ == '__main__':
    unittest.main()