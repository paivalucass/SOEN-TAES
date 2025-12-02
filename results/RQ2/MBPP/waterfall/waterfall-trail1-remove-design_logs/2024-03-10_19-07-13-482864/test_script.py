def find_max_difference(string):
    max_diff = 0
    count_0 = 0
    count_1 = 0
    
    for char in string:
        if char not in ['0', '1']:
            return "Invalid Input"
        
        if char == "0":
            count_0 += 1
        else:  # char == "1"
            count_1 += 1
        
        diff = count_0 - count_1

        if diff > max_diff:
            max_diff = diff

    return max_diff

import unittest

class Test(unittest.TestCase):
    def test_find_length(self):
        self.assertEqual(find_length('11000010001'), 6)

if __name__ == '__main__':
    unittest.main()