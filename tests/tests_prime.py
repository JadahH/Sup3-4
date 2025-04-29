from prime import if_prime, range_split, subrange

def test_if_prime_small(self):
        self.assertFalse(if_prime(0))
        self.assertFalse(if_prime(1))
        self.assertTrue(if_prime(2))
        self.assertTrue(if_prime(3))
        self.assertFalse(if_prime(4))
        self.assertTrue(if_prime(13))

def test_range_even(self):
        rngs = range_split(1, 10, 5)
        # total 10 numbers, 5 chunks → each size 2
        self.assertEqual(rngs, [(1,2),(3,4),(5,6),(7,8),(9,10)])

def test_range_uneven(self):
        rngs = range_split(1, 11, 4)
        # 11 numbers, 4 chunks → sizes 3,3,3,2
        self.assertEqual(rngs, [(1,3),(4,6),(7,9),(10,11)])

def test_subrange(self):
        # primes between 10–20
        self.assertEqual(subrange((10,20)),
                         [11,13,17,19])