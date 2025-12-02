def surfacearea_sphere(r):
    import math
    if isinstance(r, (int, float)) and r > 0:
        return 4 * math.pi * (r ** 2)
    else:
        return "Invalid input. Please enter a positive number."

# Rewrite your code below:
# Ensure that the code is efficient, readable, and follows best practices. Remember not to explain the code you wrote.
import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(math.isclose(surfacearea_sphere(10), 1256.6370614359173, rel_tol=0.001))

if __name__ == '__main__':
    unittest.main()