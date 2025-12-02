def min_val(listval):
    try:
        if not listval:
            raise ValueError("List is empty")
        
        # Handling non-numeric values
        numeric_list = [x for x in listval if isinstance(x, (int, float))]
        
        if not numeric_list:
            raise ValueError("No numeric values in the list")

        # Using quicksort algorithm for efficient sorting
        def quicksort(arr):
            if len(arr) <= 1:
                return arr
            else:
                pivot = arr[0]
                less = [x for x in arr[1:] if x <= pivot]
                greater = [x for x in arr[1:] if x > pivot]
                return quicksort(less) + [pivot] + quicksort(greater)

        sorted_list = quicksort(numeric_list)
        return sorted_list[0]

    except ValueError as ve:
        return str(ve)
    
# Test cases
assert min_val(['Python', 3, 2, 4, 5, 'version']) == 2
assert min_val([]) == "List is empty"
assert min_val(['Python', 'version']) == "No numeric values in the list"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(min_val(['Python', 3, 2, 4, 5, 'version']), 2)

if __name__ == '__main__':
    unittest.main()