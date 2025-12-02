def count_Pairs(arr, n):
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] != arr[j]:
                count += 1
    return count

# Test cases
assert count_Pairs([], 0) == 0
assert count_Pairs([1], 1) == 0
assert count_Pairs([1, 2, 3, 4, 5], 5) == 10
assert count_Pairs([1, 1, 1, 1, 1], 5) == 0
assert count_Pairs([1, 2, 1], 3) == 2
import unittest

class Test(unittest.TestCase):
    def test_count_Pairs(self):
        self.assertEqual(count_Pairs([1,2,1],3), 2)

if __name__ == '__main__':
    unittest.main()