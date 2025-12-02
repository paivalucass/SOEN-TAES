def recursive_list_sum(data_list):
    if not isinstance(data_list, list):
        return 0
    total = 0
    for i in data_list:
        if isinstance(i, list):
            total += recursive_list_sum(i)
        else:
            total += i
    return total
import unittest

class Test(unittest.TestCase):
    def test_recursive_list_sum(self):
        self.assertEqual(recursive_list_sum([1, 2, [3,4],[5,6]]), 21)

if __name__ == '__main__':
    unittest.main()