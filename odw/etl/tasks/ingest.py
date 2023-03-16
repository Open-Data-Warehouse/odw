from io import BytesIO
from typing import Dict, List

from odw.etl.tasks.celery import app
from odw.ingest.csvs import get_csv_metadata, push_csv_to_clickhouse
from odw.storage.minio import get_file


@app.task()
def extract_csv_metadata(file_name: str, minio_bucket: str) -> Dict[str, str]:
    file_data = get_file(minio_bucket, file_name)
    return get_csv_metadata(BytesIO(file_data))


@app.task()
def ingest_csv(file_name: str, minio_bucket: str, dataset: str, table: str, primary_keys: List[str]) -> bool:
    file_data = get_file(minio_bucket, file_name)
    push_csv_to_clickhouse(file_data, dataset, table, primary_keys)
    return True
