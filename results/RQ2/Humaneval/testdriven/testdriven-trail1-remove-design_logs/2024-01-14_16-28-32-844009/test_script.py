def bf(planet1, planet2):
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
    else:
        start_index = planets[planet1]
        end_index = planets[planet2]
        if start_index < end_index:
            return tuple(sorted([planet for planet, index in planets.items() if start_index < index < end_index], key=lambda x: planets[x]))
        else:
            return tuple(sorted([planet for planet, index in planets.items() if end_index < index < start_index], key=lambda x: planets[x]))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(bf('Jupiter', 'Neptune'), ('Saturn', 'Uranus'))

if __name__ == '__main__':
    unittest.main()