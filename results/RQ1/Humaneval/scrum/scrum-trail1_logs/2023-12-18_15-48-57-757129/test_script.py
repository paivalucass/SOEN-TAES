def tri(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    else:
        result = [0, 1, 1]
        for i in range(3, n+1):
            next_num = result[i-1] + result[i-2] + result[i-3]
            result.append(next_num)
        return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(tri(0), [0])
        self.assertEqual(tri(1), [1])
        self.assertEqual(tri(2), [1, 1])
        self.assertEqual(tri(3), [0, 1, 1, 2])
        self.assertEqual(tri(4), [0, 1, 1, 2, 4])
        self.assertEqual(tri(5), [0, 1, 1, 2, 4, 7])
        self.assertEqual(tri(6), [0, 1, 1, 2, 4, 7, 13])

if __name__ == '__main__':
    unittest.main()