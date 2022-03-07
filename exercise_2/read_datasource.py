from pathlib import Path
import json
import pandas as pd


def load_dataframe_from_json_files(path_to_json_files, prefix):
    """Creates a dataframe with data from the <prefix>*.json files

    Args:
        path_to_json_files (str): Path to folder containing json files
        prefix (str): Prefix used to identify .json files to be loaded in the dataframe

    Raises:
        IOError: .json file not found

    Returns:
        df_result: Dataframe with content from .json files
    """

    data_source_dir = Path(path_to_json_files)
    dfs_list = []
    for filename in data_source_dir.glob(prefix + '*.json'):
        try:
            data = json.load(open(file=path_to_json_files + '/' + filename.name, mode='r', encoding="utf-8"))
            df = pd.DataFrame(data["data"])
            dfs_list.append(df)
        except IOError as e:
            raise e
    df_result = pd.concat(dfs_list)
    return df_result
