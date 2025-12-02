def count_Pairs(arr, n):
    if not isinstance(arr, list) or not all(isinstance(x, int) for x in arr):
        return "Error: Input is not a list of integers"

    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    count = 0
    for key in freq:
        count += (freq[key] * (freq[key] - 1)) // 2

    return count
import unittest

class Test(unittest.TestCase):
    def test_count_Pairs(self):
        self.assertEqual(count_Pairs([1,2,1],3), 2)

if __name__ == '__main__':
    unittest.main()