import math

def volume_sphere(r: float) -> float:
    """
    Calculate the volume of a sphere given its radius.

    Args:
    r (float): The radius of the sphere.

    Returns:
    float: The volume of the sphere.

    Raises:
    ValueError: If the input 'r' is not a positive number.
    """
    if r <= 0:
        raise ValueError("Radius 'r' must be a positive number.")

    volume = (4/3) * math.pi * (r**3)
    return volume

# Example usage
assert math.isclose(volume_sphere(10), 4188.790204786391, rel_tol=0.001)

import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(math.isclose(volume_sphere(10), 4188.790204786391, rel_tol=0.001))

if __name__ == '__main__':
    unittest.main()