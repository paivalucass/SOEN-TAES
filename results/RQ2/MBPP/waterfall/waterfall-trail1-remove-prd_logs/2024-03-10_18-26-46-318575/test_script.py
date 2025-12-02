def is_samepatterns(colors, patterns):
    if len(colors) != len(patterns):
        raise ValueError("Lengths of 'colors' and 'patterns' should be the same")

    if not all(isinstance(color, str) for color in colors):
        raise TypeError("Input colors should be of type string")

    if not all(isinstance(pattern, str) for pattern in patterns):
        raise TypeError("Input patterns should be of type string")

    for i in range(len(patterns)):
        if patterns.count(patterns[i]) != colors.count(colors[i]):
            return False
    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_samepatterns(["red","green","green"], ["a", "b", "b"]), True)

if __name__ == '__main__':
    unittest.main()