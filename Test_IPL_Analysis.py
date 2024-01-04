"""
    Unit Testing is done for the respective functions that are used to calculate Numerical Statistics in NumericalAnalysis.py file.

    Student ID: A00315875
    Date: 20/12/2023
"""
from NumericalAnalysis import *
from pytest import *


def test_calc_the_mean():
    assert Calc_the_mean([1, 2, 3, 4, 5]) == 3.0


def test_calc_the_mode():
    assert Calc_the_mode([1, 2, 3, 4, 5]) == 1


def test_calc_the_median():
    assert Calc_the_median([1, 2, 3, 4, 5]) == 3


def test_calc_the_range():
    assert Calc_the_range([1, 2, 3, 4, 5]) == 4


def test_calc_the_interquartile_range():
    assert Calc_the_interquartile_Range([1, 2, 3, 4, 5]) == 3.0


def test_calc_standard_deviation():
    assert Calc_Standard_Deviation([1, 2, 3, 4, 5]) == approx(1.58, .01)


def test_calc_median_skewness():
    assert Calc_median_skewness([1, 9, 2, 3, 4, 9, 5]) == approx(0.6697, .01)


def test_calc_mode_skewness():
    assert Calc_mode_skewness([1, 9, 2, 3, 4, 5]) == approx(1.0660, .01)


def test_calc_correlation():
    assert calc_correlation([1, 2, 3, 4], [20, 30, 22, 33]) == approx(0.64, 0.01)


if __name__ == "__main__":
    main([__file__, '-v'])
