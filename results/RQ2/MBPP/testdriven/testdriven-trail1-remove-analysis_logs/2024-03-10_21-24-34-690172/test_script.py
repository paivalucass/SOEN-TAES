def get_ludic(n):
    result = []
    for i in range(1, n+1):
        if i == 1 or (i & (i-1)) == 0:
            result.append(i)
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_ludic(10), [1, 2, 3, 5, 7])

if __name__ == '__main__':
    unittest.main()