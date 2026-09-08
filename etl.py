import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries


def load_staging_tables(cur, conn):
    """
    Loads data from S3 into staging tables.

    Args:
        cur: The cursor object to execute database commands.
        conn: The connection object to commit changes to the database.

    Database Side Effects:
        * COPY: Data from S3 into staging tables.
    """
    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()


def insert_tables(cur, conn):
    """
    Inserts data from staging tables into the final tables.

    Args:
        cur: The cursor object to execute database commands.
        conn: The connection object to commit changes to the database.

    Database Side Effects:
        * INSERT: Data from staging tables into the final tables.
    """
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """Main function to load data from S3 into staging tables and then insert it into the final tables."""
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()
    
    load_staging_tables(cur, conn)
    insert_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()