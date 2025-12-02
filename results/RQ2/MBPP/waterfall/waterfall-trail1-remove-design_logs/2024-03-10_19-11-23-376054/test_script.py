def rear_extract(test_list):
    if not test_list:
        return []
    if not all(isinstance(item, tuple) for item in test_list):
        return "Error: Invalid Input"
    return [t[-1] for t in test_list]
import unittest

class Test(unittest.TestCase):
    def test_rear_extract(self):
        self.assertEqual(rear_extract([(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]), [21, 20, 19])

if __name__ == '__main__':
    unittest.main()