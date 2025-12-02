def empty_list(length):
    dict_list = []
    if length <= 0:
        raise ValueError("Length should be a positive integer")
    for _ in range(length):
        dict_list.append({})
    return dict_list
import unittest

class Test(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(empty_list(5), [{},{},{},{},{}])

if __name__ == '__main__':
    unittest.main()