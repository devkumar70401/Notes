# End to End ML Project

Outline:

- Steps in ML Projects
- Illustration through practical set up

## ML Project

- Excellent wine company wants to develop ML model for **predicting wine quality** on certain **physiochemical characteristics** in order to replace expensive quality sensor.
- Let us understand steps involved in addressing the problem
- There are 8 steps in machine learning project

## Steps in ML projects

1. Look at the big picture
2. Get the data
3. Discover and visualize the data to gain insights.
4. Prepare the data for machine learning algorithms.
5. Select a model and train it
6. Fine-tune your model
7. Present the solution
8. Launch, monitor and maintain your system

### A few words of wisdom

- ML is usually a small piece in a big project. e.g. wine quality prediction is a small piece in setting up the manufacturing process.
- Typically 10-15% of time is spent on ML.
- A lot more time is spent on capturing and processing data needed for ML and taking decisions based on output of ML module.
- Needs strong collaboration with domain experts, product managers and eng-teams for successful execution.

---

## Step 1: Look at the big picture

1. Frame the problem
2. Select a performance measure
3. List and check the assumptions

### 1.1 Frame the problem

- What is the input and output?
- What is the business objective? How does the company expects to use and benefit from the model?
  - Useful in problem framing
  - Algorithm and performance measure selection
  - Overall effort estimation
- What is the current solution (if any)?
  - Provides a useful baseline

---



### Design consideration in problem framing

- Is this a **supervised, unsupervised or a RL** problem?
- Is this a **classification, regression** or some other task?
- What is the nature of the output: **single** or  **multiple** outputs?
- Does system need **continuous learning** or **periodic updates**?
- What would be the learning style: **batch** or **online**?

### 1.2 Selection of performance measure

- Regression
  - Mean Squared Error (MSE) or
  - Mean Absolute Error (MAE)
- Classification
  - Precision
  - Recall
  - F1 - score
  - Accuracy

### 1.3 Check the assumptions

- List down various assumptions about the task
- Review with domain experts and other teams that plan to consume ML output.
- Make sure all assumptions are reviewed and approved before coding!

---

## Step 2: Get the data

- Data spread across multiple tables, files or documents with access control.
- Obtain appropriate access controls and authorizations.
- Get familiarized with data by looking at schema and a few rows. (Familiarity with SQL would be useful here.)

### Load basic libraries

```Python
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 
import numpy as np 
```

- Let's first access our data - in this case, we need to download it from the web.
- It's a good practice to create a function for downloading and extracting the data.

```Python
data_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/
			wine-quality-red.csv'
data = pd.read_csv(data_url, sep=';')
```

---



Now that the data is loaded, let's examine it

### 2.1 Check data samples

Let's look at a few data samples with head()  method.
