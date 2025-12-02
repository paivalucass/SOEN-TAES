def volume_cube(l: float) -> float:
    if isinstance(l, (int, float)):
        if l >= 0:
            volume = l * l * l
            return volume
        else:
            return "Error: Input 'l' should be a positive numerical value"
    else:
        return "Error: Input 'l' should be a numerical value"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(volume_cube(3), 27)

if __name__ == '__main__':
    unittest.main()