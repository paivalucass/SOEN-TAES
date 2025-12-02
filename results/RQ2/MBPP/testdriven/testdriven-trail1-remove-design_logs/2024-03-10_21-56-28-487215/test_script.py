def is_samepatterns(colors, patterns):
    if len(colors) != len(patterns):
        return False
    mapped_colors = {}
    for color, pattern in zip(colors, patterns):
        if color in mapped_colors:
            if mapped_colors[color] != pattern:
                return False
        else:
            if pattern in mapped_colors.values():
                return False
            mapped_colors[color] = pattern
    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_samepatterns(["red","green","green"], ["a", "b", "b"]), True)

if __name__ == '__main__':
    unittest.main()