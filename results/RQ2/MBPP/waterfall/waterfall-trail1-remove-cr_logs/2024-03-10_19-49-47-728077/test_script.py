def find_Volume(length, breadth, height):
    if length <= 0:
        return "Invalid input: Length should be a positive value"
    elif breadth <= 0:
        return "Invalid input: Breadth should be a positive value"
    elif height <= 0:
        return "Invalid input: Height should be a positive value"
    
    volume = (1/2) * length * breadth * height
    return volume
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Volume(10, 8, 6), 240)

if __name__ == '__main__':
    unittest.main()