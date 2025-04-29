from prime import if_prime, range_split

def test_if_prime_small(self):
        self.assertFalse(if_prime(0))
        self.assertFalse(if_prime(1))
        self.assertTrue(if_prime(2))
        self.assertTrue(if_prime(3))
        self.assertFalse(if_prime(4))
        self.assertTrue(if_prime(13))

def test_split_range_even(self):
        rngs = range_split(1, 10, 5)
        # total 10 numbers, 5 chunks → each size 2
        self.assertEqual(rngs, [(1,2),(3,4),(5,6),(7,8),(9,10)])