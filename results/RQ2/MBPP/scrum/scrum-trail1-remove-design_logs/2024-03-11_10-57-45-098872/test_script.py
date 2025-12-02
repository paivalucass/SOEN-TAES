def get_ludic(n):
    is_lucid = [True] * (n + 1)
    is_lucid[0:3] = [False, False, True]
    for i in range(2, n + 1):
        if is_lucid[i]:
            is_lucid[i*i:n+1:i] = [False] * ((n - i*i) // i + 1)
    return [i for i in range(n + 1) if is_lucid[i] and i % 2 != 0 and i > 1]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_ludic(10), [1, 2, 3, 5, 7])

if __name__ == '__main__':
    unittest.main()