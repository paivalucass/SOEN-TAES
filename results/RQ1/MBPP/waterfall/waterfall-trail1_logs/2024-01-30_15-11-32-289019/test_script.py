def rgb_to_hsv(r, g, b):
    '''Convert rgb color to hsv color'''
    if r < 0 or g < 0 or b < 0 or r > 255 or g > 255 or b > 255:
        raise ValueError("Invalid RGB color values")

    r, g, b = r / 255.0, g / 255.0, b / 255.0
    cmax = max(r, g, b)
    cmin = min(r, g, b)
    delta = cmax - cmin

    if delta == 0:
        h = 0
    elif cmax == r:
        h = (60 * ((g - b) / delta) + 360) % 360
    elif cmax == g:
        h = (60 * ((b - r) / delta) + 120) % 360
    else:
        h = (60 * ((r - g) / delta) + 240) % 360

    if cmax == 0:
        s = 0
    else:
        s = (delta / cmax) * 100

    v = cmax * 100

    return int(h), round(s, 1), round(v, 1)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(rgb_to_hsv(255, 255, 255), (0, 0.0, 100.0))

if __name__ == '__main__':
    unittest.main()