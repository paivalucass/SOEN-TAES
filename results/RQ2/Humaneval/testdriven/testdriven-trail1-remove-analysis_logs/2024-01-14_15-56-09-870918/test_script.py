def move_one_ball(arr):
    if not isinstance(arr, list) or len(arr) == 0:
        return True
    
    sorted_arr = sorted(arr)
    n = len(arr)
    min_index = arr.index(min(arr))
    return arr == sorted_arr or min_index <= n // 2 or min_index == 0
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(move_one_ball([3, 4, 5, 1, 2]), True)
        self.assertEqual(move_one_ball([3, 5, 4, 1, 2]), False)

if __name__ == '__main__':
    unittest.main()