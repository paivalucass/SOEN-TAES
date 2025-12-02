def count_Pairs(arr, n):
    if n < 2:
        return 0

    unique_pairs = set()

    for i in range(n):
        for j in range(i+1, n):
            if arr[i] != arr[j]:
                pair = tuple(sorted([arr[i], arr[j]]))
                unique_pairs.add(pair)

    return len(unique_pairs)
import unittest

class Test(unittest.TestCase):
    def test_count_pairs(self):
        self.assertEqual(count_Pairs([1,2,1], 3), 2)

if __name__ == '__main__':
    unittest.main()