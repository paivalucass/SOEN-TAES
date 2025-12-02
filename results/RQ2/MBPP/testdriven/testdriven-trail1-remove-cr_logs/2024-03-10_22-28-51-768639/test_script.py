def is_samepatterns(colors, patterns):
    return [x==y for x,y in zip(map(colors.index, colors), map(patterns.index, patterns))]==[True]*len(colors)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_samepatterns(["red","green","green"], ["a", "b", "b"]), True)

if __name__ == '__main__':
    unittest.main()