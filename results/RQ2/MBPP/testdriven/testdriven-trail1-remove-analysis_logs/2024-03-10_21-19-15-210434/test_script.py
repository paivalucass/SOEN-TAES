def shell_sort(my_list):
    '''
    Write a function to sort the given array by using shell sort
    assert shell_sort([12, 23, 4, 5, 3, 2, 12, 81, 56, 95]) == [2, 3, 4, 5, 12, 12, 23, 56, 81, 95]
    '''
    # Shell sort algorithm
    n = len(my_list)
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = my_list[i]
            j = i
            # Insertion sort
            while j >= interval and my_list[j - interval] > temp:
                my_list[j] = my_list[j - interval]
                j -= interval
            my_list[j] = temp
        interval //= 2
    return my_list
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(shell_sort([12, 23, 4, 5, 3, 2, 12, 81, 56, 95]), [2, 3, 4, 5, 12, 12, 23, 56, 81, 95])

if __name__ == '__main__':
    unittest.main()