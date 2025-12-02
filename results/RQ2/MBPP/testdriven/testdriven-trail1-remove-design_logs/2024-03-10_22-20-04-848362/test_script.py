def _sum(arr):
    try:
        if not isinstance(arr, list):
            raise TypeError("Input should be a list")
        
        total_sum = sum(arr)
        return total_sum
    except TypeError as e:
        return str(e)
    except:
        return "An error occurred"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(_sum([1, 2, 3]), 6)

if __name__ == '__main__':
    unittest.main()