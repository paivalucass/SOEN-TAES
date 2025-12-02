def move_one_ball(arr):
    if not arr:
        return True
    sorted_arr = sorted(arr)
    n = len(arr)
    for i in range(n):
        if arr == sorted_arr:
            return True
        arr = [arr[n-1]] + arr[:n-1]
    return False
import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(move_one_ball([3, 4, 5, 1, 2]), True)

    def test2(self):
        self.assertEqual(move_one_ball([3, 5, 4, 1, 2]), False)

if __name__ == '__main__':
    unittest.main()