def fib4(n: int):
    if n < 4:
        raise ValueError("Input n must be greater than or equal to 4")
    
    fib4_values = [0, 0, 2, 0]
    
    for i in range(4, n+1):
        fib4_values.append(fib4_values[i-1] + fib4_values[i-2] + fib4_values[i-3] + fib4_values[i-4])
    
    return fib4_values[n]
import unittest

class Test(unittest.TestCase):
    def test_fib4(self):
        self.assertEqual(fib4(5), 4)
        self.assertEqual(fib4(6), 8)
        self.assertEqual(fib4(7), 14)

if __name__ == '__main__':
    unittest.main()