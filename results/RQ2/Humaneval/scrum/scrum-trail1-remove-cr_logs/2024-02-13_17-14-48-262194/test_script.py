def tri(n):
    res = [0, 1, 1]
    for i in range(3, n + 1):
        if i % 2 == 0:
            res.append(res[i-1] + res[i-2] + res[i-3])
        else:
            res.append(res[i-1] + res[i-2] + res[i-3])
    return res
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(tri(0), [])
        self.assertEqual(tri(1), [0, 1])
        self.assertEqual(tri(2), [0, 1, 1])
        self.assertEqual(tri(3), [0, 1, 1, 2])
        self.assertEqual(tri(4), [0, 1, 1, 2, 4])
        self.assertEqual(tri(5), [0, 1, 1, 2, 4, 7])

if __name__ == '__main__':
    unittest.main()