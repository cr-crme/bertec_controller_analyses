import pandas as pd


def construct_data_path(data_folder: str, project_name: str, session_name: str, trial_name: str) -> str:
    return f"{data_folder}/{project_name}/{session_name}/{trial_name}.csv"


def read_csv(data_path: str) -> pd.DataFrame:
    return pd.read_csv(data_path)
