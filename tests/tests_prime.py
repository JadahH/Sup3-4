from prime import if_prime 

def test_if_prime_small(self):
        self.assertFalse(if_prime(0))
        self.assertFalse(if_prime(1))
        self.assertTrue(if_prime(2))
        self.assertTrue(if_prime(3))
        self.assertFalse(if_prime(4))
        self.assertTrue(if_prime(13))