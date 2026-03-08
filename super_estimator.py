import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.multioutput import MultiOutputRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

from classes.job_duration_predictor import Job
from classes.expense_predictor import Expense

def get_all_vals_expense():

    # Calling Everything
    df = pd.read_csv('data/pressure_washing_cleaned.csv')
    lr = LinearRegression()
    scaler = StandardScaler()
    mor = MultiOutputRegressor(lr)
    pl = make_pipeline(scaler, mor)

    # Data Processing
    df = df.sample(frac=1, random_state=42).reset_index(drop=True)
    x_expenses = df.drop(columns=['bleach_cost', 'gas_cost'])
    y_expenses = df[['bleach_cost', 'gas_cost']].reset_index(drop=True)


    # Running the model
    # print('training expenses')
    mor.fit(x_expenses, y_expenses) # How every other variable predicts gas and bleach cost
    # print('done training expenses')


    # Important Metrics

    # Isolating each target (B0 is bleach B1 is gas)
    est = pl.named_steps['multioutputregressor'].estimators_
    coef_one = est[0].coef_
    coef_two = est[1].coef_

    intercept_one = est[0].intercept_
    intercept_two = est[1].intercept_

    return x_expenses, y_expenses, coef_one, coef_two, intercept_one, intercept_two

def get_all_vals_duration():

    # Calling Everything
    df = pd.read_csv('data/pressure_washing_cleaned.csv')
    lr = LinearRegression()


    # Data Processing
    df = df.sample(frac=1, random_state=42).reset_index(drop=True)
    x = df.drop(columns=['duration', 'gas_cost', 'amount', 'bleach_cost'])

    y = df['duration'].reset_index()
    y = y.drop(columns='index') # Makes y 2d

    lr.fit(x, y) # Running the model

    # Important Metrics
    coef = lr.coef_
    intercept = lr.intercept_

    # Combining y's into a table
    y_hat = x*coef + intercept
    y_hat = pd.DataFrame(y_hat)

    mean_line = pd.DataFrame(np.mean(y), index=y.index, columns=['y_mean'])

    y_table = pd.concat(objs=[y, y_hat, mean_line], axis=1)
    y_table.columns = ['y', 'y_regressed', 'y_mean']

    MSE = mean_squared_error(y, y_hat) # How good does the line fit Y

    return coef, intercept, MSE, x, y


x_expenses, y_expenses, coef_one, coef_two, intercept_one, intercept_two = get_all_vals_expense()
coef, intercept, MSE, x, y = get_all_vals_duration()

# [Duration]

cars = int(input('How many cars can fit on the driveway: '))
job1 = Job(cars, x, y, MSE, coef, intercept) 
job1.give_estimate()
print()
job1.calculate_quote(130)

# [Expenses]

bleach = Expense(intercept=intercept_one, coef=coef_one, target_column=y_expenses.iloc[:,0], x_frame=x_expenses)
bleach.estimate_mse()
bleach.ci_value()

gas = Expense(intercept=intercept_two, coef=coef_two, target_column=y_expenses.iloc[:,1], x_frame=x_expenses)
gas.estimate_mse()
gas.ci_value()

print()
bleach.estimate_expense(job1.lower_profit, cars*90, job1.lower_hours, 10)
gas.estimate_expense(job1.lower_profit, cars*90, job1.lower_hours, 6)

# [Profit]

print()
print(f'Worst case net profit: {(job1.lower_profit - bleach.high_bound - gas.high_bound).item():.2f}')
print(f'Best case net profit: {(job1.higher_profit - bleach.low_bound - gas.low_bound).item():.2f}')
