def get_max_triples(n):
    a = [i * i - i + 1 for i in range(1, n+1)]

    def calculate_sum_modulo_3(arr):
        return sum(arr) % 3

    count = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    count += 1
    return count

# Test cases
print(get_max_triples(5)) # Output: 1
# Add more test cases for different scenarios and performance testing with larger input sizes.
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_max_triples(5), 1)

if __name__ == '__main__':
    unittest.main()