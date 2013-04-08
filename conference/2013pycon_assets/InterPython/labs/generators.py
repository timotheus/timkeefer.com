import types
import unittest

class TestGenerators(unittest.TestCase):

    def test_gen(self):
        # Generators
        #
        # Implement a generator ``two`` that yields 1 then 2
        # ================================
        def two():
            x = 1
            while x < 3:
                yield x

                x += 1

        two_gen = two()
        self.assertTrue(isinstance(two_gen, types.GeneratorType))
        self.assertEqual(next(two_gen), 1)
        self.assertEqual(next(two_gen), 2)
        self.assertRaises(StopIteration, next, two_gen)

        # Generator
        #
        # Implement a generator ``countdown`` that takes a integer yields the sequence from range(integer, -1, -1)
        # ================================
        def countdown(myint):
            x = myint
            while x >= 0:
                yield x

                x -= 1

        one = countdown(1)
        self.assertTrue(isinstance(one, types.GeneratorType))
        self.assertEqual(next(one), 1)
        self.assertEqual(next(one), 0)
        self.assertRaises(StopIteration, next, one)

if __name__ == '__main__':
    unittest.main()
