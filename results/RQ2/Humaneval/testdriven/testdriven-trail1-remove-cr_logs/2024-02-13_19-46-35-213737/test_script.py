def pluck(arr):
    smallest_even = float('inf')
    smallest_even_index = -1
    for i in range(len(arr)):
        if arr[i] % 2 == 0 and arr[i] < smallest_even:
            smallest_even = arr[i]
            smallest_even_index = i
    if smallest_even_index == -1:
        return []
    else:
        return [smallest_even, smallest_even_index]

import unittest

class Test(unittest.TestCase):
    def test_pluck(self):
        self.assertEqual(pluck([4,2,3]), [2, 1])
        self.assertEqual(pluck([1,2,3]), [2, 1])
        self.assertEqual(pluck([]), [])
        self.assertEqual(pluck([5, 0, 3, 0, 4, 2]), [0, 1])

if __name__ == '__main__':
    unittest.main()