# Drops and creates your tables. You run this file to reset your tables before each time you run your ETL scripts.

import psycopg2
from sql_queries import create_stmts, drop_stmts


def create_database():
    # connect to default database
    conn = psycopg2.connect("host=127.0.0.1 dbname=studentdb user=sparkify password=pass123")
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    
    # create sparkify database with UTF8 encoding
    cur.execute("DROP DATABASE IF EXISTS sparkifydb")
    cur.execute("CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0")

    # close connection to default database
    conn.close()    
    
    # connect to sparkify database
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=sparkify password=pass123")
    cur = conn.cursor()
    
    return cur, conn


# Function for droping tables "If already exists"
def drop_tables(cur, conn):
    for query in drop_stmts:
        cur.execute(query)
        conn.commit()


# Function for creating tables "If doesn't exist"
def create_tables(cur, conn):
    for query in create_stmts:
        cur.execute(query)
        conn.commit()


# Main Function
def main():
    cur, conn = create_database()
    
    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


# Executing main function
if __name__ == "__main__":
    main()
    print("Objects Created Successfully !!!")