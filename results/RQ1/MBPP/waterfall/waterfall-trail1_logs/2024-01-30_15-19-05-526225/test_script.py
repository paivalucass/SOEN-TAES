def is_samepatterns(colors, patterns):
    if len(colors) != len(patterns) or not colors or not patterns:
        return False
    
    return all(color == pattern for color, pattern in zip(colors, patterns))
import unittest

class Test(unittest.TestCase):
    def test_is_samepatterns(self):
        self.assertEqual(is_samepatterns(["red","green","green"], ["a", "b", "b"]), True)

if __name__ == '__main__':
    unittest.main()