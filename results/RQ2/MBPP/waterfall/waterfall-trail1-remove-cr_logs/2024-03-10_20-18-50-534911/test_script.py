def rgb_to_hsv(r, g, b):
    max_color = max(r, g, b)
    min_color = min(r, g, b)
    delta = max_color - min_color
    if delta == 0:
        h = 0
    elif max_color == r:
        h = 60 * (((g - b) / delta) % 6)
    elif max_color == g:
        h = 60 * (((b - r) / delta) + 2)
    else:
        h = 60 * (((r - g) / delta) + 4)
    if max_color == 0:
        s = 0
    else:
        s = (delta / max_color) * 100
    v = (max_color / 255) * 100
    return (round(h), round(s, 1), round(v, 1))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(rgb_to_hsv(255, 255, 255), (0, 0.0, 100.0))

if __name__ == '__main__':
    unittest.main()