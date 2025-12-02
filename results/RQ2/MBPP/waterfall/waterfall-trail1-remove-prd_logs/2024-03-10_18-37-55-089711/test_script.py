def shell_sort(my_list):
    def gap_insertion_sort(arr, start, gap):
        for i in range(start + gap, len(arr), gap):
            current_val = arr[i]
            pos = i
            while pos >= gap and arr[pos - gap] > current_val:
                arr[pos] = arr[pos - gap]
                pos -= gap
            arr[pos] = current_val

    gap_sequence = [5, 3, 1]

    for gap in gap_sequence:
        for start_pos in range(gap):
            gap_insertion_sort(my_list, start_pos, gap)

    return my_list
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(shell_sort([12, 23, 4, 5, 3, 2, 12, 81, 56, 95]), [2, 3, 4, 5, 12, 12, 23, 56, 81, 95])

if __name__ == '__main__':
    unittest.main()