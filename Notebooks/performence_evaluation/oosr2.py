import numpy as np
#OosR^2 function
def calculate_oos_r2(y_true, y_pred):

    # Initialize the sum of squared residuals and total sum of squares
    ss_res = 0
    ss_tot = 0

    for y_true, y_pred in zip(y_true, y_pred):
        # Calculate the mean of the actual implied volatilities for the current period
        y_mean = np.mean(y_true)

        # Sum of squared differences between actual and forecasted implied volatilities
        ss_res += np.sum((y_true - y_pred) ** 2)

        # Sum of squared differences between actual implied volatilities and their mean
        ss_tot += np.sum((y_true - y_mean) ** 2)

    # Calculate the out-of-sample R^2
    oos_r2 = 1 - (ss_res / ss_tot)

    return oos_r2

print(calculate_oos_r2([1,5,3], [1,2,3]))
 