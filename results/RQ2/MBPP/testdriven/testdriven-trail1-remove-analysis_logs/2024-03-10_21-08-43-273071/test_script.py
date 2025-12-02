def is_samepatterns(colors, patterns):
    if len(colors) != len(patterns):
        return False
    
    for color, pattern in zip(colors, patterns):
        if color != pattern:
            return False
    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_samepatterns(["red","green","green"], ["a", "b", "b"]), True)

if __name__ == '__main__':
    unittest.main()