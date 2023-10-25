import pandas as pd
import ibm_db
import ibm_db_dbi
# Define your dataset file path
dataset_file = "Data/processed_data/cleaned_dataset1.csv" 
# Database connection details
db_credentials = {
    "host": "0c77d6f2-5da9-48a9-81f8-86b520b87518.bs2io90l08kqb1od8lcg.databases.appdomain.cloud",       
    "db": "bludb",        
    "user": "wxg07204",       
    "password": "Nd2mxWrnTz8aU8qK"  
}
# Establish a connection to the database
conn_str = (
    f"DATABASE={db_credentials['db']};HOSTNAME={db_credentials['host']};"
    f"PORT={db_credentials['port']};PROTOCOL=TCPIP;"
    f"UID={db_credentials['user']};PWD={db_credentials['password']};"
)
try:
    conn = ibm_db.connect(conn_str, "", "")
    print("Connected to the database.")
except Exception as e:
    print(f"Unable to connect to the database: {e}")
    exit(1)
# Read the dataset into a pandas DataFrame
try:
    df = pd.read_csv(dataset_file)
# Insert the DataFrame into the database
    dbi_conn = ibm_db_dbi.Connection(conn)
    df.to_sql("WXG07204", dbi_conn, if_exists="replace", index=False)  

    print("Data successfully ingested into the database.")

except Exception as e:
    print(f"Error ingesting data: {e}")

finally:
    # Close the database connection
    ibm_db.close(conn)
    print("Database connection closed.")
