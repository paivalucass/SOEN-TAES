def rear_extract(test_list):
    if not test_list:
        raise ValueError("Input list is empty")
    
    if not all(isinstance(t, tuple) for t in test_list):
        raise TypeError("Input list should only contain tuples")
    
    rear_elements = [t[-1] for t in test_list]
    return rear_elements
import unittest

class Test(unittest.TestCase):
    def test_rear_extract(self):
        self.assertEqual(rear_extract([(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]), [21, 20, 19])

if __name__ == '__main__':
    unittest.main()