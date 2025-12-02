def find_volume(l, b, h):
    volume = (1/2 * b * h) * l
    assert volume >= 0, "Volume cannot be negative"
    return volume
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Volume(10, 8, 6), 240)

if __name__ == '__main__':
    unittest.main()