def tri(n):
    sequence = [0] * (n+1)
    if n >= 0:
        sequence[0] = 0
    if n >= 1:
        sequence[1] = 1
    if n >= 2:
        sequence[2] = 1
    for i in range(3, n+1):
        if i % 2 == 0:
            sequence[i] = 1 + i // 2
        else:
            sequence[i] = sequence[i-1] + sequence[i-2] + sequence[i-3]
    return sequence
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(tri(3), [0, 1, 1, 3, 2, 8])

if __name__ == '__main__':
    unittest.main()