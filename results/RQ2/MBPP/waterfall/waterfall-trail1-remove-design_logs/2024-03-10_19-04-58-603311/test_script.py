def is_samepatterns(colors, patterns):
    color_to_pattern = {}
    if len(colors) != len(patterns):
        return False
    for color, pattern in zip(colors, patterns):
        if color not in color_to_pattern:
            color_to_pattern[color] = pattern
        elif color_to_pattern[color] != pattern:
            return False
    return True
import unittest

class Test(unittest.TestCase):
    def test_is_samepatterns(self):
        self.assertEqual(is_samepatterns(["red","green","green"], ["a", "b", "b"]), True)

if __name__ == '__main__':
    unittest.main()