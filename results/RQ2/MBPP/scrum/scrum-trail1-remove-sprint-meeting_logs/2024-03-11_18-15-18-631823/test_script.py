def is_samepatterns(colors, patterns):
    color_to_pattern = {}
    pattern_to_color = {}
    
    if len(colors) != len(patterns):
        return False
    
    for color, pattern in zip(colors, patterns):
        if color in color_to_pattern and color_to_pattern[color] != pattern:
            return False
        else:
            color_to_pattern[color] = pattern
        
        if pattern in pattern_to_color and pattern_to_color[pattern] != color:
            return False
        else:
            pattern_to_color[pattern] = color
    
    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_samepatterns(["red","green","green"], ["a", "b", "b"]), True)

if __name__ == '__main__':
    unittest.main()