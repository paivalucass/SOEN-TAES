def move_one_ball(arr):
    if len(arr) == 0:
        return True
    sorted_arr = sorted(arr)
    for i in range(len(arr)):
        if arr == sorted_arr:
            return True
        arr = [arr[-1]] + arr[:-1]
    return False
import unittest

class Test(unittest.TestCase):
    def test_move_one_ball(self):
        self.assertEqual(move_one_ball([3, 4, 5, 1, 2]), True)
        self.assertEqual(move_one_ball([3, 5, 4, 1, 2]), False)

if __name__ == '__main__':
    unittest.main()