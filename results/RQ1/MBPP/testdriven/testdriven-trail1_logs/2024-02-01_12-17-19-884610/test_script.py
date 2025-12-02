def number_of_substrings(input_str):
    if input_str == "":
        raise ValueError("Input string cannot be empty")
    
    count = 0
    for i in range(len(input_str)):
        for j in range(i+1, len(input_str)+1):
            if input_str[i:j] != "":
                count += 1
    return count
# Rewrite your code here

def number_of_substrings(input_str):
    if input_str == "":
        raise ValueError("Input string cannot be empty")
    
    count = 0
    for i in range(len(input_str)):
        for j in range(i+1, len(input_str)+1):
            if input_str[i:j] != "":
                count += 1
    return count

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(number_of_substrings('abc'), 6)

if __name__ == '__main__':
    unittest.main()