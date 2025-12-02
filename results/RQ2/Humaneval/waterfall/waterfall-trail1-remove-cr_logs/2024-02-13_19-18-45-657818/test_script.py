def fib4(n: int):
    if not isinstance(n, int) or n < 0:
        return "Invalid Input"
    
    fib_sequence = [0, 0, 2, 0]
    for i in range(4, n+1):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2] + fib_sequence[i-3] + fib_sequence[i-4])
    return fib_sequence[n]
import unittest

class Test(unittest.TestCase):
    def test_fib4(self):
        self.assertEqual(fib4(5), 4)
        self.assertEqual(fib4(6), 8)
        self.assertEqual(fib4(7), 14)

if __name__ == '__main__':
    unittest.main()