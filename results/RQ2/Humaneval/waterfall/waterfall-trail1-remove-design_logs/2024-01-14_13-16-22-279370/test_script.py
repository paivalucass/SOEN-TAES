def move_one_ball(arr):
    if len(arr) == 0:
        return True
    else:
        n = len(arr)
        for i in range(n):
            is_sorted = True
            for j in range(n - 1 - i):
                if arr[j] > arr[j + 1]:
                    return False
        return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(move_one_ball([3, 4, 5, 1, 2]), True)
        self.assertEqual(move_one_ball([3, 5, 4, 1, 2]), False)

if __name__ == '__main__':
    unittest.main()