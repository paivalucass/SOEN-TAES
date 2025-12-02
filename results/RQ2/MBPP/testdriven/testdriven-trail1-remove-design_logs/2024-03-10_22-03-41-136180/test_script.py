def rear_extract(test_list):
    if not test_list:
        return []
    
    rear_elements = []
    for item in test_list:
        if isinstance(item, tuple):
            rear_elements.append(item[-1])
        else:
            return "Error: Input should be a list of tuples"
    return rear_elements
import unittest

class Test(unittest.TestCase):
    def test_rear_extract(self):
        self.assertEqual(rear_extract([(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]), [21, 20, 19])

if __name__ == '__main__':
    unittest.main()