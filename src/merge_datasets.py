import pandas as pd

def merge_realestate_df(real_estate_df, inflation_df):
    real_estate_df['Inflation_Change'] = inflation_df['Inflation_Change'].values
    real_estate_df['Zero'] = 0
    return real_estate_df[['Date', 'Zero', 'Composite_Benchmark_Change', 'Inflation_Change']]
