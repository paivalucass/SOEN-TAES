def rgb_to_hsv(r, g, b):
    '''Convert rgb color to hsv color.'''
    if not all(0 <= x <= 255 for x in (r, g, b)):
        raise ValueError("RGB values should be in the range 0 to 255")

    r, g, b = r / 255.0, g / 255.0, b / 255.0
    cmax = max(r, g, b)
    cmin = min(r, g, b)
    delta = cmax - cmin

    if delta == 0:
        hue = 0
    elif cmax == r:
        hue = 60 * (((g - b) / delta) % 6)
    elif cmax == g:
        hue = 60 * (((b - r) / delta) + 2)
    else:
        hue = 60 * (((r - g) / delta) + 4)

    if cmax == 0:
        saturation = 0
    else:
        saturation = (delta / cmax) * 100

    value = cmax * 100

    return int(hue), round(saturation, 1), round(value, 1)  # return the HSV color values
import unittest

class Test(unittest.TestCase):
    def test_rgb_to_hsv_conversion(self):
        self.assertEqual(rgb_to_hsv(255, 255, 255), (0, 0.0, 100.0))

if __name__ == '__main__':
    unittest.main()