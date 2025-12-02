def closest_num(N):
    if not isinstance(N, int):
        raise TypeError("Input must be an integer")

    low = 0
    high = N - 1
    closest = 0

    while low <= high:
        mid = (low + high) // 2
        if mid < N:
            closest = mid
            low = mid + 1
        else:
            high = mid - 1

    return closest
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(closest_num(11), 10)

if __name__ == '__main__':
    unittest.main()