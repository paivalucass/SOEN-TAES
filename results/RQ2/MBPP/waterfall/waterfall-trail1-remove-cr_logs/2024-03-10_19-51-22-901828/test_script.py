def is_samepatterns(colors, patterns):
    return colors == patterns
import unittest

class Test(unittest.TestCase):
    def test_is_samepatterns(self):
        self.assertEqual(is_samepatterns(["red","green","green"], ["a", "b", "b"]), True)

if __name__ == '__main__':
    unittest.main()