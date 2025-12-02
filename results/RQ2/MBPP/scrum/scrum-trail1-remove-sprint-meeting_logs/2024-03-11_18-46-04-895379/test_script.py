def count_bidirectional(input_list):
    reverse_dict = {}
    bidirectional_count = 0
    
    for tup in input_list:
        reverse_tup = (tup[1], tup[0])
        if reverse_tup in reverse_dict:
            bidirectional_count += 1
        reverse_dict[tup] = reverse_tup
    
    return bidirectional_count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_bidirectional([(5, 6), (1, 2), (6, 5), (9, 1), (6, 5), (2, 1)]), 3)

if __name__ == '__main__':
    unittest.main()