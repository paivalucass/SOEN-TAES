def find_planets_between(planet1, planet2):
    planets = {
        "Mercury": 1,
        "Venus": 2,
        "Earth": 3,
        "Mars": 4,
        "Jupiter": 5,
        "Saturn": 6,
        "Uranus": 7,
        "Neptune": 8
    }
    if planet1 not in planets or planet2 not in planets:
        return ()
    result = []
    start = min(planets[planet1], planets[planet2])
    end = max(planets[planet1], planets[planet2])
    for planet, orbit in planets.items():
        if start < orbit < end:
            result.append(planet)
    return tuple(sorted(result, key=lambda x: planets[x]))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(bf('Jupiter', 'Neptune'), ('Saturn', 'Uranus'))
        self.assertEqual(bf('Earth', 'Mercury'), ('Venus'))
        self.assertEqual(bf('Mercury', 'Uranus'), ('Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn'))

if __name__ == '__main':
    unittest.main()