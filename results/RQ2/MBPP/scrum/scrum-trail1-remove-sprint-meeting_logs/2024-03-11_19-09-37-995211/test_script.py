def get_pairs_count(arr, sum):
    if not arr or sum < 0:
        return 0

    num_dict = {}
    count = 0
    for num in arr:
        if sum - num in num_dict:
            count += num_dict[sum - num]
        if num in num_dict:
            num_dict[num] += 1
        else:
            num_dict[num] = 1
    return count
import unittest

class Test(unittest.TestCase):
    def test_get_pairs_count(self):
        self.assertEqual(get_pairs_count([1,1,1,1], 2), 6)

if __name__ == '__main__':
    unittest.main()