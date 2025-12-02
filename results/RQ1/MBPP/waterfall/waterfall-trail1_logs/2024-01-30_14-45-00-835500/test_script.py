def polar_rect(radius, angle):
    import math
    if radius < 0 or angle < 0 or angle > 2*math.pi:
        raise ValueError("Invalid input: radius cannot be negative or zero, and angle must be within the range [0, 2*pi]")

    x_coord = radius * math.cos(angle)
    y_coord = radius * math.sin(angle)
    rect_coord = (round(x_coord, 15), round(y_coord, 15))

    # Convert to complex number
    complex_coord = complex(round(x_coord, 15), round(y_coord, 15))

    return rect_coord, complex_coord
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(polar_rect(3, 4), ((5.0, 0.9272952180016122), (-2+2.4492935982947064e-16j)))

if __name__ == '__main__':
    unittest.main()