def tri(n):
    """Return a list of the tribonacci sequence up to the nth term."""
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    elif n == 0:
        return [3]
    elif n == 1:
        return [3, 1]

    tribonacci_sequence = [3, 1, 2]
    for i in range(3, n + 1):
        if i % 2 == 0:
            tribonacci_sequence.append(1 + i//2)
        else:
            tribonacci_sequence.append(tribonacci_sequence[-1] + tribonacci_sequence[-2] + tribonacci_sequence[-3])

    return tribonacci_sequence
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(tri(3), [1, 1, 1, 3])

if __name__ == '__main__':
    unittest.main()