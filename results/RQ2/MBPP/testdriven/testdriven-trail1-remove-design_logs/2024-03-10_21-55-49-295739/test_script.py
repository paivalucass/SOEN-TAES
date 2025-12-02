def count_substrings(s):
    '''Write a python function to count the number of substrings with the sum of digits equal to their length.'''
    
    if not s.isdigit():
        return "Invalid input"
    
    count = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            substring = s[i:j]
            if sum(int(digit) for digit in substring) == len(substring):
                count += 1
    return str(count)
import unittest

class Test(unittest.TestCase):
    def test_count_Substrings(self):
        self.assertEqual(count_Substrings('112112'), 6)

if __name__ == '__main__':
    unittest.main()