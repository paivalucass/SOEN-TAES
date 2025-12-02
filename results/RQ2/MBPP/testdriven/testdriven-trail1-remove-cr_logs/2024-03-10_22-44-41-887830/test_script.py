def count_Pairs(arr, n):
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] != arr[j]:
                count += 1
    return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_Pairs([1,2,1], 3), 2)

if __name__ == '__main__':
    unittest.main()