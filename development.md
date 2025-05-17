Phase 3: Development

Objective
The goal of this development phase is to build an end-to-end data analysis pipeline using Python, involving data ingestion from IBM Db2, data transformation, exploratory data analysis (EDA), and implementation of machine learning models for regression, classification, and clustering tasks.
________________________________________
Data Ingestion
✔️ Tools & Libraries Used:
•	ibm_db for connecting to IBM Db2
✔️ Key Tasks:
•	Connected to an IBM Db2 database using appropriate credentials.
•	Parsed a dataset and inserted records into the INDIA_Rainfall table.
•	Used prepared statements and parameter binding for secure and efficient data insertion.
✔️ Highlights:
•	Ensured secure handling of database credentials.
•	Checked success/failure of each insertion operation.
________________________________________
Data Transformation
✔️ Tools & Libraries Used:
•	pandas for data manipulation
✔️ Key Tasks:
•	Retrieved records from a target table using SQL queries.
•	Performed transformations including computed columns using expressions.
✔️ Highlights:
•	Added new derived columns (e.g., scaling a value by a factor).
•	Enabled a cleaner dataset structure for downstream tasks.
________________________________________
Exploratory Data Analysis (EDA)
✔️ Tools & Libraries Used:
•	pandas, matplotlib, seaborn
✔️ Key Tasks:
•	Generating descriptive statistics using data.describe()
•	Creating visualizations to understand the distribution and relationships:
o	Histogram
o	Scatter plot
o	Correlation heatmap
o	Boxplot grouped by categories
✔️ Highlights:
•	Effective visual analysis of trends and patterns.
•	Identified correlations and data anomalies.
________________________________________
Machine Learning Implementation
✔️ Tools & Libraries Used:
•	scikit-learn
________________________________________
📈 a) Linear Regression
•	Trained a model to predict a continuous variable.
•	Used train-test split to evaluate model performance.
•	Evaluated using Mean Squared Error (MSE).
________________________________________
🌲 b) Random Forest Classifier
•	Trained a classifier to predict labels based on features.
•	Assessed using:
o	Accuracy Score
o	Confusion Matrix
o	Classification Report
________________________________________
K-Means Clustering
•	Implemented unsupervised clustering with n_clusters=3.
•	Labeled clusters and visualized them using a scatter plot.
•	Used seaborn for colored cluster visualization.
________________________________________
Challenges & Solutions
Challenge	Solution
Understanding differences in Node.js vs browser JS	Used documentation to clarify global objects and module use
Managing asynchronous fetch in frontend/backend	Used async/await and Promises properly
CORS issues between React frontend and Node backend	Applied correct CORS headers in Express server
JSX and component structuring confusion in React	Gained clarity through practical component planning and JSX familiarity
React form handling and validation	Used controlled components with useState
Complex state management in React	Adopted useReducer and Context API for scalable state logic
________________________________________
Evaluation Metrics
•	MSE (Regression)
•	Accuracy, Confusion Matrix, Classification Report (Classification)
•	Cluster Visualization (Clustering)
________________________________________
Conclusion
This development script effectively demonstrates the use of:
•	Data connection and ingestion using IBM Db2
•	Data manipulation and visualization with Pandas, Matplotlib, and Seaborn
•	Basic and advanced machine learning models using Scikit-learn
•	Full-stack connectivity in the Movie Search app (API + React + Node)
This lays a solid foundation for more complex deployments and analytics features in upcoming phases.
