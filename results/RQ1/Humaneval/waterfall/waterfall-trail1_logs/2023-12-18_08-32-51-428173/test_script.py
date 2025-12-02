def bf(planet1, planet2):
    planets_orbits = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    start_orbit = min(get_planet_orbit(planet1), get_planet_orbit(planet2))
    end_orbit = max(get_planet_orbit(planet1), get_planet_orbit(planet2))
    result = [planet for planet in planets_orbits if start_orbit < get_planet_orbit(planet) < end_orbit]
    return tuple(sorted(result, key=lambda x: get_planet_orbit(x)))
import unittest

class Test(unittest.TestCase):
    def test_bf(self):
        self.assertEqual(bf('Jupiter', 'Neptune'), ('Saturn', 'Uranus'))
        self.assertEqual(bf('Earth', 'Mercury'), ('Venus'))
        self.assertEqual(bf('Mercury', 'Uranus'), ('Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn'))

if __name__ == '__main__':
    unittest.main()