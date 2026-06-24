"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt
import pytest

from inflammation.models import daily_mean, daily_min


@pytest.mark.parametrize(
    "test_input, test_result", 
    [
    (np.array([[0, 0], [0, 0], [0, 0]]), np.array([0, 0])),
    (np.array([[1, 2], [3, 4], [5, 6]]), np.array([3, 4]))
    ]
)
def test_daily_mean(test_input, test_result):
    """Test that mean function works for various input arrays."""
    
    npt.assert_array_equal(daily_mean(test_input), test_result)


@pytest.mark.parametrize(
    "test_input, test_result",
    [
    (np.array([[1/3, 0], [0.4, 0], [4, -2000]]), np.array([1/3, np.nan])),
    (np.array([[1, 2], [3, 4], [5, 6]]), np.array([1, 2])),
    (np.array([[-1, -2], [-3, -4], [-5, -6]]), np.array([np.nan,np.nan]))
    ]
)
def test_daily_min(test_input, test_result):
    """Test that min function works for an array of negative integers."""

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_min(test_input), test_result)

