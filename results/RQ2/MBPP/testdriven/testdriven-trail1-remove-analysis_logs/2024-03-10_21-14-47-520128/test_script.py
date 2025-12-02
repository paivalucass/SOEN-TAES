def find_star_num(n):
    star_number = 0
    count = 0
    while count < n:
        star_number += 1
        if is_star_number(star_number):
            count += 1
    return star_number

def is_star_number(num):
    # Implement the algorithm to check if a number is a star number
    pass

# Test the function
assert find_star_num(3) == 37
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_star_num(3), 37)

if __name__ == '__main__':
    unittest.main()