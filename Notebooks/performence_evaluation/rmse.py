import numpy as np
import pandas as pd

def calculate_daily_rmse(df):
    
    # Group by date
    grouped = df.groupby('date')

    # Initialize a list to store the results
    results = 0

    # Iterate over each group
    for date, group in grouped:
        y_true = group['y_true'].values
        y_pred = group['y_pred'].values

        # Ensure the sets are the same length
        if len(y_true) != len(y_pred):
            raise ValueError("Actual and forecasted sets must be of the same length")

        # Calculate the sum of squared errors
        sum_squared_errors = np.sum((y_true - y_pred) ** 2)

        # Add to results
        results += sum_squared_errors

        # # Calculate the RMSE
        # 

        # # Store the result
        # results.append({'date': date, 'RMSE': rmse})
    rmse = np.sqrt(results / len(grouped))

    # Convert the results to a DataFrame
    # results_df = pd.DataFrame(results)

    return rmse

# Create a sample DataFrame
df = pd.DataFrame({
    'date': ['2020-01-01', '2020-01-01', '2020-01-02', '2020-01-02'],
    'y_true': [1, 2, 3, 4],
    'y_pred': [1, 3, 2, 4]
})

# Calculate the RMSE
print(calculate_daily_rmse(df))