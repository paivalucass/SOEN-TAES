def is_samepatterns(colors, patterns):
    pattern_dict = {}
    for color, pattern in zip(colors, patterns):
        if pattern not in pattern_dict:
            pattern_dict[pattern] = color
        elif pattern_dict[pattern] != color:
            return False
    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_samepatterns(["red","green","green"], ["a", "b", "b"]), True)

if __name__ == '__main__':
    unittest.main()