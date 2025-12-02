def move_one_ball(arr):
    if not arr:
        return True
    sorted_arr = sorted(arr)
    n = len(arr)
    for i in range(n):
        if arr == sorted_arr:
            return True
        arr = [arr[-1]] + arr[:-1]  # right shift operation
    return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(move_one_ball([3, 4, 5, 1, 2]), True)
        self.assertEqual(move_one_ball([3, 5, 4, 1, 2]), False)

if __name__ == '__main__':
    unittest.main()