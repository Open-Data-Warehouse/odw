from typing import List

import numpy as np
from clickhouse_driver import Client

CLICKHOUSE_DATA_TYPES = {
    np.dtype('int32'): "Int32",
    np.dtype('int64'): "Int64",
    np.dtype('O'): "String",
    np.dtype('float32'): "Float32",
    np.dtype('float64'): "Float64",
}


class ClickhouseInterface:
    def __init__(self, host: str = "localhost", port: int = 9000, username: str = "default", password:str = ""):
        self.clickhouse_url = f"clickhouse://{username}:{password}@{host}:{port}/default"
        self.client = Client.from_url(self.clickhouse_url)

    def create_database(self, database: str):
        self.client.execute(f"CREATE DATABASE IF NOT EXISTS {database}")

    def create_table(self, database: str, table: str, columns: List[str], data_types: List[str],
                     primary_keys: List[str], engine: str = "MergeTree"):
        statement = f"CREATE TABLE IF NOT EXISTS {database}.{table} ("
        added_column = False
        for col, dtype in zip(columns, data_types):
            if added_column:
                statement += ","
            if col in primary_keys:
                statement += f" {col} {dtype}"
            else:
                statement += f" {col} Nullable({dtype})"
            added_column = True
        statement += f") ENGINE = {engine} PRIMARY KEY ("
        added_primary_key = False
        for primary_key in primary_keys:
            if added_primary_key:
                statement += ","
            statement += primary_key
            added_primary_key = True
        statement += ")"
        print(statement)
        self.client.execute(statement)

    def add_data(self, database: str, table: str, data: List[List[any]]):
        statement = f"INSERT INTO {database}.{table} (*) VALUES"
        args = [tuple(row) for row in data]
        for row in args:
            try:
                self.client.execute(statement, [row])
            except Exception as e:
                print(f"Error inserting row: {row}")
                print(str(e))