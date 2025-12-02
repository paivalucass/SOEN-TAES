import math

def area_polygon(s, l):
    return (l * s ** 2) / (4 * math.tan(math.pi / s))
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(area_polygon(4, 20), 400., delta=0.001)

if __name__ == '__main__':
    unittest.main()