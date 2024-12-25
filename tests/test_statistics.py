# tests/test_statistics.py

from src.lib.statistics import mean, variance, standard_deviation

def test_mean():
    assert mean([1,2,3]) == 2

def test_variance():
    assert variance([1,2,3,4,5]) == 2

def test_standard_deviation():
    assert standard_deviation([1,2,3,4,5]) == 2 ** 0.5
