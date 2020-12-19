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

def make_portfolio_df():
    RRSP = 'Registered Retirement Savings Plans (RRSPs), Registered Retirement Income Funds (RRIFs), Locked-in Retirement Accounts (LIRAs) and other'
    PRINCIPAL_REDIDENCE = 'Principal residence'
    TFSA = 'Tax Free Saving Accounts (TFSA)'

    df = pd.read_csv('../data/raw/under35.csv')
    df = df[['REF_DATE', 'Assets and debts', 'VALUE']]

    portfolio_metrics = [RRSP, PRINCIPAL_REDIDENCE, TFSA]

    df = df.loc[df['Assets and debts'].isin(portfolio_metrics)]
    df.groupby('REF_DATE')

    df = df.pivot_table(values='VALUE', index='REF_DATE', columns='Assets and debts').reset_index().melt(id_vars='REF_DATE')
    df['Assets and debts'] = df['Assets and debts'].replace({RRSP: 'RRSP', 'Net Worth (assets less debts)': 'Net Worth', TFSA: 'TFSA'})
    return df