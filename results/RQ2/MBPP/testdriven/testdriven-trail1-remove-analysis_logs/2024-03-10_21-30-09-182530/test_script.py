def mul_even_odd(input_list):
    if len(input_list) < 2:
        return None
    
    even_numbers = [num for num in input_list if num % 2 == 0]
    odd_numbers = [num for num in input_list if num % 2 != 0]

    if len(even_numbers) == 0 or len(odd_numbers) == 0:
        return None

    product_of_first_even = even_numbers[0]
    product_of_first_odd = odd_numbers[0]

    return product_of_first_even * product_of_first_odd

# Test cases
print(mul_even_odd([1,3,5,7,4,1,6,8]))  # Expected output: 4
print(mul_even_odd([]))  # Expected output: None
print(mul_even_odd([2,4,6,8]))  # Expected output: None
print(mul_even_odd([1,3,5,7]))  # Expected output: None
print(mul_even_odd([-3,2,-5,7,-4,1,6,8]))  # Expected output: -12
print(mul_even_odd([6]))  # Expected output: None
print(mul_even_odd([1,10,100,1000]))  # Expected output: 10
print(mul_even_odd([2,2,3,3,4,4]))  # Expected output: 6
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(mul_even_odd([1,3,5,7,4,1,6,8]), 4)

if __name__ == '__main__':
    unittest.main()