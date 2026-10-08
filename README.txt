# AI-Powered Pressure Washing Job Predictor

An applied data science project that uses historical pressure-washing job data to estimate **job duration, quote ranges, operating expenses, and potential net profit**.

The project was built around a real business problem: using historical operational data to make better decisions about **scheduling, pricing, expenses, and job profitability** rather than relying entirely on intuition.

---

# 1. Purpose

The predictor uses the estimated number of cars that can fit on a driveway as a primary input to estimate:

* Job duration
* Quote range
* Operating expenses
* Potential net profit

The model is based on historical data collected from my own pressure-washing operations.

Rather than producing only a single estimate, the program uses statistical intervals to represent uncertainty around the predictions.

> **Note:** A 95% confidence interval should not be interpreted as "95% prediction accuracy." The interval represents statistical uncertainty under the assumptions of the underlying model.

---

# 2. Applications

## Job Duration

Estimating job duration can help both the business and the customer.

For the business, it can:

* Improve scheduling
* Estimate how many jobs can fit into a workday
* Reduce reliance on intuition when estimating completion times
* Identify jobs that may take significantly longer than expected

For the customer, it can:

* Provide a more realistic expected completion time
* Help with scheduling a service window
* Set better expectations before the job begins

The model is based on my historical completion times, allowing the estimates to reflect the actual operating characteristics of my business.

---

## Job Quotes

The model provides a general quote range based on historical accepted quotes.

As more jobs are collected, the underlying statistics can be updated to reflect changes in pricing and the business's average job value.

This can help answer:

> **Is this job worth taking?**

rather than simply:

> **What should I charge?**

---

## Expense Prediction

The expense model estimates variable costs associated with completing a job, including:

* Bleach/chemical costs
* Fuel
* Other consumable supplies

These estimates are then incorporated into the profitability calculation.

---

## Net Profit

Potential net profit is derived from estimated revenue and estimated operating expenses.

**Net Profit = Estimated Revenue − Estimated Expenses**

This provides another metric for determining whether a potential job is economically worthwhile.

---

# 3. How It Works

## Regression Modeling

I first analyzed the relationships between driveway size and the target variables.

Because the variables showed relatively strong positive relationships, I experimented with:

* Simple linear regression
* Multiple linear regression

The models were implemented using Python and evaluated using statistical and machine-learning techniques.

---

## Job Duration

The primary goal was to estimate how long a job would take based on driveway size.

The simple regression model follows the general form:

**y = β₀ + β₁x**

Where:

* `x` = estimated driveway capacity
* `y` = estimated job duration
* `β₀` = intercept
* `β₁` = regression coefficient

The regression coefficients were used to calculate the expected duration for a given driveway size.

I then calculated an interval around the estimate to represent uncertainty in the prediction.

---

## Confidence Interval

For the regression analysis, I used statistical quantities including:

* Mean squared error
* Variance of the predictor
* Mean predictor value
* Number of observations
* Regression coefficients
* Student's t-distribution

These calculations were used to generate a **95% confidence interval** around the regression estimate.

For the multiple-regression model, I also used linear algebra and matrix calculations to calculate the standard error associated with the regression estimates.

---

## Revenue Estimation

Revenue is derived from the predicted job duration and the historical gross hourly rate of the business.

This creates a relationship between the statistical model and the business model:

**Predicted Duration → Estimated Revenue**

The revenue calculation therefore combines a model prediction with a business assumption rather than attempting to independently predict revenue.

---

## Profit Estimation

The estimated profit is calculated as:

**Estimated Profit = Estimated Revenue − Estimated Expenses**

The resulting range provides different possible financial outcomes based on the model's estimated duration, quote, and expenses.

---

# 4. Model Performance

The regression models were evaluated using **10-fold cross-validation** and the **R² (coefficient of determination)** score.

## Job Duration Model

The model improved during development:

| Model                       |        R² |
| --------------------------- | --------: |
| Initial regression pipeline |     0.757 |
| Revised regression pipeline | **0.880** |

The final R² of **0.880** means that the model explains approximately **88% of the variance** in the observed job-duration data used during evaluation.

The improvement came after reviewing the underlying Excel data for inconsistencies and refining the modeling pipeline.

---

## Expense Model

The expense model uses multiple-output regression to estimate job-related costs.

The model was also evaluated using **10-fold cross-validation** and R².

The resulting predictions were generally within approximately a few dollars of the observed expense values during testing.

