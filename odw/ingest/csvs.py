import csv
from io import BytesIO, StringIO
from typing import Dict, List

import pandas as pd
import numpy as np

from odw.storage.clickhouse import ClickhouseInterface, CLICKHOUSE_DATA_TYPES


MAX_BATCH_SIZE = 100000


def get_csv_metadata(file_data: BytesIO) -> Dict[str, str]:
    # Read first N rows
    df = pd.read_csv(file_data, nrows=10000, parse_dates=True, infer_datetime_format=True)
    # Get headers from CSV file
    data_types = dict(df.dtypes.items())
    # Convert to clickhouse data types
    for header in data_types.keys():
        data_types[header] = CLICKHOUSE_DATA_TYPES[data_types[header]]
    return data_types


def push_csv_to_clickhouse(file_data: bytes, database: str, table: str, primary_keys: List[str]):
    ci = ClickhouseInterface(host="clickhouse", password="DataLake123")  # TODO: Update to read from env
    # Create database and tables
    headers_and_types = get_csv_metadata(BytesIO(file_data))
    ci.create_database(database)
    ci.create_table(database,
                    table,
                    list(headers_and_types.keys()),
                    list(headers_and_types.values()),
                    primary_keys)
    # Ingest data
    """
    batch = []
    reader = csv.reader(StringIO(file_data.decode()))
    next(reader)  # Skip first row
    for row in reader:
        batch.append(row)
        if len(batch) > MAX_BATCH_SIZE:
            ci.add_data(database, table, batch)
            batch = []
    if batch:
        ci.add_data(database, table, batch)
    """
    with pd.read_csv(BytesIO(file_data), chunksize=MAX_BATCH_SIZE) as reader:
        for df in reader:
            df = df.replace(np.nan, None)
            ci.add_data(database, table, df.values.tolist())


if __name__ == '__main__':
    file_path = "test-data/AIS_2022_01_01.csv"
    with open(file_path, "rb") as f:
        file_data = BytesIO(f.read())
    metadata = get_csv_metadata(file_data)
