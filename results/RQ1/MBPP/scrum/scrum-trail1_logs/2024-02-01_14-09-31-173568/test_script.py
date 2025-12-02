def find_Volume(length_in_cm, breadth_in_cm, height_in_cm):
    if length_in_cm <= 0 or breadth_in_cm <= 0 or height_in_cm <= 0:
        return -1
    
    volume = (1/2) * length_in_cm * breadth_in_cm * height_in_cm
    return volume
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Volume(10, 8, 6), 240)

if __name__ == '__main__':
    unittest.main()