import streamlit as st
import pandas as pd
import statsmodels.api as sm


st.title('Econometric Regressions using ML')

upload = st.file_uploader("upload a csv or a stata file", type=['csv', 'dta'])
if upload is not None:
    if 'csv' in upload.name:
        data = pd.read_csv(upload)
    else:
        data = pd.read_stata(upload)
response = st.textinput('type in the name of your response variable')
regressors = st.textinput('type in the names of your regressor variables')
st.caption('for regressors, please separate your regressors with a comma')

selector = st.radio("select the linear regression method", 
                    ('least squares', 'regularized'))

process = st.button('regress')

if process:
    regressors_list = regressors.rstrip('')
    regressors_list = regressors_list.split(',')

    regressors_data = data[data.columns.intersection(regressors_list)]
    response_data = data[data.columns.intersection(response)]

    if selector = 'least squares':
        model_ols = sm.OLS(response_data, regressors_data).fit()
    else: 
        model_reg = sm.OLS(response_data, regressors_data).fit_regularized()



