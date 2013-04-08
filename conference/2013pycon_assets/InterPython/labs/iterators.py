import unittest
import types

class TestIterators(unittest.TestCase):
    def test_iterators(self):
        # Iterators
        #
        # Create a list ``a_list`` with [0,1,2] in it.
        # Get an iterator ``an_iter`` for ``a_list`` by calling
        # the ``iter`` function on it
        # ================================
        a_list = range(3)
        an_iter = iter(a_list)

        self.assertEqual(next(an_iter), 0)
        self.assertEqual(next(an_iter), 1)
        self.assertEqual(next(an_iter), 2)
        self.assertRaises(StopIteration, next, an_iter)


        # Iterators
        #
        # Create a list, ``b_list`` with [4, 3, 2] in it.
        # Store an iterator for ``b_list`` in ``b_iter``.
        # Take 2 items off the iterator by calling ``next()`` on it.
        # ==================   ==============
        b_list = [4,3,2]
        b_iter = iter(b_list)
        b_iter.next()
        b_iter.next()
        self.assertEqual(next(b_iter), 2)
        self.assertRaises(StopIteration, next, b_iter)

if __name__ == '__main__':
    unittest.main()
