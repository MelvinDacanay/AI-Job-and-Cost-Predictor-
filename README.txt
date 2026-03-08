AI powered pressure washing job predictor

1. Purpose

     Just from the size of a persons driveway, this predictor can predict with 95% accuracy
     how long the job will take, how much a person should quote, how much the expenses will be,
     and how much they will make from the job.

2. Implementations

     The duration feature is useful on both the customer end and the business end
          - It enables both the customer and the business to better schedule a slot that works for both parties
          - It also helps automate the process of fitting several jobs into one day which i often struggle with 
          when i try to go off intuition and judgement alone.
          - It sets expectations and the model is tailored around how long it took me to complete my job in the past and
          takes conservative measures (95% CI t-test) into account.

     Job quotes:
          This gives a person a general idea of how much they shoould quote
          the customer. It's based on previous agreed on quotes. One's average value will shift the interval over time
          once they start scaling their business. This helps tell a person if
          its worth taking a job.

     Expense predictors:
          This predicts how much a person will spend on the supplies
          that get used during a job.

     Net Profit:
          simply how much a person makes minus how much they spend.
          Another measure that someone can use to tell them if its worth
          taking a job.

3. How it works
     Since all the values have a reletively strong positive relationship
     I decided to go with linear regression and multiple regression.
     Both already had good scores to begin with so I get to modeling.

     My goal was to essentially get input an amount of cars and recieve
     a 95% confidence interval of how long a job would take

     This is how I did it in simple terms:

          - Using the same model I got the distance of y from the mean
          and the distance from the line
          - I already had the coefficient, and the intercept which I used
          to calculate the hours (y) it took at a number of cars (x)
          - I calculated the confidence interval using the mean squared error
          of the slope, variance of x, mean of x, and the number of observations
          - I ran a 95% CI t test and came out with the interval

          - for multiple regression it was a similar process. 
          I used the same test
          - for standard error I used linear algebra and matrices to
          generate the shape of the interval of our expense

          - For the revenue estimates I multiplied the duration by the average gross
          wage of operations

          - I then computer the profit by subtracting the expense from 
          revenue
     
4. Tools used:
     I used numpy, pandas, scikit learn, scipy, and created my own classes as well

5. Sample output:

How many cars can fit on the driveway: 20
The job will take between 2.00 hour(s) and 51.00 minute(s) and 3.00 hour(s) and 8.00 minute(s)

Low bid: 333.47 USD
High bid: 408.21 USD

You will spend between 11 dollar(s) and 18 dollars on bleach_cost
You will spend between 6 dollar(s) and 6 dollars on gas_cost

Worst case net profit: 309.47
Best case net profit: 391.21

6. How to use it:

     Simply find a driveway in your neighborhood, estimate how many cars are
     able to fit on it by eye (many are 4-6 on average in a residential).
     My program will then do all the calculations for you!

7. Future updates and notes

Notes:
     The cost of a job to me depends on how much money I spend and how much time I spend on it. My goal is to maximize the profit margin.
     I mainly want to maximize the profit margin so that I am able to spend more on lead generation as that is the biggest expense Since
     I dont have any employees. Essentially lead generation is what my business is built upon. There is opportunity cost in my
     situation meaning it is much better if I did door to door (current method) over ads. Door to door is terrible for scaling but im not scaling
     at the moment.

     TLDR: maximize profit margin first (minimize expenses) and maximize leads (MOST IMPORTANT d2d sales shift to digital marketing), 
     once lead generation is solved (constantly booked 2 weeks out) we can then maximize speed (job duration), 
     once the two are resolved we cannot add more hours into our day meaning we must horizontally expand (more rigs in our fleet).

     I will be making a job cost predictor (profit margin, revenue, COGS, advertising expenses):
     - calculates our revenue/wage by calculating the duration
          - uses duration to calculate wage (low vs high bid)
     - desired net profit is calculated
          - revenue - COGS / hours 

future updates:

Oppurtunity cost calculator:
     - using profit we calculate money that we are willing to spend on ads 
          - uses opportunity cost
               - at what point is it more worth it to do online marketing over d2d
               - at what point can I reject low bidders
                    - what makes a job worth it vs not worth it depending on my stage
                         - stage being assessed by revenue and profit margin
                         - make graph on when the d2d and marketing graphs intersect (revenue target vs expenses)
               - once my hourly profit passes a certain value, I am wasting time 
               going d2d when I could be quickly getting leads via marketing 
                    - my time is essentially worth more at scale
          - essentially a stop loss (CPA threshold)
          - based on previous metrics reguarding how much we spent per lead in the past season


Model preformance over time and logging:

1. linear regression + pipeline: .757 (super inconsistent confidence interval)
2. linear regression + pipeline: 
     -.880 (Checked excel data for inconsistencies)
     - x explains 88% of the variance in Y
3. Since im doing linear regression I will do this in SAS
4. manual reg calc not scaling because calculations automatically account 
for variation and less leakage when computing back to initial scales

Model test expense
1. out first multi output regres sor test had us only having values that were ~1$ (square root of 2.7) off the line after rooting the mean squared error, using cross
validation we are only a dollar or so off
     - In the grand scheme, its negligible if my profit margins are greater than 10%
