# Python-Customer-Lifetime-Value-Prediction
Predicts Customer Lifetime Value from csv file

This code assumes that your CSV dataset has columns named CustomerID, InvoiceDate, and TotalAmount. The program first loads the CSV dataset using the pandas library. It then extracts the relevant columns and uses the lifetimes library to fit the BetaGeoFitter model. The program prints a summary of the model and visualizes the frequency and recency of purchases using a built-in function.Finally, the program predicts customer lifetime value using the fitted model and the customer data, and adds the result to the summary dataframe.
