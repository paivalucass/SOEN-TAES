def is_samepatterns(colors, patterns):
    if len(colors) != len(patterns):
        return False
    pattern_map = {}
    color_map = {}
    for color, pattern in zip(colors, patterns):
        if color not in color_map:
            color_map[color] = pattern
        if pattern not in pattern_map:
            pattern_map[pattern] = color
        if color_map[color] != pattern or pattern_map[pattern] != color:
            return False
    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_samepatterns(["red","green","green"], ["a", "b", "b"]), True)

if __name__ == '__main__':
    unittest.main()