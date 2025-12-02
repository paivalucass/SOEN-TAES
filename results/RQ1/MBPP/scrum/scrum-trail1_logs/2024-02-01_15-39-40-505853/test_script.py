def shell_sort(my_list):
    if not isinstance(my_list, list) or len(my_list) == 0:
        return "Invalid input. Please provide a non-empty list."

    n = len(my_list)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = my_list[i]
            j = i
            while j >= gap and my_list[j - gap] > temp:
                my_list[j] = my_list[j - gap]
                j -= gap
            my_list[j] = temp
        gap //= 2

    return my_list
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(shell_sort([12, 23, 4, 5, 3, 2, 12, 81, 56, 95]), [2, 3, 4, 5, 12, 12, 23, 56, 81, 95])

if __name__ == '__main__':
    unittest.main()