def unique_sublists(list1):
    # Write a function to count lists within a list. 
    # The function should return a dictionary where every list is converted to a tuple and the value of such tuple is the number of its occurrences in the original list.
    
    # Validate input
    if not all(isinstance(sublist, list) for sublist in list1):
        raise TypeError("Input must be a list of lists")
    
    # Convert inner lists to tuples
    tuples_list = [tuple(sublist) for sublist in list1]

    # Create a dictionary to store tuples as keys and their occurrences as values
    count_dict = {}
    for tup in tuples_list:
        if tup in count_dict:
            count_dict[tup] += 1
        else:
            count_dict[tup] = 1
    
    # Return the dictionary as the output
    return count_dict

# Test cases
assert unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]) == {(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1}
assert unique_sublists([]) == {}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]), {(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1})

if __name__ == '__main__':
    unittest.main()