def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_fib(n: int):
    if n < 1 or type(n) != int:
        return "Invalid input"
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        fib_sequence = [2, 3]
        i = 2
        while len(fib_sequence) < n:
            next_fib = fib_sequence[i-1] + fib_sequence[i-2]
            while not is_prime(next_fib):
                next_fib = fib_sequence[i-1] + fib_sequence[i-2]
                fib_sequence.append(next_fib)
                i += 1
        return fib_sequence[n-1]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(prime_fib(1), 2)
        self.assertEqual(prime_fib(2), 3)
        self.assertEqual(prime_fib(3), 5)
        self.assertEqual(prime_fib(4), 13)
        self.assertEqual(prime_fib(5), 89)

if __name__ == '__main__':
    unittest.main()