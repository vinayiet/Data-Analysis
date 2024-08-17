# Data Analysis Project

## Overview

This project involves performing data analysis on a dataset containing information about sugar futures prices. The analysis includes data cleaning, feature engineering, and predictive modeling to understand historical trends and predict future prices.

## Contents

- **Data Analysis.ipynb**: Jupyter Notebook containing detailed data analysis and visualization.
- **historical_data.xls**: The data which is scrapped from the site is converted into the excel format using python script.


## Dataset

The dataset used in this project includes the following columns:

- **Date**: Date of the record.
- **Price**: Closing price of sugar futures.
- **Open**: Opening price of sugar futures.
- **High**: Highest price of sugar futures on the given date.
- **Low**: Lowest price of sugar futures on the given date.
- **Vol.**: Trading volume (in thousands).
- **Change %**: Percentage change in price from the previous day.
- **Day**: Day of the month.
- **Month**: Month of the year.
- **Year**: Year of the record.

## Data Processing

The following steps were performed on the dataset:

1. **Data Cleaning**: Handled missing values and cleaned column names.
2. **Feature Engineering**: Extracted day, month, and year from the date.
3. **Normalization**: Converted the trading volume from thousands to standard format.
4. **Conversion**: Changed data types of columns to appropriate formats (int, float).

## Analysis

1. **Exploratory Data Analysis (EDA)**:
   - Analyzed the historical price trends over time.
   - Identified the highest average price per year.
   - Created visualizations to show the relationship between different features and the price.

2. **Predictive Modeling**:
   - Used regression models to predict the price based on historical data and features.
   - Compared actual prices with predicted prices using scatter plots and residual plots.

## Visualization

Visualizations included in this project:
- **Price Over Time**: Line plot showing the trend of closing prices over time.
- **Actual vs. Predicted Prices**: Scatter plot comparing the predicted prices with actual prices.
- **Residuals Plot**: Scatter plot of residuals vs. predicted prices to analyze model performance.

## Requirements

To run the code and analysis, you need the following Python packages:

- pandas
- numpy
- matplotlib
- scikit-learn

Install the required packages using the following command:

```bash
pip install -r requirements.txt
```

## How to Use

1. Clone the repository:

    ```bash
    git clone https://github.com/vinayiet/Data-Analysis.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Data-Analysis
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the Jupyter Notebook for analysis:

    ```bash
    jupyter notebook Data Analysis.ipynb
    ```


## Acknowledgments

- [pandas](https://pandas.pydata.org/)
- [numpy](https://numpy.org/)
- [matplotlib](https://matplotlib.org/)
- [scikit-learn](https://scikit-learn.org/)

