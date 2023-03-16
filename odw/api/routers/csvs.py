from typing import List

from fastapi import APIRouter, File, UploadFile, Form

from odw.etl.tasks.ingest import extract_csv_metadata, ingest_csv
from odw.storage.minio import upload_file

router = APIRouter(
    prefix="/csv",
    tags=["CSV Upload"]
)


@router.post("/metadata")
def get_csv_headers_and_types(csv_file: UploadFile = File()):
    minio_bucket, minio_file_name = upload_file(csv_file.file.read(), csv_file.filename, csv_file.content_type)
    result = extract_csv_metadata.delay(minio_file_name, minio_bucket)
    headers_and_types = result.get()
    return {"status": "OK", "metadata": headers_and_types}


@router.post("/")
def upload_csv_file(dataset: str = Form(),
                    table: str = Form(),
                    primary_keys: List[str] = Form(),
                    csv_file: UploadFile = File()):
    # Handle case where Swagger UI produces invalid curl request: https://github.com/tiangolo/fastapi/discussions/8741
    # This produces a comma-separated string a single list element, rather than multiple list elements
    if len(primary_keys) == 1 and "," in primary_keys[0]:
        primary_keys = primary_keys[0].split(",")
    minio_bucket, minio_file_name = upload_file(csv_file.file.read(), csv_file.filename, csv_file.content_type)
    result = ingest_csv.delay(minio_file_name, minio_bucket, dataset, table, primary_keys)
    success = result.get()
    return {"status": "OK", "success": success}