Because expenses represent one of the inputs to the final profitability calculation, improving the expense model can directly improve the quality of the financial estimates.

---

## Model Interpretation

The R² scores indicate that the models capture a substantial portion of the relationships present in the historical dataset.

However, the results should not be interpreted as a guarantee that the model will perform identically on future jobs.

The dataset is primarily based on my own historical pressure-washing operations, so performance may change as:

* More jobs are collected
* Different property types are added
* Pricing changes
* Operating procedures change
* Additional predictors are introduced

---

# 5. Sample Output

### Input

```text
How many cars can fit on the driveway: 20
```

### Predicted Job Duration

```text
Lower estimate: 2 hours 51 minutes
Upper estimate: 3 hours 8 minutes
```

### Estimated Quote Range

```text
Low bid:  $333.47
High bid: $408.21
```

### Estimated Expenses

```text
Bleach: $11–$18
Gas:    ~$6
```

### Estimated Net Profit

```text
Worst-case: $309.47
Best-case:  $391.21
```

These values are model-derived estimates and are not guaranteed outcomes.

---

# 6. How to Use

1. Find a potential residential pressure-washing job.
2. Estimate how many cars could fit on the driveway.
3. Enter the estimated driveway capacity into the program.
4. The program calculates:

   * Estimated job duration
   * Quote range
   * Estimated operating expenses
   * Estimated net profit

For example, many residential driveways may accommodate approximately 4–6 vehicles, although actual driveway size varies significantly between properties.

---

# 7. Technologies

* **Python**
* **NumPy**
* **Pandas**
* **SciPy**
* **Scikit-learn**
* **Linear Regression**
* **Multiple Linear Regression**
* **10-fold Cross-Validation**
* **Statistical Inference**
* **Matrix-based calculations**
* **Custom Python Classes**

---

# 8. Future Work

## Expanded Job Cost Model

The next version will expand the financial model to incorporate:

* Revenue
* Cost of goods sold (COGS)
* Labor/time cost
* Advertising expenses
* Profit margin
* Customer acquisition cost (CAC)

The goal is to evaluate the complete economics of accepting a job rather than evaluating a job based solely on revenue.

---

## Opportunity Cost Calculator

A future version will compare different customer-acquisition strategies, particularly:

**Door-to-door sales**

vs.

**Digital advertising**

The goal is to determine the point at which the value of the owner's time becomes high enough that spending money on customer acquisition becomes more profitable than manually generating leads.

Potential inputs include:

* Revenue
* Profit margin
* Hourly profit
* Cost per lead
* Lead-to-customer conversion rate
* Advertising spend
* Available working hours

This could eventually produce a dynamic **customer acquisition cost threshold** based on the current economics of the business.

---

## Business Scaling Model

The long-term objective is to model the business in stages.

### Stage 1 — Generate Leads

Focus on consistently acquiring enough customers to maintain a healthy schedule.

↓

### Stage 2 — Improve Job Economics

Optimize:

* Pricing
* Expenses
* Profit margins
* Customer acquisition costs

↓

### Stage 3 — Improve Operational Efficiency

Reduce unnecessary job duration and increase the number of jobs that can be completed in a day.

↓

### Stage 4 — Scale Capacity

Once available working hours become the primary constraint, increase capacity through additional equipment, employees, or additional rigs.

---

# 9. Limitations

The model currently has several limitations:

* The dataset is based primarily on my own historical jobs.
* Driveway capacity is estimated rather than measured precisely.
* Job duration depends on factors beyond driveway size.
* Surface condition can significantly affect cleaning time.
* Equipment setup and operating conditions can affect duration.
* Historical pricing may not represent optimal market pricing.
* Expense estimates depend on historical consumption patterns.
* Statistical intervals depend on the assumptions of the regression model.
* A larger and more diverse dataset would improve confidence in the model's generalizability.

These limitations are important because a strong relationship in historical data does not necessarily guarantee the same performance on every future property.

---

# 10. Project Objective

The ultimate goal of this project is to turn historical operational data into a **decision-support system for a service business**.

Instead of relying exclusively on intuition, the system attempts to answer:

> **How long will this job take?**

> **What should I charge?**

> **What will it cost me?**

> **How profitable is it?**

> **Is accepting this job worth the opportunity cost?**

The project combines **statistical modeling, machine learning, and real-world business analysis** to explore how operational data can be used to improve pricing, scheduling, and profitability.
