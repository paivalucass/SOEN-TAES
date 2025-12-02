def find_Volume(length, base, height):
    if length <= 0 or base <= 0 or height <= 0:
        raise ValueError("Dimensions must be positive.")

    if length + base <= height or length + height <= base or base + height <= length:
        raise ValueError("Invalid dimensions for a triangular prism.")

    volume = (1/2) * base * height * length

    return volume
import unittest

class Test(unittest.TestCase):
    def test_volume_of_triangular_prism(self):
        self.assertEqual(find_Volume(10, 8, 6), 240)

if __name__ == '__main__':
    unittest.main()