# AI-Powered Pressure Washing Job Predictor

> **Applied Data Science | Python | Regression | Statistical Modeling | Business Analytics**

## Project Summary

While running a residential pressure-washing business, I found that estimating job duration, pricing, and profitability largely depended on intuition. This made scheduling difficult and made it harder to determine whether potential jobs were worth accepting.

I wanted to turn my historical job data into a decision-support tool that could estimate **how long a job would take, what I could reasonably quote, what it would cost, and how profitable it could be**.


I collected and analyzed historical operating data and built regression models in Python using **NumPy, Pandas, SciPy, and Scikit-learn**. I evaluated the models using **10-fold cross-validation and R²**, implemented statistical confidence intervals, and built custom Python classes to organize the prediction and financial calculations.

The final job-duration model achieved an **R² of 0.880**, meaning it explained approximately **88% of the variance** in the observed job-duration data during evaluation.

The program can take an estimated driveway capacity and produce:

* A predicted job-duration range
* A quote range
* Estimated operating expenses
* Estimated net profit

This turned a subjective estimating process into a **data-driven decision-support tool** that can be expanded as more business data is collected.

---

# 1. Project Overview

The predictor uses the estimated number of cars that can fit on a driveway as a primary input to estimate:

* Job duration
* Quote range
* Operating expenses
* Potential net profit

The model is based on historical data collected from my own pressure-washing operations.

The project combines **statistical modeling with business decision-making**, using model predictions as inputs to financial calculations.

---

# 2. Business Applications

## Job Duration

Estimating job duration can help:

* Improve scheduling
* Estimate how many jobs can fit into a workday
* Set realistic customer expectations
* Reduce reliance on intuition when estimating completion times

## Job Quotes

The model provides a general quote range based on historical accepted quotes.

This can help determine whether a potential job is financially worthwhile rather than simply estimating what to charge.

## Expense Prediction

The expense model estimates variable job costs such as:

* Bleach/chemical costs
* Fuel
* Other consumable supplies

## Net Profit

Estimated profit is calculated using:

**Net Profit = Estimated Revenue − Estimated Expenses**

This provides another metric for evaluating potential jobs.

---

# 3. Technical Approach

## Regression Modeling

I analyzed the relationships between driveway size and the target variables.

Because the variables showed relatively strong positive relationships, I experimented with:

* Simple linear regression
* Multiple linear regression

The models were implemented in Python and evaluated using statistical and machine-learning techniques.

---

## Job Duration Model

The primary objective was to estimate job duration based on driveway size.

The basic regression model follows:

**y = β₀ + β₁x**

Where:

* `x` = estimated driveway capacity
* `y` = estimated job duration
* `β₀` = intercept
* `β₁` = regression coefficient

The regression parameters are used to calculate the expected duration for a given driveway size.

---

## Statistical Intervals

Rather than returning only a point estimate, the program calculates an interval around the estimate.

The calculations incorporate:

* Mean squared error
* Predictor variance
* Mean predictor value
* Number of observations
* Regression coefficients
* Student's t-distribution

These calculations are used to generate a **95% confidence interval** around the regression estimate.

For the multiple-regression model, I also used matrix-based calculations to determine the standard error associated with the regression estimates.

> A 95% confidence interval represents statistical uncertainty under the assumptions of the model. It should not be interpreted as 95% prediction accuracy.

---

# 4. Model Evaluation

The regression models were evaluated using **10-fold cross-validation** and **R² (coefficient of determination)**.

### Job Duration Model

| Version                     |        R² |
| --------------------------- | --------: |
| Initial regression pipeline |     0.757 |
| Revised regression pipeline | **0.880** |

The final model's R² of **0.880** indicates that approximately 88% of the variance in the observed job-duration data was explained by the model during evaluation.

The improvement came after reviewing the underlying Excel data for inconsistencies and refining the modeling pipeline.

### Expense Model

The expense model uses multiple-output regression and was also evaluated using 10-fold cross-validation and R².

During testing, the predicted expenses were generally within approximately a few dollars of the observed values.

Because these expense estimates feed into the profitability calculation, improving this model is important for improving the reliability of the final financial estimates.

---

# 5. Example

### Input

```text
How many cars can fit on the driveway: 20
```

### Job Duration

```text
Lower estimate: 2 hours 51 minutes
Upper estimate: 3 hours 8 minutes
```

### Quote

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

1. Estimate how many cars could fit on the driveway.
2. Enter the estimated driveway capacity.
3. The program calculates:

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

Expand the financial model to incorporate:

* Revenue
* Cost of goods sold (COGS)
* Labor/time cost
* Advertising expenses
* Profit margin
* Customer acquisition cost (CAC)

## Opportunity Cost Calculator

Compare the economics of:

**Door-to-door sales vs. digital advertising**

Potential inputs include:

* Revenue
* Profit margin
* Hourly profit
* Cost per lead
* Lead-to-customer conversion rate
* Advertising spend
* Available working hours

The goal is to determine when the value of the owner's time becomes high enough that spending money on customer acquisition becomes more profitable than manually generating leads.

## Business Scaling Model

Eventually model the business through several stages:

**Lead Generation → Job Economics → Operational Efficiency → Capacity Expansion**

The model could eventually help determine when additional equipment, employees, or additional rigs become economically justified.

---

# 9. Limitations

The current model has several limitations:

* The dataset is primarily based on my own historical jobs.
* Driveway capacity is estimated rather than precisely measured.
* Job duration depends on factors beyond driveway size.
* Surface condition can significantly affect cleaning time.
* Equipment setup and operating conditions can affect duration.
* Historical pricing may not represent optimal market pricing.
* Expense estimates depend on historical consumption patterns.
* Statistical intervals depend on the assumptions of the regression model.
* A larger and more diverse dataset would improve generalizability.

As additional jobs are collected, the model can be retrained with a larger and more representative dataset.

---

# 10. Project Objective

The long-term goal is to turn historical operational data into a **decision-support system for a service business**.

The system is designed to answer:

> **How long will this job take?**

> **What should I charge?**

> **What will it cost me?**

> **How profitable is it?**

> **Is accepting this job worth the opportunity cost?**

This project combines **data science, statistical modeling, software engineering, and real-world business analytics** to solve a problem directly derived from operating a service business.
