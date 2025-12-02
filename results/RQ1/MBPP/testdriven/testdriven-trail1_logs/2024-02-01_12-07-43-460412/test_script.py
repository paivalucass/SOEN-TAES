def magic_square_test(my_matrix):
    n = len(my_matrix)
    sum_list = []
    # calculate sum of rows
    for row in my_matrix:
        sum_list.append(sum(row))
    # calculate sum of columns
    for i in range(n):
        column_sum = 0
        for j in range(n):
            column_sum += my_matrix[j][i]
        sum_list.append(column_sum)
    # calculate sum of diagonals
    diag_sum1 = sum(my_matrix[i][i] for i in range(n))
    diag_sum2 = sum(my_matrix[i][n - i - 1] for i in range(n))
    sum_list.append(diag_sum1)
    sum_list.append(diag_sum2)
    # check if all sums are equal
    return all(x == sum_list[0] for x in sum_list)

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]]), True)

if __name__ == '__main__':
    unittest.main()