# Credit Score Predictor

The Credit Score Predictor project aims to assess credit risk by analyzing customer transaction data. The project leverages advanced data processing techniques and machine learning models to predict credit scores and identify potential high-risk customers.

## Features

- **Credit Risk Analysis**: Understand customer behavior and assess creditworthiness.
- **Data-Driven Insights**: Analyze transaction patterns, fraud trends, and spending behavior.
- **Predictive Modeling**: Build and deploy machine learning models for credit score prediction.
- **Interactive API**: Provide real-time predictions through a RESTful API.

## Dataset Overview

The dataset includes customer transaction data with the following key fields:

- **TransactionId**: Unique identifier for each transaction.
- **AccountId**: Unique identifier for each customer account.
- **CustomerId**: Unique identifier for the customer.
- **Amount**: Transaction value (positive for debits, negative for credits).
- **ProductCategory**: Broader category of purchased products.
- **ChannelId**: Indicates the transaction channel (e.g., web, Android, iOS).
- **FraudResult**: Indicates whether the transaction was fraudulent (1 = Fraud, 0 = No Fraud).

## Objectives

- Predict credit scores based on transaction data and customer behavior.
- Identify high-risk customers with a higher likelihood of default.
- Provide actionable insights for better credit risk management.

## Tools and Technologies

- **Python**: Data processing and model development.
- **Pandas & NumPy**: Data manipulation and analysis.
- **Matplotlib & Seaborn**: Data visualization.
- **Scikit-learn**: Machine learning model development.
- **FastAPI**: RESTFull API for model deployment.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Tekalig/credit-score-predictor.git
   cd credit-score-predictor
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   uvicorn app.main:app --reload
   ```

## Usage

- Analyze customer data to derive meaningful insights.
- Train and evaluate predictive models for credit score estimation.
- Deploy the trained model via an API for real-time predictions.

## License

This project is licensed under the Apache License. See the `LICENSE` file for more details.

## Author

- **Tekalign Mesfin** - Developer and Data Scientist