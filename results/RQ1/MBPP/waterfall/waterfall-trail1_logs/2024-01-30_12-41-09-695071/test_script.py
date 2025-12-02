def next_power_of_2(n):
    if n <= 0:
        return 1  # Return 1 for edge case of input being 0 or negative

    power = 1
    while power < n:  # Finding the smallest power of 2
        power <<= 1  # Using bitwise shift operation to find the next power of 2

    return power

# Ensure the code passes all the provided test cases
assert next_power_of_2(0) == 1
assert next_power_of_2(5) == 8
assert next_power_of_2(100) == 128
assert next_power_of_2(-5) == 1
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(next_power_of_2(0), 1)

if __name__ == '__main__':
    unittest.main()