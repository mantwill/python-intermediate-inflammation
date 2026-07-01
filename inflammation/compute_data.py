"""Module containing mechanism for calculating standard deviation between datasets.
"""

import glob
import os
import numpy as np

from inflammation import models


class CSVDataSource:
    """
    Loads all the inflammation CSV files within a specified directory.
    """
    def __init__(self, dir_path):
        self.dir_path = dir_path

    def load_inflammation_data(self):
        data_file_paths = glob.glob(os.path.join(self.dir_path, 'inflammation*.csv'))
        if len(data_file_paths) == 0:
            raise ValueError(f"No inflammation CSV files found in path {self.dir_path}")
        data = map(models.load_csv, data_file_paths)
        return list(data)

class JSONDataSource:
    """A data source that loads inflammation data from JSON files in a directory."""
    
    def __init__(self, dirname):
        self.dirname = dirname

    def load_inflammation_data(self):
        """Loads all inflammation data from JSON files within the directory.

        Returns a list of 2D numpy arrays, one for each dataset."""
        data_file_paths = glob.glob(os.path.join(self.dirname, 'inflammation*.json'))
        if len(data_file_paths) == 0:
            raise ValueError(f"No inflammation data JSON files found in path {self.dirname}")
        data = map(models.load_json, data_file_paths)
        return list(data)
    
def analyse_data(data):
    """Calculates the standard deviation by day between datasets.

    Gets passed some inflammation data,
    works out the mean inflammation value for each day across all datasets,
    then plots the graphs of standard deviation of these means."""

    daily_standard_deviation = models.compute_standard_deviation_by_day(data)
    
    #means_by_day = map(models.daily_mean, data)
    #means_by_day_matrix = np.stack(list(means_by_day))


    graph_data = {
        'standard deviation by day': daily_standard_deviation,
    }
    # views.visualize(graph_data)
    
    return(daily_standard_deviation)

data = CSVDataSource('data/').load_inflammation_data()
print(analyse_data(data))
