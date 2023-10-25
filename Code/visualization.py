import ibm_db
import pandas as pd
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

# SQL query to retrieve your dataset from the database
sql_query = "SELECT * FROM cleaning "  

try:
    # Execute the SQL query and fetch the data into a Pandas DataFrame
    df = pd.read_sql(sql_query, conn)
    
    # Print the column names to verify the correct column names
    print("Column Names:")
    print(df.columns)

    # Define the scatter_plot function
    def scatter_plot(x, y, title, x_label, y_label):
        plt.scatter(x, y, c='blue', marker='o')
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.show()

    # Usage with the loaded DataFrame
    scatter_plot(df['AverageTemperature'], df['Longitude'], "Scatter Plot for AverageTemperature", "AverageTemperature", "Longitude")

except Exception as e:
    print(f"Error during data retrieval or data visualization: {e}")

# Close the database connection
ibm_db.close(conn)
print("Database connection closed.")
