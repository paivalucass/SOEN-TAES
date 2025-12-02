def min_jumps(steps, d):
    if not isinstance(steps, tuple) or len(steps) != 2 or not all(isinstance(i, (int, float)) for i in steps) or not isinstance(d, (int, float)):
        return "Invalid input"

    if steps[1] != 0:
        jump_length = steps[0]
        remaining_distance = d - steps[1]

        if remaining_distance < 0:
            return "Destination point is unreachable with the given length of jumps"

        jumps = remaining_distance / jump_length

        return jumps if jumps.is_integer() else round(jumps, 2)
    else:
        return "Invalid input"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(min_Jumps((3,4),11), 3.5)

if __name__ == '__main__':
    unittest.main()