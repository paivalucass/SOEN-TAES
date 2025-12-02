def volume_sphere(r):
    if not isinstance(r, (int, float)):
        return "Error: Non-numeric input"
    if r < 0:
        return "Error: Negative radius value"
    if r == 0:
        return 0.0
    if r > 1000000:
        return "Error: Maximum radius value exceeded"
    if not isinstance(r, int):
        return "Error: Non-integer radius value"
    if isinstance(r, str):
        return "Error: Invalid input format"
    return (4/3) * math.pi * r**3

import math

# Test cases
print(volume_sphere(3))  # Output: 113.09733552923255
print(volume_sphere(0))  # Output: 0.0
assert math.isclose(volume_sphere(10), 4188.790204786391, rel_tol=0.001)
import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(math.isclose(volume_sphere(10), 4188.790204786391, rel_tol=0.001))

if __name__ == '__main__':
    unittest.main()