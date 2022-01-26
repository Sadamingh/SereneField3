## Data Science Experiments 1 | Basic Concepts

![exp](../../../Blog/image/exp.png)

### 1. The Basic Definitions

#### (1) Metrics of Interest

The metrics of interest are the statistics that the experiment is meant to investigate. For example,

- **Key Performance Indicators (KPIs)**: which are statistics that quantify something about a business
- **Click Through Rates (CTR)**
- **Average Time on Page**
- **Check Out Rate (COR)**
- **Average Viewing Duration (AVD)**

#### (2) The Definition of Response Variables

The response variable is the variable of the primary interest. This is what needs to be measured for the metrics of interest to be calculated.

#### (3) The Definition of Factors

Factors are also called covariates, explanatory variables, predictors, or features. These variables are thought to influence the response. 

#### (4) The Definition of Levels

Levels are the values that a factor takes on in an experiment. Levels can be either numeric or categorical according to the factors.

#### (5) The Definition of Experiment Conditions 

Experiment conditions are the unique combinations of levels of one or more factors. For a single-factor experiment, the levels are exactly the conditions.

#### (6) The Definition of Experimental Units

The experiment units are the objects that are assigned to the experimental conditions, and on which the response variable is measured. Often in the experiments, the experiment unit is a **person** (i.e. a customer or a user) but it can be something else like **algorithms**.

#### (7) The Definition of Experiment

An experiment is composed of a collection of conditions defined by purposeful changes to one or more factors and the goal is to identify and qualify the differences in response variable values across conditions. In determining whether a factor significantly influences a response, it is necessary to understand how experimental units respond when exposed to each of the corresponding conditions.

#### (8) The Problem of Experiments

It would be nice if we could observe the same units and how they behave in each experimental condition, but we can not do that because we can only observe their response in a single condition. So the counterfactual part is the hypothetical and unobservable value of a unit's response in a condition to which they were not assigned because counterfactuals can not be observed. Therefore, a proxy is required.

The solution for this problem is that we assign different units to different conditions and compare their responses. Ideally, the only difference between the units in each condition is the fact that they are in different conditions, so we want the units to be as homogeneous as possible and this will help facilitate casual influence. Commonly, this can be achieved typically by **randomizator**. 

#### (9) The Definition of Observational Study

In an observational study, there is no measure of control in the data collection process. The data is collected passively and the relationship between the response variable and the factors is observed organically. This hinders our ability to establish causal connections between the factors and the response variable. However, sometimes we have no choice.

#### (10) Experiments Vs. Observational Study

Experiments are good at finding the causal influence but it could also be risky, unethical, and costly. However, the obervational studies have no cost, risk, or ethics concerns but the causal influences can be messy.

### 2. QPDAC Approach

#### (1) The Definition of QPDAC

QPDAC is an data experimenting strategy aims for answering questions with data. It refers to five different phases including,

* Question
* Plan
* Data
* Analysis
* Conclusion

#### (2) Question

Question is to develop a clear statement of the question that needs to be answered. It is important that this is clear, concrete, concise, widely communicated and understood so that all the stakeholders are on the same page. This should also be quantifiable and stated in forms of the metrics of interest.

#### (3) Plan

In the planning stage, the experiment is designed and all pre-experimental questions should be answered. Therefore, we are ought to choose,

* **the responsible variable**
* **the factors**: There are three types of factors including design factors, nuisance factors, and allow-to-vary factors.
  * Design factors: these are factors that we actually manipulate in the experiment and that define the conditions
  * Nuisance factors: these are factors that we anticipate will influence the response. However, we are not interested in investigating these factors and what we have to do is to eliminate the  impact of these variables via blocking.
  * Allow-to-vary factors: these are the factors that we don't control or manipulate, which are commonly the factors we are ignoring or unaware of.
* **the experiment units**
* **the sample size**
* **the sampling mechanism**

#### (4) Data

In the data stage, the data are collected according to the **plan**. It is extremely important that this step be done correctly and the suitability and activeness of the analysis relies on the data being collected correctly.

#### (5) Analysis

In this stage the Data are statistically analyzed to provide an objective answer to the **question**. This is typically achieved by way of estimating parameters, fitting models, and carrying out statistical hypothesis tests. If the experiment was well-designed and the data were collected correctly, this step should be straight forward.

#### (6) Conclusion

In the conclusion stage, the results of the **analysis** are considered and one must draw conclusions about what has been learned. These conclusions should then be clearly communicated to all parties involved in the experiment.