def is_samepatterns(colors, patterns):
    if len(colors) != len(patterns):
        return False
    
    color_map = {}
    for i in range(len(colors)):
        color = colors[i]
        pattern = patterns[i]
        if color in color_map:
            if color_map[color] != pattern:
                return False
        else:
            color_map[color] = pattern
    
    for i in range(len(colors)):
        color = colors[i]
        pattern = patterns[i]
        if color_map[color] != pattern:
            return False
    
    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_samepatterns(["red","green","green"], ["a", "b", "b"]), True)

if __name__ == '__main__':
    unittest.main()