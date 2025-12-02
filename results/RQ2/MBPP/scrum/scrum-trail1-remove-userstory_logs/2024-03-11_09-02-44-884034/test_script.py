def rear_extract(input_list):
    if input_list is None:
        return "Error: Input list is null"
    if not isinstance(input_list, list) or not all(isinstance(t, tuple) for t in input_list):
        return "Error: Invalid input list format"
    
    return [t[-1] for t in input_list]
import unittest

class Test(unittest.TestCase):
    def test_rear_extract(self):
        self.assertEqual(rear_extract([(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]), [21, 20, 19])

if __name__ == '__main__':
    unittest.main()