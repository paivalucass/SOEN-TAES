def sum_average(number):
    try:
        if not isinstance(number, int) or number <= 0:
            raise ValueError("Input must be a positive integer")
        
        natural_numbers = [i for i in range(1, number+1)]
        sum_of_numbers = sum(natural_numbers)
        average_of_numbers = sum_of_numbers / number
        
        return (sum_of_numbers, average_of_numbers)
    
    except ValueError as ve:
        return str(ve)

    except Exception as e:
        return str(e)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_average(10), (55, 5.5))

if __name__ == '__main__':
    unittest.main()