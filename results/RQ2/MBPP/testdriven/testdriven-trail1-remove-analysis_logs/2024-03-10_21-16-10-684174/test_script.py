def otherside_rightangle(w, h):
    '''
    Write a function to find the third side of a right-angled triangle.
    assert otherside_rightangle(7, 8) == 10.63014581273465
    '''
    if w <= 0 or h <= 0:
        return "Invalid input"
    else:
        return (w**2 + h**2)**0.5
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(otherside_rightangle(7, 8), 10.63014581273465)

if __name__ == '__main__':
    unittest.main()