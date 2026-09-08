# Sparkify Data Warehouse

## Summary
This project illustrates the development of a cloud ELT pipeline of a
dataset from a mock music-streaming startup called Sparkify. The raw
dataset resides in the AWS S3. The pipeline starts by ingesting the raw
data in S3 from the AWS Redshift and creating a staging area for them.
Then in the Redshift itself, the staging dataset is transformed into
the final fact and dimension tables ready for analytical processes.

## Schema
- Staging Tables:
  - `staging_events`
  - `staging_songs`
- Fact Tables:
  - `songplays`
- Dimension Tables:
  - `users`
  - `songs`
  - `artists`
  - `time`

## ELT Insights
- For staging tables, the DLD requires columns of `artist_location`, `artist_name`, and `title` to be `VARCHAR(500)` due to the existance of data points that have long values.
- The fact table has `artist_id` as `DISTKEY` for partitioning and `start_time` as `SORTKEY` for sorting.
- All dimension tables aside from the `artists`, have distribution style of `ALL` to eliminate shuffling.
- The transformation of `start_time` of `songplays` table is from the UNIX milisecond timestamp from the `staging_events` table into a `TIMESTAMP` format.

## Usage
### Requirements
- A Redshift Cluster
- A Redshift Associated IAM Role for S3 Read Access

### Runing the Code
1. Make sure to configure the `dwh.cfg` with your Redshift and IAM details.
2. Run `create_tables.py` to create staging, fact, and dimension tables.
3. Run `etl.py` to populate the staging tables and transform their data and insert them into the fact and dimension tables.


## File Description
- `create_tables.py`: python script to instantiate tables in the Redshift
- `dwh.cfg`: configuration file with AWS credential and endpoints
- `etl.py`: python script to populate staging tables and transform them
- `sql_queries.py`: python script containing SQL queries for creating tables and the ELT process
- `README.md`: markdown file containing this project report


## Contribution
If you want to contribute to this project and make it beter, your help is very welcome.

The following is the general guide on how to contribute to this project:
1. Fork this project & clone it on your local machine
2. Create an upstream remote and sync your local copy before you branch
3. Branch for each piece of work
4. Do the work
5. Push to your origin repository
6. Create a new pull request on GitHub

## License
The content of this project is covered under the [MIT License](./license.txt).