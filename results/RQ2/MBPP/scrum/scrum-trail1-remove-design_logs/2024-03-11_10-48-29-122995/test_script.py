def count_Pairs(arr, n):
    count_dict = {}
    for num in arr:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    pairs_count = 0
    for key in count_dict:
        pairs_count += count_dict[key] * (n - count_dict[key])

    return pairs_count // 2
import unittest

class Test(unittest.TestCase):
    def test_count_Pairs(self):
        self.assertEqual(count_Pairs([1,2,1], 3), 2)

if __name__ == '__main__':
    unittest.main()