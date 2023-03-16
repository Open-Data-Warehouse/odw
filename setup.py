import setuptools

setuptools.setup(
    name="odw",
    description="Open Data Warehouse",
    version="0.0.1",
    packages=setuptools.find_packages(),
    python_requires=">=3",
    install_requires=[
        "pandas",
        "numpy",
        "clickhouse-driver",
        "fastapi",
        "uvicorn[standard]",
        "python-multipart",
        "celery",
        "redis",
        "minio",
    ]
)