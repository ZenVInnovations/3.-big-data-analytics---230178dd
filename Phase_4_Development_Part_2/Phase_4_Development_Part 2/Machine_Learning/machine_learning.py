# machine_learning.py
# This script applies machine learning algorithms to the dataset.

# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Database connection details
db_credentials = {
   "hostname": "your_db_hostname",
    "port": "your_db_port",
    "username": "your_db_username",
    "password": "your_db_password",
    "database": "your_db_name",
}

# Establish a connection to the database
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
sql_query = "SELECT * FROM your_table_name"

try:
    # Execute the SQL query and fetch the data into a Pandas DataFrame
    df = pd.read_sql(sql_query, conn)

    # Split the dataset into features (X) and the target (y)
    X = df.drop('target_column', axis=1)
    y = df['target_column']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create and train a machine learning model
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    # Evaluate the model
    accuracy = model.score(X_test, y_test)
    print(f"Model Accuracy: {accuracy:.2f}")

except Exception as e:
    print(f"Error during data retrieval or model training: {e}")

# Close the database connection
ibm_db.close(conn)
print("Database connection closed.")
