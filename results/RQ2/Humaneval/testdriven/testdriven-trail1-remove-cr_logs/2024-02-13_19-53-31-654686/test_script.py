def bf(planet1, planet2):
    valid_planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    if planet1 not in valid_planets or planet2 not in valid_planets:
        return ()
    start_index = valid_planets.index(planet1)
    end_index = valid_planets.index(planet2)
    result = valid_planets[min(start_index, end_index) + 1:max(start_index, end_index)]
    return tuple(result)

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(bf('Jupiter', 'Neptune'), ('Saturn', 'Uranus'))
        self.assertEqual(bf('Earth', 'Mercury'), ('Venus'))
        self.assertEqual(bf('Mercury', 'Uranus'), ('Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn'))

if __name__ == '__main__':
    unittest.main()