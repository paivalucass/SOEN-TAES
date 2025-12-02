def pluck(arr):
    min_even_value = float('inf')
    min_even_index = -1
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            if arr[i] < min_even_value:
                min_even_value = arr[i]
                min_even_index = i
    if min_even_index == -1:
        return []
    return [min_even_value, min_even_index]
import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(pluck([4,2,3]), [2, 1])

    def test2(self):
        self.assertEqual(pluck([1,2,3]), [2, 1])

    def test3(self):
        self.assertEqual(pluck([]), [])

    def test4(self):
        self.assertEqual(pluck([5, 0, 3, 0, 4, 2]), [0, 1])

if __name__ == '__main__':
    unittest.main()