🌧️ Rainfall Prediction & Anomaly Detection in India (1901–2015)

This project focuses on analyzing and predicting rainfall patterns across India using historical data from 1901 to 2015. It uses machine learning and deep learning techniques to predict future rainfall trends and detect anomalies. The system also integrates with IBM Db2 for cloud-based storage and data management.

---

📊 Project Objectives

- Predict rainfall using historical climate data.
- Detect anomalies in rainfall across different regions.
- Perform clustering based on rainfall patterns.
- Forecast rainfall using LSTM deep learning models.
- Store and manage data using IBM Db2 on the cloud.

---

🧰 Technologies Used

🐍 Programming Language
- Python

📦 Libraries & Frameworks

Data Analysis & Visualization
- Pandas, NumPy
- Matplotlib, Seaborn

Machine Learning
- Scikit-learn (Linear Regression, Random Forest, KMeans)
- Evaluation Metrics: MSE, R2 Score, Accuracy, Confusion Matrix, Classification Report

Deep Learning
- TensorFlow, Keras (LSTM model)

Database Integration
- IBM Db2 on Cloud
- ibm_db connector for Python

---

## 🗃️ Dataset

- **Source**: [Rainfall in India 1901–2015]
- **Format**: CSV
- **Columns**: `SUBDIVISION`, `YEAR`, `JAN`, `FEB`, ..., `DEC`, `ANNUAL`

---


---

## ⚙️ Setup Instructions

1. Clone the Repository
   git clone "link"
   cd rainfall-prediction

2. Install Dependencies
   pip install -r requirements.txt
   Set IBM Db2 Credentials

3. Update
   db/db_connection.py with your IBM Db2 credentials.

4. Run Notebooks in Order

    data_cleaning.ipynb → Data preprocessing and EDA

    ml_models.ipynb → Train and evaluate ML models

    lstm_model.ipynb → Build and train LSTM model

📌 Key Features
Real-time analytics and visualization.

Multi-model comparison and evaluation.

Time-series forecasting using LSTM.

Cloud-based data management with IBM Db2.




