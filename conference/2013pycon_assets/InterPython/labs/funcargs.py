import unittest

class TestFunctions(unittest.TestCase):
    def test_function(self):
        # Variable args
        #
        # Create a function ``backwards`` that accepts variable
        # arguments ``(*args)`` and returns a list with the
        # arguments in ``reversed`` order.
        # ================================
        def backwards(*args):
            mylist   = []
            for i in reversed(args):
                mylist.append(i)
            
            return mylist

        # note that when passing a sequence, we need to flatten with the ``*``
        self.assertEqual(backwards(*[0,1,2]), [2,1,0])
        # no flattening required here
        self.assertEqual(backwards(3,2,1), [1,2,3])


        # Invoking variable args
        #
        # Create a function ``shove_args`` that takes one normal
        # parameter, ``func``, one named parameter and variable args.
        # It should call ``func`` with the named parameter and
        # variable args splatted out, and return the results.
        # ================================
        def shove_args(func, *args, **kwargs):
            return func(args, kwargs)

        #self.assertEqual(shove_args(backwards, 1, *[0, 2]), [2,0,1])


        # Keyword args
        #
        # Create a function ``sorted_keys`` that accepts only keyword
        # arguments and returns the sorted keys of those arguments
        # ================================
        def sorted_keys(*args, **kwargs):
            keys = kwargs.keys()
            keys.sort()
            return keys
            
        a_dict = {'a':1, 'b':2, '1':'one'}
        # note that we have to pass in a dict with **
        self.assertEqual(sorted_keys(**a_dict), ['1', 'a', 'b'])
        self.assertEqual(sorted_keys(c=3, d=5),['c', 'd'])

if __name__ == '__main__':
    unittest.main()
