"""Module containing mechanism for calculating standard deviation between datasets.
"""

import glob
import os
import numpy as np

from inflammation import models, views


class CSVDataSource:
    """A data source that loads inflammation data from CSV files in a directory."""

    def __init__(self, dirname):
        self.dirname = dirname

    def load_data(self):
        """Loads all inflammation data from CSV files within the directory.

        Returns a list of 2D numpy arrays, one for each dataset."""
        data_file_paths = glob.glob(os.path.join(self.dirname, 'inflammation*.csv'))
        if len(data_file_paths) == 0:
            raise ValueError(f"No inflammation data CSV files found in path {self.dirname}")
        data = map(models.load_csv, data_file_paths)

        return data

class JSONDataSource:
    """A data source that loads inflammation data from JSON files in a directory."""
    
    def __init__(self, dirname):
        self.dirname = dirname

    def load_data(self):
        """Loads all inflammation data from JSON files within the directory.

        Returns a list of 2D numpy arrays, one for each dataset."""
        data_file_paths = glob.glob(os.path.join(self.dirname, 'inflammation*.json'))
        if len(data_file_paths) == 0:
            raise ValueError(f"No inflammation data JSON files found in path {self.dirname}")
        data = map(models.load_json, data_file_paths)

def analyse_data(data):
    """Calculates the standard deviation by day between datasets.

    Gets passed some inflammation data,
    works out the mean inflammation value for each day across all datasets,
    then plots the graphs of standard deviation of these means."""

    means_by_day = map(models.daily_mean, data)
    means_by_day_matrix = np.stack(list(means_by_day))

    daily_standard_deviation = np.std(means_by_day_matrix, axis=0)

    graph_data = {
        'standard deviation by day': daily_standard_deviation,
    }
    views.visualize(graph_data)

data = CSVDataSource('data').load_data()
analyse_data(data)