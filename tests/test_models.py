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

from inflammation.models import patient_normalise

@pytest.mark.parametrize(
    "test, expected, expect_raises",
    [
        # previous test cases here, with None for expect_raises, except for the next one - add ValueError
        # as an expected exception (since it has a negative input value)
        (
            [[-1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [[0, 0.67, 1], [0.67, 0.83, 1], [0.78, 0.89, 1]],
            ValueError,
        ),
        (
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [[0.33, 0.67, 1], [0.67, 0.83, 1], [0.78, 0.89, 1]],
            None,
        ),
    ])
def test_patient_normalise(test, expected, expect_raises):
    """Test normalisation works for arrays of one and positive integers."""
        
    if expect_raises is not None:
        with pytest.raises(expect_raises):
            patient_normalise(np.array(test))
    else:
        result = patient_normalise(np.array(test))
        npt.assert_allclose(result, np.array(expected), rtol=1e-2, atol=1e-2)