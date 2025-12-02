def rgb_to_hsv(r, g, b):
    if r < 0 or r > 255 or g < 0 or g > 255 or b < 0 or b > 255:
        raise ValueError("RGB values should be between 0 and 255")

    r, g, b = r / 255.0, g / 255.0, b / 255.0
    cmax = max(r, g, b)
    cmin = min(r, g, b)
    delta = cmax - cmin

    if delta == 0:
        h = 0
    elif cmax == r:
        h = 60 * (((g - b) / delta) % 6)
    elif cmax == g:
        h = 60 * (((b - r) / delta) + 2)
    elif cmax == b:
        h = 60 * (((r - g) / delta) + 4)

    if cmax == 0:
        s = 0
    else:
        s = (delta / cmax) * 100

    v = cmax * 100

    return int(h), round(s, 1), round(v, 1)
import unittest

class Test(unittest.TestCase):
    def test_rgb_to_hsv_conversion(self):
        self.assertEqual(rgb_to_hsv(255, 255, 255), (0, 0.0, 100.0))

if __name__ == '__main__':
    unittest.main()