def even_odd_count(num):
    try:
        num_str = str(abs(num))
        even_count = 0
        odd_count = 0
        for digit in num_str:
            if int(digit) % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
        return (even_count, odd_count)
    except:
        raise ValueError("Input must be an integer")

# Test cases
print(even_odd_count(-12))  # Output: (1, 1)
print(even_odd_count(123))   # Output: (1, 2)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(even_odd_count(-12), (1, 1))
        self.assertEqual(even_odd_count(123), (1, 2))

if __name__ == '__main__':
    unittest.main()