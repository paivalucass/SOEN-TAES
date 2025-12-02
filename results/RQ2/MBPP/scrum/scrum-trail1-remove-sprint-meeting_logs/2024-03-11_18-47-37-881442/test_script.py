def cube_nums(nums):
    try:
        if not all(isinstance(number, (int, float)) for number in nums):
            raise TypeError("Input must be a list of numbers")
    except TypeError as e:
        print(e)
        return

    cubes = [number**3 for number in nums]
    
    return cubes
assert cube_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(cube_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000])

if __name__ == '__main__':
    unittest.main()