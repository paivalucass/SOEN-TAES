def min_Jumps(steps, d): 
    def calculate_distance(x, y): 
        return ((x**2) + (y**2)) ** 0.5 
    
    total_distance = calculate_distance(steps[0], steps[1]) 
    num_jumps = total_distance / d 
    return round(num_jumps, 1)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(min_Jumps((3,4), 11), 3.5)

if __name__ == '__main__':
    unittest.main()