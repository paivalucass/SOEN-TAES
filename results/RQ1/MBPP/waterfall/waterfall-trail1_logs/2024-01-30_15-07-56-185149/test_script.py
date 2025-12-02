def get_pairs_count(arr, target_sum):
    pairs_count = 0
    num_dict = {}
    for num in arr:
        complement = target_sum - num
        if complement in num_dict:
            pairs_count += num_dict[complement]
        if num in num_dict:
            num_dict[num] += 1
        else:
            num_dict[num] = 1
    return pairs_count
import unittest

class Test(unittest.TestCase):
    def test_get_pairs_count(self):
        self.assertEqual(get_pairs_count([1,1,1,1], 2), 6)

if __name__ == '__main__':
    unittest.main()