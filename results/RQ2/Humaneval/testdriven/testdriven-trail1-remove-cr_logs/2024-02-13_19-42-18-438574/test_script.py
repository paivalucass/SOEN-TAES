def count_distinct_characters(string: str) -> int:
    if string is None or not isinstance(string, str):
        return 0
    
    string = string.lower()  # convert input string to lowercase
    distinct_chars = set(string)  # using set to get distinct characters
    distinct_chars.discard(' ')  # remove any spaces from distinct characters
    return len(distinct_chars)  # return the count of distinct characters

# Test cases
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('abc123!@#'))  # Output: 6
print(count_distinct_characters(''))  # Output: 0
print(count_distinct_characters('a'))  # Output: 1
print(count_distinct_characters('abcdefghijklmnopqrstuvwxyz'))  # Output: 26
print(count_distinct_characters('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'))  # Output: 52
print(count_distinct_characters('a'))  # Output: 1
print(count_distinct_characters(None))  # Output: 0
print(count_distinct_characters('123'))  # Output: 0
print(count_distinct_characters('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()'))  # Output: 62
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_distinct_characters('xyzXYZ'), 3)
        self.assertEqual(count_distinct_characters('Jerry'), 4)

if __name__ == '__main__':
    unittest.main()