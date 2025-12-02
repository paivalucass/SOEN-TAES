def is_samepatterns(colors, patterns):
    # Write a function to check whether it follows the sequence given in the patterns array.
    color_pattern_map = {}

    if len(colors) != len(patterns):
        return False

    for i in range(len(colors)):
        color = colors[i]
        pattern = patterns[i]

        if color in color_pattern_map:
            if color_pattern_map[color] != pattern:
                return False
        else:
            color_pattern_map[color] = pattern

    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_samepatterns(["red","green","green"], ["a", "b", "b"]), True)

if __name__ == '__main__':
    unittest.main()