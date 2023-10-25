import ibm_db
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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
    data = pd.read_sql(sql_query, conn)
    
    # Create and display the bar chart interactively within your Jupyter notebook
    x_column = "your_x_column"  
    y_column = "your_y_column"  
    title = "Your Bar Chart Title"  
    x_label = "X-Axis Label"  
    y_label = "Y-Axis Label" 
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x=data[x_column], y=data[y_column])
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.xticks(rotation=45)
    plt.show()

except Exception as e:
    print(f"Error during data retrieval or data visualization: {e}")

# Close the database connection
ibm_db.close(conn)
print("Database connection closed.")
