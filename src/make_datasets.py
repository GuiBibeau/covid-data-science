import pandas as pd

def make_real_estate_df():
    df = pd.read_excel('../data/raw/home.xlsx')
    # just keeping recent data
    df = df.loc[df['Date'] > '2018-12-01']
    # calculate some monthly changes
    df['Composite_Benchmark_Change'] = df[['Composite_Benchmark']].pct_change()[
        'Composite_Benchmark']
    df = df[['Date', 'Composite_Benchmark_Change']]
    return df


def make_inflation_df():
    df = pd.read_csv('../data/raw/CPI_MONTHLY.csv')
    # keep recent data
    df = df.loc[df['date'] > '2018-12-01']
    # drop other columns
    df = df[['date', 'V41690973']]
    df = df.rename(columns={"date": "Date"})
    # get monthly change
    df['Inflation_Change'] = df[['V41690973']].pct_change()['V41690973'] 
    df = df[['Date', 'Inflation_Change']]
    return df

