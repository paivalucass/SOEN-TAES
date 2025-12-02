def recursive_list_sum(data_list):
    if not data_list:
        return 0
    if isinstance(data_list[0], list):
        return recursive_list_sum(data_list[0]) + recursive_list_sum(data_list[1:])
    return data_list[0] + recursive_list_sum(data_list[1:])
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(recursive_list_sum([1, 2, [3, 4], [5, 6]]), 21)

if __name__ == '__main__':
    unittest.main()