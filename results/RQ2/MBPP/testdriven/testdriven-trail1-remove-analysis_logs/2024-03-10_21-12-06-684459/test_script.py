import math

def area_polygon(sides, length):
    '''Write a function to calculate the area of a regular polygon given the length and number of its sides.'''
    if sides < 3:
        raise ValueError("Number of sides must be greater than 2")
    if length <= 0:
        raise ValueError("Length of each side must be a positive number")
    
    apothem = length / (2 * math.tan(math.pi / sides))
    area = (sides * length * apothem) / 2
    return area
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(area_polygon(4, 20), 400., delta=0.001)

if __name__ == '__main__':
    unittest.main()