def is_Sum_Of_Powers_Of_Two(n):
    try:
        if not isinstance(n, int):
            raise ValueError("Input must be an integer")
        
        def calculate_powers_of_two(n):
            power = 1
            powers = []
            while power <= n:
                powers.append(power)
                power *= 2
            return powers
        
        def check_sum_of_powers(n, powers):
            remaining_value = n
            for power in reversed(powers):
                if power <= remaining_value:
                    remaining_value -= power
            return remaining_value == 0
        
        powers = calculate_powers_of_two(n)
        return check_sum_of_powers(n, powers)
    
    except ValueError as ve:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_Sum_Of_Powers_Of_Two(10), True)

if __name__ == '__main__':
    unittest.main()