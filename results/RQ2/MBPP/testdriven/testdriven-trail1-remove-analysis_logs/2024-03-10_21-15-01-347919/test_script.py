def rear_extract(test_list):
    if not test_list or not all(isinstance(x, tuple) for x in test_list):
        return []

    result = [x[-1] for x in test_list]
    return result
import unittest

class Test(unittest.TestCase):
    def test_rear_extract(self):
        self.assertEqual(rear_extract([(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]), [21, 20, 19])

if __name__ == '__main__':
    unittest.main()