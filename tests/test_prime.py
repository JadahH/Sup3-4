import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(__file__, '..', 'src', 'Prime')))

from prime.prime_num import if_prime, range_split, subrange

def test_if_prime_small():
    assert not if_prime(0)
    assert not if_prime(1)
    assert if_prime(2)
    assert if_prime(13)

def test_range_even():
    assert range_split(1, 10, 5) == [(1,2),(3,4),(5,6),(7,8),(9,10)]

def test_range_uneven():
    assert range_split(1, 11, 4) == [(1,3),(4,6),(7,9),(10,11)]

def test_subrange():
    assert subrange((10,20)) == [11,13,17,19]