import math

def otherside_rightangle(w, h):
    return math.sqrt(w**2 + h**2)

import math

class Test(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(otherside_rightangle(7, 8), 10.63014581273465)

if __name__ == '__main__':
    unittest.main()