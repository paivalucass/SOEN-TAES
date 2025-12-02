def count_pairs(arr, n):
    count = 0
    frequency_map = {}
    for i in arr:
        if i in frequency_map:
            frequency_map[i] += 1
        else:
            frequency_map[i] = 1
    for key in frequency_map:
        count += (frequency_map[key] * (frequency_map[key] - 1))
    return count // 2
import unittest

class Test(unittest.TestCase):
    def test_count_Pairs(self):
        self.assertEqual(count_Pairs([1,2,1], 3), 2)

if __name__ == '__main__':
    unittest.main()