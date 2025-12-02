def get_pairs_count(arr, sum):
    pairs = 0
    num_dict = {}
    for num in arr:
        if num in num_dict:
            pairs += num_dict[num]
        complement = sum - num
        if complement in num_dict:
            num_dict[complement] += 1
        else:
            num_dict[complement] = 1
    return pairs

assert get_pairs_count([1,2,3,4], 5) == 2
assert get_pairs_count([-1,-2,-3,-4], -5) == 2
assert get_pairs_count([0,0,0,0], 0) == 6
assert get_pairs_count([], 5) == 0
assert get_pairs_count([5], 5) == 0
assert get_pairs_count([1,2,3,4], 6) == 1
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_pairs_count([1,1,1,1], 2), 6)

if __name__ == '__main__':
    unittest.main()