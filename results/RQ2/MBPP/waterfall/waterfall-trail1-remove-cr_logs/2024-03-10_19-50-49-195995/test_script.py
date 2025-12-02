def recursive_list_sum(data_list):
    def flatten_list(input_list):
        flattened_list = []
        for i in input_list:
            if isinstance(i, list):
                flattened_list.extend(flatten_list(i))
            else:
                flattened_list.append(i)
        return flattened_list
    
    try:
        flattened_data = flatten_list(data_list)
        return sum(flattened_data)
    except:
        return "Invalid input or empty list"
import unittest

class Test(unittest.TestCase):
    def test_recursive_list_sum(self):
        self.assertEqual(recursive_list_sum([1, 2, [3,4],[5,6]]), 21)

if __name__ == '__main__':
    unittest.main()