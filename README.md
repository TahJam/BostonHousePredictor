# boston_valuation Module

## Overview

The `boston_valuation` module is designed to predict house prices in Boston using Linear Regression. It utilizes a variety of features to make predictions based on a historical dataset. The target variable is the median value of owner-occupied homes in $1000's.

## Features

- **CRIM:** Per capita crime rate by town
- **ZN:** Proportion of residential land zoned for lots over 25,000 sq.ft.
- **INDUS:** Proportion of non-retail business acres per town
- **CHAS:** Charles River dummy variable (= 1 if tract bounds river; 0 otherwise)
- **NOX:** Nitric oxides concentration (parts per 10 million) used to show pollution
- **RM:** Average number of rooms per dwelling
- **AGE:** Proportion of owner-occupied units built prior to 1940
- **DIS:** Weighted distances to five Boston employment centres
- **RAD:** Index of accessibility to radial highways
- **TAX:** Full-value property-tax rate per $10,000
- **PTRATIO:** Pupil-teacher ratio by town
- **B:** 1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town
- **LSTAT:** % lower status of the population

## Target Variable

- **TARGET:** Median value of owner-occupied homes in $1000's

## Dataset

The dataset used in this module was obtained from [this source](http://lib.stat.cmu.edu/datasets/boston) since the original dataset from sci-kit learn has been deprecated.

## Adjusting Predicted Price

The module adjusts the predicted price to reflect today's prices. It uses the median price of a house today (from Zillow) and the median price of a house in the dataset to create a factor. The predicted house price is then multiplied by this factor.

## Usage

To get a predicted house price, use the `get_dollar_est` function with the following parameters:

```python
from boston_valuation import get_dollar_est

predicted_price = get_dollar_est(rm, ptratio, chas=False, large_range=True)
```

Parameters:
- `rm`: Number of rooms in the property.
- `ptratio`: Number of students per teacher in the classroom for the school in the area.
- `chas`: True if the property is next to the river, False otherwise. Default is False.
- `large_range`: True for a 95% prediction interval, False for a 68% interval. Default is True.

## Example

```python
predicted_price = get_dollar_est(6, 20, chas=True, large_range=False)
print(f"Predicted House Price: ${predicted_price}")
```
