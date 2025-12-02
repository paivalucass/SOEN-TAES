def bell_number(n):
    if not isinstance(n, int) or n < 0:
        return "Error: Invalid input value"

    bell_triangle = [[1]]

    for i in range(1, n):
        new_row = [bell_triangle[i-1][-1]]
        for j in range(i):
            new_row.append(new_row[j] + bell_triangle[i-1][j])
        bell_triangle.append(new_row)

    return bell_triangle[n-1][-1]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(bell_number(2), 2)

if __name__ == '__main__':
    unittest.main()