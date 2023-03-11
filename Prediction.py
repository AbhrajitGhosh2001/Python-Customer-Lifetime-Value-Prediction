import pandas as pd
from lifetimes import BetaGeoFitter
from lifetimes.plotting import plot_period_transactions
from lifetimes.utils import summary_data_from_transaction_data

# Load dataset
data = pd.read_csv('customer_data.csv')

# Extract relevant columns
summary = summary_data_from_transaction_data(data, 'CustomerID', 'InvoiceDate', monetary_value_col='TotalAmount')

# Fit the BG/NBD model
bgf = BetaGeoFitter(penalizer_coef=0.0)
bgf.fit(summary['frequency'], summary['recency'], summary['T'])

# Print model summary
print(bgf.summary)

# Visualize frequency and recency of purchases
plot_period_transactions(bgf)

# Predict customer lifetime value
summary['clv'] = bgf.customer_lifetime_value(bgf, summary['frequency'], summary['recency'], summary['T'], summary['monetary_value'])
print(summary.head())
