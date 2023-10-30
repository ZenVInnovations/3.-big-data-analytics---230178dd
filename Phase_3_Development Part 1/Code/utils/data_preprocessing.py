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

# SQL query to retrieve your dataset from the database
sql_query = "SELECT * FROM cleaning"  

try:
    # Execute the SQL query and fetch the data into a Pandas DataFrame
    df = pd.read_sql(sql_query, conn)
    
    #  Function for handling missing values
    def handle_missing_values(df):
        df.dropna(inplace=True)
        return df

    # Function for standardizing numeric columns
    def standardize_numeric_column(df, column_name):
        mean_value = df[column_name].mean()
        std_deviation = df[column_name].std()
        df['standardized_' + column_name] = (df[column_name] - mean_value) / std_deviation
        return df

    df = handle_missing_values(df)
    df = standardize_numeric_column(df, 'AverageTemperature')  

except Exception as e:
    print(f"Error during data retrieval or data preprocessing: {e}")

# Close the database connection
ibm_db.close(conn)
print("Database connection closed.")
