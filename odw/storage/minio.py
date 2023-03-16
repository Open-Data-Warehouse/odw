import os
from io import BytesIO
from typing import Tuple

from minio import Minio


def upload_file(file_data: bytes, file_name: str, file_type: str, bucket: str = "ingest") -> Tuple[str, str]:
    # Create MinIO client
    minio_host = os.environ.get("MINIO_HOST") or "localhost"
    minio_port = int(os.environ.get("MINIO_PORT") or 10000)
    minio_access_key = os.environ.get("MINIO_ACCESS_KEY")
    minio_secret_key = os.environ.get("MINIO_SECRET_KEY")
    minio_client = Minio(
        f"{minio_host}:{minio_port}",
        access_key=minio_access_key,
        secret_key=minio_secret_key,
        secure=False
    )
    # Create bucket if it doesn't exist
    if not minio_client.bucket_exists(bucket):
        minio_client.make_bucket(bucket)
    # Push file to bucket
    minio_client.put_object(bucket, file_name, BytesIO(file_data), len(file_data), file_type)
    return bucket, file_name


def get_file(bucket: str, file_name: str) -> bytes:
    # Create MinIO client
    minio_host = os.environ.get("MINIO_HOST") or "localhost"
    minio_port = int(os.environ.get("MINIO_PORT") or 10000)
    minio_access_key = os.environ.get("MINIO_ACCESS_KEY")
    minio_secret_key = os.environ.get("MINIO_SECRET_KEY")
    minio_client = Minio(
        f"{minio_host}:{minio_port}",
        access_key=minio_access_key,
        secret_key=minio_secret_key,
        secure=False
    )
    # Get image
    response = minio_client.get_object(bucket, file_name)
    file_data = response.data
    return file_data
