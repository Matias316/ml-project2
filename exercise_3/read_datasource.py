import pandas as pd


def load_dataframe_from_excel_file(path_to_excel_file):
    """Creates a dataframe with data from excel file

    Args:
        path_to_excel_file (str): Path to excel file including filename

    Raises:
        IOError: excel file not found

    Returns:
        df_result: Dataframe with content from excel file
    """
    try:
        df_result = pd.read_excel(path_to_excel_file, sheet_name='Data')
    except IOError as e:
        raise e

    return df_result
