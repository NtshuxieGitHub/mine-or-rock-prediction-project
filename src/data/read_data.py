# Import dependency libraries
import pandas as pd
from src.config import sonar_data_path

def read_data() -> pd.DataFrame:
    """
    Read data into Python from a specified file path. The output is a Pandas dataframe.

    Returns:
        pd.DataFrame: A Pandas dataframe containing the data from the file.

    Raises:
        FileNotFoundError: if the file does not exist.
        pd.errors.EmptyDataError: if the file is empty.
        pd.errors.ParseError: if the file is amlformed
    """

    try:
        # Read the data into a Pandas dataframe
        sonar_data = pd.read_csv(sonar_data_path, header=None)

        # Return the dataframe
        return sonar_data

    except FileNotFoundError:
        # Handle the case where the file is not found
        raise FileNotFoundError(f"File '{sonar_data_path}' not found.")
    except pd.errors.EmptyDataError:
        # Handle the case where the file is empty
        raise pd.errors.EmptyDataError(f"File '{sonar_data_path}' is empty.")
    except pd.errors.ParseError:
        # Handle the case where the file is malformed
        raise pd.errors.ParseError(f"File '{sonar_data_path}' is malformed.")

