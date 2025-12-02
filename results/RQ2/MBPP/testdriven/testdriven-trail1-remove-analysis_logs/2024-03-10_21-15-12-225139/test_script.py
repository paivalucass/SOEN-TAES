def volume_cylinder(r, h):
    """
    Calculate the volume of a cylinder.

    Args:
    r (float): the radius of the cylinder
    h (float): the height of the cylinder

    Returns:
    float: the volume of the cylinder

    Raises:
    ValueError: if either r or h are negative values
    """
    if r < 0 or h < 0:
        raise ValueError("Radius and height must be positive values.")

    # Calculate the volume using the formula V = πr^2h
    volume = math.pi * (r ** 2) * h

    # Assertion to validate the correctness of the calculated volume
    expected_volume = math.pi * (r ** 2) * h
    assert math.isclose(volume, expected_volume, rel_tol=1e-9), "Calculated volume does not match the expected value within the specified relative tolerance."

    return volume
import math
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(math.isclose(volume_cylinder(10,5), 1570.7500000000002, rel_tol=0.001))

if __name__ == '__main__':
    unittest.main()