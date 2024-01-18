from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

import pandas as pd
import numpy as np
import re

# get Boston housing data
# Read text from 'boston.txt'
with open('boston.txt', 'r') as file:
    text = file.readlines()
# Column names
cols = ["CRIM", "ZN", "INDUS", "CHAS", "NOX", "RM", "AGE", "DIS", "RAD", "TAX", "PTRATIO", "B", "LSTAT", "Price"]
# strip any whitespace from the beginning of each string and split 
for i, line in enumerate(text):
    temp = line.lstrip()
    temp = re.sub('\s+', ' ', temp)
    text[i] = [float(x) for x in temp.split(' ')[:-1]]
# data[i] = text[i] + text[i+1] when i % 2 == 0
boston_data = []
for i in range(0, len(text) - 1, 2):
    boston_data.append(text[i] + text[i + 1])
# create dataframe 
data = pd.DataFrame(data=boston_data, columns=cols)
# boston_data['Price'] = boston_target
# boston_data.describe()

# split features and target values and transform target (Log prices)
features = data.drop(['INDUS', 'AGE', 'Price'], axis=1)
log_prices = np.log(data['Price'].values)
target = pd.DataFrame(log_prices, columns=['PRICE'])

# populate ndarray with feature means
property_stats = features.mean().values.reshape(1, 11)

regr = LinearRegression().fit(features.values, target['PRICE'].values)
fitted_vals = regr.predict(features.values)
mse = mean_squared_error(target['PRICE'].values, fitted_vals)
rmse = np.sqrt(mse)


def get_log_est(nr_rooms, students_per_classroom, next_to_river=False, high_confidence=True):
    # Configure property
    property_stats[0][4] = nr_rooms  # RM_IDX = 4
    property_stats[0][8] = students_per_classroom  # PTRATIO_IDX = 8
    property_stats[0][2] = 1 if next_to_river else 0  # CHAS_IDX = 2

    # Make prediction
    log_estimate = regr.predict(property_stats)[0]

    # Calc Range 
    if high_confidence:
        upper_bound = log_estimate + 2 * rmse
        lower_bound = log_estimate - 2 * rmse
        interval = 95
    else:
        upper_bound = log_estimate + rmse
        lower_bound = log_estimate - rmse
        interval = 68

    return log_estimate, upper_bound, lower_bound, interval


ZILLOW_MEDIAN_PRICE = 715.9  # taken from Zillow as of 12/14/2023
SCALE_FACTOR = ZILLOW_MEDIAN_PRICE / np.median(data['Price'])


def get_dollar_est(rm, ptratio, chas=False, large_range=True):
    """Estimate the price of a property in Boston.
    
    Keyword arguments:
    rm: number of rooms in the property.
    ptratio: number of students per teacher in the classroom for the school in the area.
    chas: True if the property is next to the river, False otherwise. Default False
    large_range: True for a 95% prediction interval, False for a 68% interval. Default True
    
    """
    if rm < 1 or ptratio < 1:
        raise ValueError('Unrealistic Values given. rm parameter and ptratio parameter must be greater than 1')

    log_est, upper, lower, conf = get_log_est(rm, students_per_classroom=ptratio, next_to_river=chas,
                                              high_confidence=large_range)

    # Convert to today's dollars
    dollar_est = np.e ** log_est * 1000 * SCALE_FACTOR
    dollar_hi = np.e ** upper * 1000 * SCALE_FACTOR
    dollar_low = np.e ** lower * 1000 * SCALE_FACTOR

    # Round the dollar values to the nearest thousandth
    rounded_est = np.around(dollar_est, -3)
    rounded_hi = np.around(dollar_hi, -3)
    rounded_low = np.around(dollar_low, -3)

    return rounded_est, rounded_hi, rounded_low
