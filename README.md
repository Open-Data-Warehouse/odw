# Open Data Warehouse

Open Data Wareehouse is a Free and Open Source platform that provides
data lake and data warehouse capabilities. Example use cases include:

- Ingesting a CSV file, automatically inferring column names and data types, and inserting the data into a SQL database.
- Ingesting and storing a variety of multimedia files in an object store.

## Services:

Open Data Warehouse provides the following services:

- Object Storage: MinIO
- SQL Database: Clickhouse
- Full Text Search Database: OpenSearch
- Data Visualization: Apache Superset
- Data Ingest: OWD Ingest Service

## Setup

1. Copy `example.env` to `.env`. Update usernames and passwords as appropriate.
2. Run the first time setup script: `./firstTime.sh`
3. Start up the storage services: `make up-init`
4. Log into MinIO (http://<hostname>:10000) and create an access token. Copy the access key and secret key to the appropriate values in `.env`
5. Start all the services: `make up`
6. The services should now be available at the following locations:
    - MinIO: http://<hostname>:10000
    - Clickhouse: http://<hostname>:8123, native queries at <hostname>:9000
    - Opensearch: <hostname>:9200
    - Superset: http://<hostname>:8888
    - ODW Ingest Service: http://<hostname>:8000/docs

## License

Each individual service retains its own Free and Open Source license.

All software developed under the Open Data Warehouse project are licensed under the Mozilla Public License 2.0.