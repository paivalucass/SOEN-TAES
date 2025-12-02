def find_Volume(length, base, height):
    """
    Calculate the volume of a triangular prism

    Args:
        length (float): length of the triangular prism
        base (float): base of the triangular prism
        height (float): height of the triangular prism

    Returns:
        float: volume of the triangular prism
    """
    if not all(isinstance(i, (int, float)) for i in [length, base, height]) or length <= 0 or base <= 0 or height <= 0:
        return 'Invalid input'

    volume = (1/2) * base * height * length
    return volume
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Volume(10, 8, 6), 240)

if __name__ == '__main__':
    unittest.main()