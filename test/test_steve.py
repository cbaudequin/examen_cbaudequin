from devine_steve import *

def test_decomposer():
    assert decomposer(-100) == None
    assert decomposer(99) == None
    assert decomposer(1000) == None
    assert decomposer(2000) == None
    assert decomposer(100) == (1,0,0)
    assert decomposer(500) == (5,0,0)
    assert decomposer(999) == (9,9,9)


def test_somme():
    assert somme(5, 2, 3) == True
    assert somme(7, 1, 6) == None
    assert somme(4, 0, 4) == True
    assert somme(9, 3, 6) == None


def test_divisible():
    assert divisible(18) == True
    assert divisible(27) == True
    assert divisible(35) == False
    assert divisible(42) == False

