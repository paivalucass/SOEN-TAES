def is_samepatterns(colors, patterns):
    if len(colors) != len(patterns):
        return False
    for color, pattern in zip(colors, patterns):
        if color != pattern:
            return False
    return True
import unittest

class Test(unittest.TestCase):
    def test_is_samepatterns(self):
        self.assertTrue(is_samepatterns(["red","green","green"], ["a", "b", "b"]))

if __name__ == '__main__':
    unittest.main()