import pandas as pd
import ibm_db
import matplotlib.pyplot as plt

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

# SQL query to retrieve data from the database (modify as needed)
sql_query = "SELECT * FROM TABLE1"

try:
    # Execute the SQL query and fetch the data into a Pandas DataFrame
    df = pd.read_sql(sql_query, conn)
    
    # Display the first few rows of the dataset
    print("First few rows of the dataset:")
    print(df.head())

    # Get statistics of the dataset
    summary_stats = df.describe()
    print("\nSummary Statistics:")
    print(summary_stats)

    # Generate basic visualizations
    plt.hist(df['numeric_column'], bins=20)
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title('Histogram of Numeric Column')
    plt.show()

except Exception as e:
    print(f"Error during data exploration: {e}")

# Close the database connection
ibm_db.close(conn)
print("Database connection closed.")

