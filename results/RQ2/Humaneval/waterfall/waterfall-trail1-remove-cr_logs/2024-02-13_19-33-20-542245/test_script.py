def bf(planet1, planet2):
    planet_names = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

    if planet1 not in planet_names or planet2 not in planet_names or planet1 == planet2:
        return ()

    start_index = min(planet_names.index(planet1), planet_names.index(planet2))
    end_index = max(planet_names.index(planet1), planet_names.index(planet2))

    if start_index < end_index:
        return tuple(planet_names[start_index + 1:end_index])
    else:
        return tuple(planet_names[end_index + 1:start_index])
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(bf("Jupiter", "Neptune"), ("Saturn", "Uranus"))
        self.assertEqual(bf("Earth", "Mercury"), ("Venus"))
        self.assertEqual(bf("Mercury", "Uranus"), ("Venus", "Earth", "Mars", "Jupiter", "Saturn"))

if __name__ == '__main__':
    unittest.main()