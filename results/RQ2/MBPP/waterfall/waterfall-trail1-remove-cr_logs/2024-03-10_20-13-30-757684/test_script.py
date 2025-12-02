def get_coordinates(coordinate, result = []):
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            new_coordinate = [coordinate[0] + i, coordinate[1] + j]
            result.append(new_coordinate)
    return result

# Test Cases:
assert get_coordinates((3, 4)) == [[2, 3], [2, 4], [2, 5], [3, 3], [3, 4], [3, 5], [4, 3], [4, 4], [4, 5]]
assert get_coordinates((0, 0)) == [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
assert get_coordinates((-1, 2)) == [[-2, 1], [-2, 2], [-2, 3], [-1, 1], [-1, 2], [-1, 3], [0, 1], [0, 2], [0, 3]]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(adjac((3, 4)), [[2, 3], [2, 4], [2, 5], [3, 3], [3, 4], [3, 5], [4, 3], [4, 4], [4, 5]])

if __name__ == '__main__':
    unittest.main()