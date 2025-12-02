def find_Volume(length, base, height):
    """
    Calculate the volume of a triangular prism.

    Args:
    length (float): The length of the triangular prism.
    base (float): The base of the triangular prism.
    height (float): The height of the triangular prism.

    Returns:
    float: The volume of the triangular prism.
    """
    if not all(isinstance(param, (int, float)) for param in [length, base, height]):
        raise TypeError("Input parameters must be numeric")

    if length <= 0 or base <= 0 or height <= 0:
        raise ValueError("Input parameters must be positive numbers")

    volume = (1/2) * length * base * height

    return volume
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Volume(10, 8, 6), 240)

if __name__ == '__main__':
    unittest.main()