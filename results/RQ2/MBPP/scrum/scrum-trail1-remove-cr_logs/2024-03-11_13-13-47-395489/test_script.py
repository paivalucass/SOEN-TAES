def rearrange_bigger(n):
    try:
        if not isinstance(n, int) or n < 0:
            raise ValueError("Input must be a positive integer")
        
        num_str = str(n)
        num_list = list(num_str)
        
        i = len(num_list) - 1
        while i > 0:
            if num_list[i] > num_list[i-1]:
                break
            i -= 1
        
        if i == 0:
            return int("No rearrangement possible")
        
        pivot = i - 1
        for j in range(len(num_list)-1, pivot, -1):
            if num_list[j] > num_list[pivot]:
                num_list[pivot], num_list[j] = num_list[j], num_list[pivot]
                break
        
        num_list[pivot+1:] = sorted(num_list[pivot+1:])
        
        result = int("".join(num_list))
        return result
    
    except ValueError as ve:
        return str(ve)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(rearrange_bigger(12), 21)

if __name__ == '__main__':
    unittest.main()