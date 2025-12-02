def tri(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    else:
        sequence = [0, 1, 1]
        for i in range(3, n + 1):
            next_number = sum(sequence[-3:])
            sequence.append(next_number)
        return sequence
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(tri(3), [0, 1, 1, 2])

if __name__ == '__main__':
    unittest.main()