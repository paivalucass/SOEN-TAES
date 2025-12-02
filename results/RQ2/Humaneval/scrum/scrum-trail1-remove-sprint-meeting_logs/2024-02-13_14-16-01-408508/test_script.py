def move_one_ball(arr):
    if not arr:
        return True
    sorted_arr = sorted(arr)
    n = len(arr)
    for i in range(n):
        if arr == sorted_arr:
            return True
        last_element = arr.pop()
        arr.insert(0, last_element)
    return False
import unittest

class Test(unittest.TestCase):
    def test_move_one_ball(self):
        self.assertEqual(move_one_ball([3, 4, 5, 1, 2]), True)
        self.assertEqual(move_one_ball([3, 5, 4, 1, 2]), False)

if __name__ == '__main__':
    unittest.main()