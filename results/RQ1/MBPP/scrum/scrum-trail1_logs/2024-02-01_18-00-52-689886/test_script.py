import math

def triangle_area(r) :
    if r <= 0:
        return None
    else:
        return (math.pi * r * r) / 2
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(triangle_area(1), 0.5)
        self.assertEqual(triangle_area(2), 2)
        self.assertEqual(triangle_area(-1), None)

if __name__ == '__main__':
    unittest.main()