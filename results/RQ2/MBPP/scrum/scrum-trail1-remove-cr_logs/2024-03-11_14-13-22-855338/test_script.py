def get_median(arr1, arr2, n):
    combined_list = sorted(arr1 + arr2)
    if len(combined_list) % 2 != 0:
        median_index = len(combined_list) // 2
        return float(combined_list[median_index])
    else:
        median_index_1 = len(combined_list) // 2 - 1
        median_index_2 = len(combined_list) // 2
        return (combined_list[median_index_1] + combined_list[median_index_2]) / 2.0
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5), 16.0)

if __name__ == '__main__':
    unittest.main()