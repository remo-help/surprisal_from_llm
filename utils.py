import pandas as pd


def read_in_csv(path: str, feature_column: str, id_column: str = None) -> (pd.DataFrame, pd.DataFrame):
    """Takes a path string and returns a DataFrame.

    Args:
        path (str): The path to a .csv file

    Returns:
        DataFrame: The .csv file as a DataFrame
        :param path:
        :param id_colum:
        :param feature_column:
    """
    if path[-3:] == 'tsv':
        file = pd.read_csv(path,sep='\t')
    else:
        file = pd.read_csv(path)
    if id_column:
        return list(file[feature_column]), list(file[id_column])
    else:
        return list(file[feature_column]), None
