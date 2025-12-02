def rear_extract(test_list):
    result = []
    for item in test_list:
        if isinstance(item, tuple):
            result.append(item[-1])
    return result
import unittest

class Test(unittest.TestCase):
    def test_rear_extract(self):
        self.assertEqual(rear_extract([(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]), [21, 20, 19])

if __name__ == '__main__':
    unittest.main()