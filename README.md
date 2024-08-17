
# Data Analysis Project

## Overview

This project focuses on collecting and analyzing sugar futures prices data through web scraping, followed by data cleaning, feature engineering, and predictive modeling. The primary goal is to gain insights into historical trends and use predictive techniques to estimate future prices.

The project involves:
1. Implementing a web scraping code to extract data from a website.
2. Converting the scraped data into a structured Excel format.
3. Cleaning and processing the data to make it ready for analysis.
4. Performing exploratory data analysis (EDA) to uncover trends and insights.
5. Building a predictive model to forecast future prices.

## Contents

- **Data Analysis.ipynb**: Jupyter Notebook containing detailed data analysis, visualization, and predictive modeling.
- **historical_data.xls**: The data obtained through web scraping, converted into Excel format using Python.
- **web_scraping_script.py**: Python script used for web scraping the sugar futures prices data.

## Dataset

The dataset scraped from the web includes the following columns:

- **Date**: Date of the record.
- **Price**: Closing price of sugar futures.
- **Open**: Opening price of sugar futures.
- **High**: Highest price of sugar futures on the given date.
- **Low**: Lowest price of sugar futures on the given date.
- **Vol.**: Trading volume (in thousands).
- **Change %**: Percentage change in price from the previous day.
- **Day**: Day of the month (extracted from Date).
- **Month**: Month of the year (extracted from Date).
- **Year**: Year of the record (extracted from Date).

## Data Processing

1. **Web Scraping**: Data was collected using a Python-based web scraping script that extracts sugar futures price data from a financial website.
2. **Data Cleaning**: Cleaned the scraped data, handled missing values, and standardized column names.
3. **Feature Engineering**: Extracted `Day`, `Month`, and `Year` from the `Date` column for further analysis.
4. **Normalization**: Standardized the trading volume data for consistency.
5. **Data Type Conversion**: Ensured proper data types for columns, converting to integer and float formats where applicable.

## Analysis

### 1. **Exploratory Data Analysis (EDA)**:
   - Explored historical price trends over time.
   - Analyzed yearly trends to find the highest average prices.
   - Visualized relationships between features like `Open`, `High`, `Low`, and `Price` to understand price dynamics.

### 2. **Predictive Modeling**:
   - Built regression models using historical data to predict future sugar prices.
   - Visualized the comparison between actual and predicted prices to assess model performance.
   - Used residual plots to evaluate the accuracy of predictions and identify areas for improvement.

## Visualization

Visualizations created in this project include:
- **Price Over Time**: A line plot displaying the trend of closing prices over time.
- **Actual vs. Predicted Prices**: A scatter plot comparing predicted prices against actual prices.
- **Residual Plot**: A scatter plot showing the residuals of the predictions to assess model performance.

## Requirements

To run the code and analysis, you will need the following Python packages:

- pandas
- numpy
- matplotlib
- scikit-learn
- beautifulsoup4 (for web scraping)
- requests (for web scraping)

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

4. Run the web scraping script to collect data:

    ```bash
    python web_scraping_script.py
    ```

5. Open the Jupyter Notebook to perform analysis:

    ```bash
    jupyter notebook Data Analysis.ipynb
    ```

## Acknowledgments

- [pandas](https://pandas.pydata.org/)
- [numpy](https://numpy.org/)
- [matplotlib](https://matplotlib.org/)
- [scikit-learn](https://scikit-learn.org/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- [requests](https://docs.python-requests.org/)
