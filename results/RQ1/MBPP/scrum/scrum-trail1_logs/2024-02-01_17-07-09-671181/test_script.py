def recursive_list_sum(data_list):
    def flatten_list(input_list):
        flat_list = []
        for i in input_list:
            if isinstance(i, list):
                flat_list.extend(flatten_list(i))
            else:
                if isinstance(i, int):
                    flat_list.append(i)
                else:
                    return "Error"
        return flat_list
    
    flattened = flatten_list(data_list)
    if "Error" in flattened:
        return "Error"
    else:
        sum_of_elements = sum(flattened)
        return sum_of_elements
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(recursive_list_sum([1, 2, [3,4],[5,6]]), 21)

if __name__ == '__main__':
    unittest.main()