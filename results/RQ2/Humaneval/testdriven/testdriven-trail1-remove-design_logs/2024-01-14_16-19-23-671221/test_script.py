def common(l1: list, l2: list):
    count = {}
    result = []
    for num in l1:
        count[num] = count.get(num, 0) + 1
    for num in l2:
        if num in count and count[num] > 0:
            result.append(num)
            count[num] -= 1
    return sorted(result)
import unittest

class Test(unittest.TestCase):
    def test_common_elements(self):
        self.assertEqual(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]), [1, 5, 653])
        self.assertEqual(common([5, 3, 2, 8], [3, 2]), [2, 3])

if __name__ == '__main__':
    unittest.main()