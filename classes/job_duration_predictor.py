import pandas as pd
import numpy as np
from scipy.stats import t


 

class Job:

    def __init__(self, num_cars, x, y, MSE, coef, intercept):
        self.x = x # uses past jobs to determine this one
        self.y = y # same as above
        self.mse = MSE
        self.num_cars = num_cars
        self.coef = coef
        self.intercept = intercept
        self.interval = 0
        self.x_o = 90*num_cars
        self.lower_hours = 0
        self.higher_hours = 0
        self.lower_profit = 0
        self.higher_profit = 0
        pass

    def ci_value(self): #works
        p = 2 # 2 parameters
        n = self.x.shape[0] # subject to change
        dfyx = n - p # degrees of freedom

        x_mean = self.x.mean()['sq_ft_cleaned']
        x_squared_error = np.sum((self.x-x_mean)**2)
        alpha = .025 # 95% CI
        critical_value = np.abs(t.ppf(alpha, dfyx))
        y_hat_standard_error = np.sqrt(self.mse * ((1/n) + (np.square(self.x_o-x_mean) / x_squared_error)))
        interval = y_hat_standard_error * critical_value
        self.interval = interval
        return interval

    def confidence_interval(self, y_prediction): #issue
            # lower limit (many jobs usually take around 2 hours minimum hence the statement)
    
        lower_bound = (y_prediction - self.interval) // 1
        lower_minutes = np.round(((y_prediction % 1) * 60), decimals=0) 

        if lower_bound < 1.5:
            lower_bound = y_prediction // 1
            lower_minutes = np.round(((y_prediction % 1) * 60), decimals=0) 


        # upper limit
        higher_bound = (y_prediction + self.interval) // 1
        higher_minutes = (((y_prediction + self.interval) % 1) * 60).round()

        self.lower_hours = y_prediction - self.interval
        self.higher_hours = y_prediction + self.interval

        return lower_minutes, higher_minutes, lower_bound, higher_bound
    

    def give_estimate(self):

        x_o = 90*self.num_cars # Turns metric into square feet (90 is the area of a car)
        y_prediction = x_o*self.coef + self.intercept # outputs units in hours correct not issue

        self.ci_value()

        lower_minutes, higher_minutes, lower_bound, higher_bound = self.confidence_interval(y_prediction)

        # result
        print(f'The job will take between {lower_bound.item():.2f} hour(s) and {lower_minutes.item():.2f} minute(s) and {higher_bound.item():.2f} hour(s) and {higher_minutes.item():.2f} minute(s)')

    def calculate_quote(self, average_wage):
        lower_bound = self.lower_hours * average_wage
        higher_bound = self.higher_hours * average_wage

        self.lower_profit = lower_bound
        self.higher_profit = higher_bound  

        # result
        print(f'Low bid: {lower_bound.item():.2f} USD\nHigh bid: {higher_bound.item():.2f} USD')








# [Using our model]

# job1 = Job(4) # 20 cars
# job1.give_estimate() # CI of a job that has a driveway of 20 cars in area