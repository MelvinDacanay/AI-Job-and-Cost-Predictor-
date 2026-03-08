import pandas as pd
import numpy as np
from scipy.stats import t
from sklearn.metrics import mean_squared_error

class Expense:
    def __init__(self, intercept, coef, target_column, x_frame):
        self.x = x_frame # uses local x fix this so that x expenses can be used   
        self.mse = 0
        self.interval = 0 # plus/minus CI value
        self.intercept = intercept # target at 0
        self.coef = coef # coefs the predict this target
        self.target_column = target_column # takes a series
        self.low_bound = 0 
        self.high_bound = 0 
        pass

    def estimate_mse(self):
        y_one = self.target_column # Y values

        y_pred = self.coef[0]*self.x.iloc[:,0] + self.coef[1]*self.x.iloc[:,1] + self.coef[2]*self.x.iloc[:,2] + self.intercept # Y hat regression Y|x1,2,3
        y_hat = pd.DataFrame(y_pred) # Formatting to match y_one

        MSE = mean_squared_error(y_one, y_hat) # Lower means a better line
        self.mse = MSE
        return self.mse

    
    def ci_value(self):

        # DF and params
        p = self.x.shape[1] + 1
        n = self.x.shape[0]
        dfyx = n - p 

        alpha = .025 # 95% CI
        critical_value = np.abs(t.ppf(alpha, dfyx)) # for final calculation
        #fine
        intercept_frame = pd.DataFrame(data=self.intercept, columns=['intercept'], index=self.x.index)
        x = pd.concat(objs=[self.x, intercept_frame], axis=1) # adding intercept to x values

        # multi output standard error calculation
        xtx = np.linalg.inv(x.T @ x)
        cov_beta = xtx* self.mse
        np.diag(cov_beta)
        x_calc = np.array([1, self.coef[0], self.coef[1], self.coef[2]])
        critical_value*np.sqrt(x_calc.T@cov_beta@x_calc)

        interval = critical_value*np.sqrt(x_calc.T@cov_beta@x_calc) # 95% CI
        self.interval = interval
        return interval

    def confidence_interval(self, y_pred, minimum_cost):
        
        # lower limit (many jobs usually take around 2 hours minimum hence the statement)
        # I usually use one jug reguardless 
        y_pred_calc = y_pred - self.interval
        lower_bound = np.round(y_pred_calc, 0).round()
        
        if lower_bound < minimum_cost:
            lower_bound = minimum_cost

        higher_bound = (y_pred + self.interval).round() // 1

        if higher_bound < lower_bound:
            higher_bound = lower_bound

        self.low_bound = lower_bound
        self.high_bound = higher_bound

        return lower_bound, higher_bound

    def estimate_expense(self, amount, sq_feet, duration, minimum_cost):
    
        # Predicting bleach
        y_pred = self.coef[0]*self.x.iloc[:,0] + self.coef[1]*self.x.iloc[:,1] + self.coef[2]*self.x.iloc[:,2] + self.intercept
        y_one = self.target_column


        # Making dataframe of the regression line and the mean line
        y_hat = pd.DataFrame(y_pred)
        mean_line = pd.DataFrame(np.mean(y_one), index=y_one.index, columns=['y_mean'])

        y_table = pd.concat(objs=[y_one, y_hat, mean_line], axis=1)

        y_table.columns = ['y', 'y_regressed', 'y_mean']

        # Making our interval for bleach

        y_pred = self.coef[0]*amount + self.coef[1]*sq_feet + self.coef[2]*duration + self.intercept

        lower_bound, higher_bound = self.confidence_interval(y_pred=y_pred, minimum_cost=minimum_cost)

        lower_bound_string = str(np.round(lower_bound, decimals=1)).strip('[].')
        higher_bound_string = str(np.round(higher_bound, decimals=1)).strip('[].')

        # result
        print(f'You will spend between {lower_bound_string} dollar(s) and {higher_bound_string} dollars on {self.target_column.name}')