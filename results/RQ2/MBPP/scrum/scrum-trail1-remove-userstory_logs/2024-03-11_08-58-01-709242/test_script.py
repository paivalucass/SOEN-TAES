def frequency(a, x):
    count = 0
    if not a:
        return 0
    for num in a:
        if num == x:
            count += 1
    return count

# Test cases
print(frequency([1, 2, 3], 4))  # Expected output: 0
print(frequency([], 1))  # Expected output: 0
print(frequency([1, 2, 2, 3, 4, 2], 2))  # Expected output: 3
print(frequency([1.5, 2.5, 3.5, 1.5, 2.5], 1.5))  # Expected output: 2
print(frequency([-1, 2, -1, 3, -1, 4, 5], -1))  # Expected output: 3
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(frequency([1, 2, 3], 4), 0)

if __name__ == '__main__':
    unittest.main()