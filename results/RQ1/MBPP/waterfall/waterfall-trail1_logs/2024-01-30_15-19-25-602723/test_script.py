def find_length(binary_string):
    max_diff = 0
    count = 0
    count_map = {0: -1}

    for i in range(len(binary_string)):
        if binary_string[i] == '0':
            count -= 1
        else:
            count += 1
        
        if count in count_map:
            max_diff = max(max_diff, i - count_map[count])
        else:
            count_map[count] = i
    
    return max_diff

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_length('11000010001'), 6)

if __name__ == '__main__':
    unittest.main()