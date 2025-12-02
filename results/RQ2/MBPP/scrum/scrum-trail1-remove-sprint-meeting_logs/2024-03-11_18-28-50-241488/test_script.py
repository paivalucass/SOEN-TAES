def number_of_substrings(input_string):
    if not input_string:
        return 0
    
    count = 0
    for i in range(len(input_string)):
        for j in range(i+1, len(input_string)+1):
            substring = input_string[i:j]
            if substring:
                count += 1
    
    return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(number_of_substrings('abc'), 6)

if __name__ == '__main__':
    unittest.main()