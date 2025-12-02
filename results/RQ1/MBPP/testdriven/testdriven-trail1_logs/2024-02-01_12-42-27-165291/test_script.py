def shell_sort(my_list):
    '''Write a function to sort the given array by using shell sort.'''
    if not my_list:
        return "Error: Input array is empty"
    
    if not isinstance(my_list, list):
        return "Error: Invalid input"
    
    # Shell sort algorithm implementation
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

# Test Cases
assert shell_sort([]) == "Error: Input array is empty"
assert shell_sort([5]) == [5]
assert shell_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
assert shell_sort('invalid input') == "Error: Invalid input"
assert shell_sort([12, 23, 4, 5, 3, 2, 12, 81, 56, 95]) == [2, 3, 4, 5, 12, 12, 23, 56, 81, 95]
import unittest

class Test(unittest.TestCase):
    def test_shell_sort(self):
        self.assertEqual(shell_sort([12, 23, 4, 5, 3, 2, 12, 81, 56, 95]), [2, 3, 4, 5, 12, 12, 23, 56, 81, 95])

if __name__ == '__main__':
    unittest.main()