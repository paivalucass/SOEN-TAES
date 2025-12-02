def sum_range_list(input_list, start_index, end_index):
    if not isinstance(input_list, list) or not all(isinstance(i, int) for i in [start_index, end_index]):
        return "Invalid input"
    
    if start_index < 0 or end_index < 0:
        return 0
    
    if start_index >= len(input_list) or end_index >= len(input_list):
        return 0
    
    return sum(input_list[start_index:end_index+1])
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 8, 10), 29)

if __name__ == '__main__':
    unittest.main()