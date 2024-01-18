# Boston Valuation Module

## Overview

The Boston Valuation module is a Python module that utilizes Linear Regression to predict house prices in Boston. It takes into account various features related to different town attributes and provides an estimate of the median value of owner-occupied homes in $1000's.

## Features

The module uses the following features for prediction:

- `CRIM`: Per capita crime rate by town
- `ZN`: Proportion of residential land zoned for lots over 25,000 sq.ft.
- `INDUS`: Proportion of non-retail business acres per town
- `CHAS`: Charles River dummy variable (1 if tract bounds river, 0 otherwise)
- `NOX`: Nitric oxides concentration (parts per 10 million) for pollution
- `RM`: Average number of rooms per dwelling
- `AGE`: Proportion of owner-occupied units built before 1940
- `DIS`: Weighted distances to five Boston employment centers
- `RAD`: Index of accessibility to radial highways
- `TAX`: Full-value property-tax rate per $10,000
- `PTRATIO`: Pupil-teacher ratio by town
- `LSTAT`: Percentage of lower status of the population

## Target Values

- `TARGET`: Median value of owner-occupied homes in $1000's

## Dataset

The dataset used for training the model is no longer available in sci-kit learn. However, you can find the dataset [here](http://lib.stat.cmu.edu/datasets/boston).

## Adjustment for Today's Prices

The module adjusts the predicted price to reflect today's prices using the median price of a house today (from Zillow) and the median price of a house in the dataset. It creates a factor by dividing these two values and multiplies the predicted house price with this factor.

## Function: get_dollar_est

The core function of the module is `get_dollar_est`, which takes the following parameters:

- `rm`: Number of rooms in the property.
- `ptratio`: Number of students per teacher in the classroom for the school in the area.
- `chas` (Optional): True if the property is next to the river, False otherwise. Default is False.
- `large_range` (Optional): True for a 95% prediction interval, False for a 68% interval. Default is True.

The function returns three values:

1. A rounded estimate of the house price.
2. The high end of the estimate interval.
3. The low end of the estimate interval.

## Usage

```python
from boston_valuation import get_dollar_est

# Example usage
rm = 5
ptratio = 20
chas = True
large_range = False

estimate, high_estimate, low_estimate = get_dollar_est(rm, ptratio, chas, large_range)
print(f"Estimated house price: ${estimate} (Interval: ${low_estimate} - ${high_estimate})")
```
