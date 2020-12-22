import pandas as pd
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima_model import ARIMA
import pmdarima as pm

def make_real_estate_model(df):
    return pm.auto_arima(df['Composite_Benchmark_Change'], start_p=1, start_q=1,
                      test='adf',       
                      max_p=3, max_q=3,
                      m=1,             
                      d=None,           
                      seasonal=False,   
                      start_P=0, 
                      D=0, 
                      Y=df['Composite_Benchmark_Change'],
                      trace=True,
                      error_action='ignore',  
                      suppress_warnings=True, 
                      stepwise=True)

def make_real_estate_predictions(model, df):
    n_periods = 300
    fitted, confint = model.predict(n_periods=n_periods, return_conf_int=True)
    index_of_fc = pd.date_range(df.reset_index().iloc[-1]['Date'], periods = n_periods, freq='d')

    fitted_series = pd.Series(fitted, index=index_of_fc)
    lower_series = pd.Series(confint[:, 0], index=index_of_fc)
    upper_series = pd.Series(confint[:, 1], index=index_of_fc)

    return fitted_series, lower_series, upper_series