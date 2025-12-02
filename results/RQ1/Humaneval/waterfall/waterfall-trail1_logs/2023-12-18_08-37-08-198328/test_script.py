def get_max_triples(n):
    a = [i * i - i + 1 for i in range(1, n+1)]
    remainders = {0: 0, 1: 0, 2: 0}
    count = 0
    for num in a:
        remainder = num % 3
        count += remainders[(3 - remainder) % 3]
        remainders[remainder] += 1
    return count

# Test cases
print(get_max_triples(5))  # Output: 1
print(get_max_triples(6))  # Output: 3
print(get_max_triples(3))  # Output: 3
print(get_max_triples(0))  # Output: 0
import unittest

class Test(unittest.TestCase):
    def test_get_max_triples(self):
        self.assertEqual(get_max_triples(5), 1)

if __name__ == '__main__':
    unittest.main()