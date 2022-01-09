import mysql.connector
from mysql.connector import Error
from getpass import getpass
import time

def create_connection(host_name,user_name, user_password, db_name = None, autocommit=True):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password,
            database=db_name,
            autocommit = autocommit
        )
        if db_name:
            print("Connection to MySQL Database successful")
        else:
            print("Connection to MySQL successful")
    except Error as err:
        print(f"Error: '{err}'")
    
    return connection


def run_sql_query(connection, query , on_success_show = "Query run successfully"):
    cursor = connection.cursor(buffered = True)
    try:
        cursor.execute(query)
        print(on_success_show)
    except Error as err:
        print(f"Error: '{err}'")

    return cursor


def execute_sql_query(connection, query , on_success_show = "Query run successfully"):
    cursor = connection.cursor()

    try:
        cursor.execute(query)
        print(on_success_show)
    except Error as err:
        print(f"Error: '{err}'")
        # Add rollback() ??
    return 


db_create_sql_file_path = 'sql docs/create_expresso_db.sql'


def create_database(connection,  db_create_sql_file_path):
    sql_file = open( db_create_sql_file_path)
    # Create the string query
    db_create_query= sql_file.read()
    show_db_created = "Database Created Succesfully "

    execute_sql_query(connection, db_create_query ,show_db_created )

    return


def insert_data_to_sql(connection, path_to_sql_file):
    
    try:
        sql_file = open(path_to_sql_file)
        # create a query string that will be executed
        file_upload_query = sql_file.read()
        show_data_inserted = "Data Inserted"
        execute_sql_query(connection, file_upload_query, show_data_inserted)
        

    except Error as err:
        print(f"Error: '{err}'")
        # Add rollback() ??

    
    return


user_name="root"
host_name="localhost"
user_password = getpass()
db_name = "expresso_churn"


initial_connection = create_connection(host_name, user_name, user_password)

'''
Check if database exists:
- If not ,Create it
- If it exists just connect
'''
show_db_query = "SHOW DATABASES"
all_dbs = run_sql_query(initial_connection,show_db_query,"List of Databases retrieved")


if any(db[0] != db_name for db in all_dbs):
    #Create the database
    create_database(initial_connection, db_create_sql_file_path)

try:
    all_dbs.close()
    initial_connection.close()
except:
    pass



# Sometimes the server is too slow so you can run a query
# Sleep allows for the db to finish fully creation before inserting data 
time.sleep(4)
db_connect  = create_connection(host_name,user_name, user_password, db_name)
insert_data_to_sql(db_connect,'sql docs/expresso_train_data_loader.sql')

#Also insert the data from test to the users table
insert_data_to_sql(db_connect,'sql docs/expresso_test_data_loader.sql')

# Add Churn Data
insert_data_to_sql(db_connect,'sql docs/churn_table_loader.sql')

time.sleep(4)
db_connect.close()

