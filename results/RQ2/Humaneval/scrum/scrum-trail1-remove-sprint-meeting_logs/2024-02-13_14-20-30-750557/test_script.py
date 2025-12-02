def tri(n):
    result = [0, 1, 1]
    for i in range(3, n + 1):
        if i % 2 == 0:
            next_trib = 1 + i // 2
        else:
            next_trib = result[i-1] + result[i-2] + result[i-3]
        result.append(next_trib)
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(tri(3), [0, 1, 1, 2])

if __name__ == '__main__':
    unittest.main()