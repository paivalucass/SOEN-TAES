def count_bidirectional(test_list):
    if not isinstance(test_list, list) or not all(isinstance(t, tuple) for t in test_list):
        raise TypeError("Input must be a list of tuples")
    
    count_dict = {}
    bidirectional_count = 0
    
    for t in test_list:
        if len(t) != 2 or not all(isinstance(i, int) for i in t):
            raise ValueError("Each tuple in the input list must contain exactly 2 integers")
        
        if t in count_dict:
            bidirectional_count += 1
        elif (t[1], t[0]) in count_dict:
            bidirectional_count += 1
        
        count_dict[t] = count_dict.get(t, 0) + 1
    
    return bidirectional_count
import unittest

class Test(unittest.TestCase):
    def test_count_bidirectional(self):
        self.assertEqual(count_bidirectional([(5, 6), (1, 2), (6, 5), (9, 1), (6, 5), (2, 1)]), 3)

if __name__ == '__main__':
    unittest.main()