def rgb_to_hsv(r, g, b):
    '''Convert RGB color to HSV color.'''
    r, g, b = r / 255.0, g / 255.0, b / 255.0
    cmax = max(r, g, b)
    cmin = min(r, g, b)
    delta = cmax - cmin
    if cmax == cmin:
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
    return round(h), round(s, 1), round(v, 1)

import unittest

class Test(unittest.TestCase):
    def test_rgb_to_hsv(self):
        self.assertEqual(rgb_to_hsv(255, 255, 255), (0, 0.0, 100.0))

if __name__ == '__main__':
    unittest.main()