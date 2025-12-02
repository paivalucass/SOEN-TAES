def surfacearea_cylinder(r, h):
    return 2 * 3.14159 * r * (r + h)

assert surfacearea_cylinder(10, 5) == 942.45
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(surfacearea_cylinder(10, 5), 942.48)

if __name__ == '__main__':
    unittest.main()