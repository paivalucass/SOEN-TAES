def find_Volume(l, b, h):
    if not all(isinstance(x, (int, float)) for x in [l, b, h]):
        raise ValueError("Invalid input, all parameters must be numerical values")

    volume = (1/2) * l * b * h

    assert find_Volume(10, 8, 6) == 240
    assert find_Volume(0, 8, 6) == 0
    assert find_Volume(10, -8, 6) == -240
    assert find_Volume("abc", 8, 6)  # Bug fix: Changed find_Volume to find_Volume

    return volume
import unittest

class Test(unittest.TestCase):
    def test_find_volume(self):
        self.assertEqual(find_Volume(10, 8, 6), 240)

if __name__ == '__main__':
    unittest.main()