import ibm_db
import pandas as pd

# Database connection details
db_credentials = {
    "hostname": "0c77d6f2-5da9-48a9-81f8-86b520b87518.bs2io90l08kqb1od8lcg.databases.appdomain.cloud",
    "port": "31198",
    "username": "wxg07204",
    "password": "Nd2mxWrnTz8aU8qK",
    "database": "bludb",
}

# Establish a connection to the IBM Db2 database
conn_str = (
    f"DATABASE={db_credentials['database']};"
    f"HOSTNAME={db_credentials['hostname']};"
    f"PORT={db_credentials['port']};"
    f"PROTOCOL=TCPIP;"
    f"UID={db_credentials['username']};"
    f"PWD={db_credentials['password']};"
)

try:
    conn = ibm_db.connect(conn_str, "", "")
    print("Connected to the IBM Db2 database.")
except Exception as e:
    print(f"Unable to connect to the database: {e}")
    exit(1)

# Load the dataset from a CSV file into a Pandas DataFrame 
# For inserting data, you'll typically need to iterate through your DataFrame rows and execute INSERT statements.

cursor = ibm_db.exec_immediate(conn, "CREATE TABLE cleaning (AverageTemperature FLOAT, Longitude FLOAT)")
for index, row in df.iterrows():
    query = f"INSERT INTO YOUR_TABLE_NAME (AverageTemperature, Longitude) VALUES ({row['AverageTemperature']}, {row['Longitude']})"
    ibm_db.exec_immediate(conn, query)

# Close the database connection
ibm_db.close(conn)
print("Database connection closed.")

