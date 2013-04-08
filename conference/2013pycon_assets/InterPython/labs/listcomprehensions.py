import unittest

class TestListComprehensions(unittest.TestCase):
    def test_lc(self):
        # Identity List Comprehension
        #
        # Write a function ``identity`` that accepts a sequence and uses a list comprehension to create a new sequence that is the same.
        # ================================
        def identity(*args):
            results = [x for x in args]
            return results[0]

        self.assertEqual(identity(range(3)), [0,1,2])
        seq = [0,1,2]
        # since identity creates a new list, the id's should be different
        self.assertFalse(identity(seq) is seq)

        # List Comp 2
        #
        # Create a function ``double`` that accepts a sequence and
        # returns a sequence where every item is multiplied by 2 (use
        # list comprehension)
        # ================================

        self.assertEqual(double(range(3)), [0,2,4])

        # List Comp 3
        #
        # Create a function, ``truthy`` that accepts a sequence and
        # uses a list comprehension to return the items that a
        # "truthy" in the sequence.
        # ================================

        self.assertEqual(truthy([0, None, '', 3, 'hello']), [3, 'hello'])

        # List Comp 4
        #
        # Create a function ``matrix`` that takes 2 parameters, x and
        # y and does the following pseudocode using list comps.:
        # results = []
        # for item in range(0, x):
        #     for item2 in range(0, y):
        #         if item2 % 2 == 0:
        #             results.append((item*3, item2))
        # return results
        # ================================

        self.assertEqual(matrix(3,4), [(0, 0), (0, 2), (3, 0), (3, 2), (6, 0), (6, 2)])


if __name__ == '__main__':
    unittest.main()
