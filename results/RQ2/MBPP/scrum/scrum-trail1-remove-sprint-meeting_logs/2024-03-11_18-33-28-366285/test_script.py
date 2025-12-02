def rear_extract(test_list):
    result = []
    
    if not all(isinstance(item, tuple) for item in test_list):
        raise ValueError("Input is not a list of tuples")
    
    if len(test_list) == 0:
        return result
    
    tuple_length = len(test_list[0])
    
    for tpl in test_list:
        if len(tpl) != tuple_length:
            raise ValueError("Tuples have different lengths")
    
    for tpl in test_list:
        result.append(tpl[-1])
    
    return result
import unittest

class Test(unittest.TestCase):
    def test_rear_extract(self):
        self.assertEqual(rear_extract([(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]), [21, 20, 19])

if __name__ == '__main__':
    unittest.main()