# AI-Powered Pressure Washing Job Predictor

> **Applied Data Science | Python | Regression | Statistical Modeling | Business Analytics**

## Project Summary

While running a residential pressure-washing business, I found that estimating job duration, pricing, and profitability often relied on intuition, making scheduling and job selection difficult.

Build a data-driven tool that could estimate **job duration, quote ranges, expenses, and potential net profit** from historical business data.

I collected and analyzed historical job data and built regression models using **Python, Pandas, NumPy, SciPy, and Scikit-learn**. I used **10-fold cross-validation and R²** for model evaluation and implemented statistical calculations to generate prediction intervals.

The final job-duration model achieved an **R² of 0.880**, explaining approximately 88% of the variance in the observed duration data during evaluation.

The resulting program converts a simple driveway-size estimate into:

* Estimated job duration
* Quote range
* Operating expense estimate
* Potential net profit

---

## Key Features

* **Job duration prediction** — estimates completion time from driveway size
* **Quote estimation** — produces a historical-data-based quote range
* **Expense prediction** — estimates variable job costs
* **Profit calculation** — combines predicted revenue and expenses
* **Statistical intervals** — represents uncertainty around model estimates
* **10-fold cross-validation** — evaluates model performance using R²

---

## Model Performance

| Model                       |        R² |
| --------------------------- | --------: |
| Initial regression pipeline |     0.757 |
| Revised regression pipeline | **0.880** |

The final model's **R² of 0.880** indicates that approximately 88% of the variance in the observed job-duration data was explained by the model during evaluation.

> R² is not the same as prediction accuracy, and the 95% statistical intervals should not be interpreted as 95% accuracy.

---

## Example

**Input**

```text
Driveway capacity: 20 cars
```

**Output**

```text
Job duration: 2h 51m – 3h 8m

Low bid:  $333.47
High bid: $408.21

Bleach: $11–$18
Gas:    ~$6

Worst-case profit: $309.47
Best-case profit:  $391.21
```

---

## Tech Stack

* Python
* Pandas
* NumPy
* SciPy
* Scikit-learn
* Linear Regression
* Multiple Linear Regression
* 10-fold Cross-Validation
* Statistical Inference
* Custom Python Classes

---

## Future Work

* Expand the dataset with additional jobs and property characteristics
* Add more predictors to improve duration and expense estimates
* Incorporate COGS, advertising expenses, and customer acquisition cost
* Build an opportunity-cost model comparing door-to-door sales with digital marketing
* Develop a business scaling model for determining when additional equipment or labor becomes economically justified

---

## Limitations

* Dataset is primarily based on my own historical jobs.
* Driveway capacity is estimated rather than precisely measured.
* Job duration depends on factors beyond driveway size.
* Historical pricing may not represent optimal market pricing.
* Expense estimates depend on historical consumption patterns.
* Model performance may change as additional and more diverse data is collected.

---

## Project Goal

Turn:

**Historical Business Data → Statistical Model → Job Estimate → Financial Decision**

The project combines **data science, statistical modeling, software engineering, and real-world business analytics** to make operational decisions more data-driven.
