"""Module containing models representing patients and their data.

The Model layer is responsible for the 'business logic' part of the software.

Patients' data is held in an inflammation table (2D array) where each row contains
inflammation data for a single patient taken over a number of days
and each column represents a single day across all patients.
"""

import numpy as np
from inflammation import models


def load_csv(filename):
    """Load a Numpy array from a CSV

    :param filename: Filename of CSV to load
    :returns: 2D Numpy array of inflammation data
    """
    return np.loadtxt(fname=filename, delimiter=',')

def load_json(filename):
    """Load a numpy array from a JSON document.
    
    Expected format:
    [
      {
        "observations": [0, 1]
      },
      {
        "observations": [0, 2]
      }    
    ]
    :param filename: Filename of JSON to load
    """
    
    with open(filename, 'r', encoding='utf-8') as file:
        data_as_json = json.load(file)
        return [np.array(entry['observations']) for entry in data_as_json]
    

def daily_mean(data):
    """Calculate the daily mean of a 2D inflammation data array.
    :param data: 2D Numpy array of inflammation data
    :returns: 1D Numpy array of daily mean inflammation values
    """
    return np.mean(data, axis=0)


def daily_max(data):
    """Calculate the daily max of a 2D inflammation data array.

    :param data: 2D Numpy array of inflammation data
    :returns: 1D Numpy array of daily max inflammation values
    """
    return np.max(data, axis=0)


def patient_normalise(data):
    """Normalise patient data from a 2D inflammation data array."""
    if not isinstance(data, np.ndarray):
        raise TypeError('Data must be a Numpy array')
    if data.ndim != 2:
        raise ValueError('Data must be a 2D array')
    if np.any(data < 0):
        raise ValueError('Inflammation values should not be negative')
    max_data = np.max(data, axis=1)
    return data / max_data[:, np.newaxis]


def daily_min(data):
    """Calculate the daily min of a 2D inflammation data array.

    :param data: 2D Numpy array of inflammation data
    :returns: 1D Numpy array of daily min inflammation values
    """
    min_value = np.min(data, axis=0).astype(float)
    min_value[min_value < 0] = np.nan
    return min_value
def compute_standard_deviation_by_day(data):
    means_by_day = map(models.daily_mean, data)
    means_by_day_matrix = np.stack(list(means_by_day))

    daily_standard_deviation = np.std(means_by_day_matrix, axis=0)
    return daily_standard_deviation
