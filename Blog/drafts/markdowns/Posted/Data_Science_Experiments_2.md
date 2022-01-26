## Data Science Experiments 2 | Fundamental Principles and Two-Condition Experiments

![exp](../../../Blog/image/exp.png)

### 1. Fundamental Principles for Data Science

#### (1) The Definition of Randomization

Randomization refers both to the manner in which experimental units are selected for inclusion in the experiment and the manner in which they are assigned to experimental conditions. Basically, we have two levels of randomization,

* 1st Level Randomization: this exists to ensure the sample of units included in the experiment is **represnetative** of those that were not. This allows us to generalize conclusions beyond the units in the experiment.
* 2nd Level Randomization: this exists to **balance** the effects of extraneous variables not under study, for example, the allowed-to-vary factors. Balancing the effects if the allowed-to-vary factors makes out conditions homogeneous and thus best mimics the conterfactual, thereby making causal influence easy.

#### (2) The Definition of Replication 

Replication refers to the existence of multiple response observations within each experimental condition and thus corresponds to the situation in which more than one unit is assigned to each condition. This means to assign multiple units to each condition and it provides assurance that the observed results are genuine and not just due to chance. 

To decide how many units should be assigned to each condition, power analysis and sample size calculations help to answer this. 

#### (3) The Definition of Blocking

Blocking is the mechanism by which the **nuisance factors** are controlled for. To eliminate the influence of nuisance factors, we hold them fixed during the experiment, and then run the experiment at fixed levels of nuisance factors, or so-called, within blocks. 

### 2. Experiments with Two Conditions

#### (1) The Definition of A/B Test

Next up, let's consider the design and analysis of an experiment consisting of two experimental conditions or what many data scientists broadly refer to as **A/B Testing**. For example,

* Button color experiment
* List view vs. tile view
* Checkout ressurances
* Host landing page redesign

* etc.

Typically, the goal of A/B test is to decide which condition is optimal with respect to some **metric of interest** $\theta$, which could be,

* Mean: average viewing duration, average revenue per customer
* Proportion: CTR, COR, bounce rate, conversion rate, retention rate
* Variance
* Quantile: meadian, 95% percentile of page load time
* Technically, any other statistics can be satisfied

#### (2) Hypothesis Testing

Even though we get the MOI of one sample surpasses the MOI of another, we are not able to confirm  which condition is better. Formally, such a question should be phrased as a statisical hypothesis that we test using the data collected from the experiment. Typically, we have,

* Two-sided Testing
* One-side Testing

No matter which hypothesis is approprate, the goal is always the same, which is, based on observed data, we will decide whether to reject the null hypothesis $H_0$ or not. A test statistic $T$ should be defined in each of the hypothesis testing.

#### (3) Properties of Testing Statisic

 To define a proper test statistic $T$, we have to make it satisfy three properties,

* It must be a function of the observed data
* It must be a function of the metric of interest $\theta_1$ and $\theta_2$
* Its distribution must not depend on $\theta_1$ and $\theta_2$

#### (4) Procedures of Hypothesis Testing

Assuming the null hypothesis is true, then the test statistic $T$ follows a particular distribution which we called the null distribution. Then, we should,

* Calcluate the observed value $t$ of the test statistic
* Check the relationship of this observed value to the null distribution we have assumed
  * if $t$ is very extreme, this suggest that the null hypothesis should be rejected
  * if $t$ appears as it could have come from the null distribution, we are not able to reject this value and there is no reason to disbelieve the null hypothesis unless the null distribution is mistakenly chosen

The relationship between $t$ and null distribution or the extermity of $t$ is measured using the **p-value**, which is defined as the probability of observing a valu of the test statistic at least as extreme as the value we observed if the null hypothesis is true.

In order to decide how extreme $t$ must be for us to reject the null hypothesis, we should define a threshold called the significant level $\alpha$ so that,

* Reject $H_0$ if $p \leq \alpha$
* Do not reject $H_0$ if $p > \alpha$

#### (5) Type I Error and Type II Error

There are still some probabilities that we may falsely reject or not reject a null hypothesis because of the following reasons,

* Wrong null distribution
* Biased sample
* Improper significant level (too large or too small)
* Etc.

Based on the possible outcomes, we can have two types of errors,

* **Type I Error**: false positive, reject $H_0$ when $H_0$ is true.  

$$
\alpha = P(Type\ I\ Error)
$$

* **Type II Error**: false negative, do not reject $H_0$ when $H_0$ is false

$$
\beta = P(Type\ II\ Error)
$$

The **power** is defined by,
$$
power = 1 -\beta
$$

#### (6) Comparing Two Means: Student's T Test

Suppose we assume that two conditions $Y_{i 1}$ and $Y_{i 2}$ both follow the normal distribution with the same standard deviation,
$$
Y_{i 1} \sim \mathrm{N}\left(\mu_{1}, \sigma^{2}\right) \text { and } Y_{i 2} \sim \mathrm{N}\left(\mu_{2}, \sigma^{2}\right)
$$
with the sample size $n_1$ and $n_2$, respectively. 

Then the student's T test is defined as,
$$
T=\frac{\left(\bar{Y}_{1}-\bar{Y}_{2}\right)-\left(\mu_{1}-\mu_{2}\right)}{\sigma\sqrt{\frac{1}{n_{1}}+\frac{1}{n_{2}}}} \sim t_{\left(n_{1}+n_{2}-2\right)}
$$
In an observarion, we only have estimated value of $\hat{\mu}_{1}$ and $\hat{\mu}_{2}$ with estimated overall sample standard deviation $\hat{\sigma}$. Also, under the null hypothesis $\mu_{1} = \mu_{2}$, we could derive that $\mu_{1} - \mu_{2} = 0$. So we have,
$$
t = \frac{\hat{\mu}_{1}-\hat{\mu}_{2}}{\hat{\sigma} \sqrt{\frac{1}{n_{1}}+\frac{1}{n_{2}}}}
$$
Note that the estimated overall sample variance should the unbiased arithmetic mean of the observed variances,
$$
\hat{\sigma}^{2}=\frac{\left(n_{1}-1\right) \hat{\sigma}_{1}^{2} \cdot\left(n_{2}-1\right) \hat{\sigma}_{2}^{2}}{n_{1}+n_{2}-2}
$$
And the observed variances for each condition should be calculated by,
$$
\hat{\sigma}_{j}^{2}=\frac{1}{n_{j}-1} \sum_{i=1}^{n_{j}}\left(y_{ij}-\bar{y}_{j}\right)^{2}
$$

#### (7) Comparing Two Means: Welch's T Test

Suppose we assume that two conditions $Y_{i 1}$ and $Y_{i 2}$ both follow the normal distribution, but with different standard deviation. This is less common in practice but we may also find it hard to confirm that the two conditions have the same standard deviation. So, 
$$
Y_{i 1} \sim \mathrm{N}\left(\mu_{1}, \sigma_1^{2}\right) \text { and } Y_{i 2} \sim \mathrm{N}\left(\mu_{2}, \sigma_2^{2}\right)
$$
Where,
$$
\sigma_{1} \neq \sigma_{2}
$$
The test statistic for Welch's T test is,
$$
T=\frac{\left(\bar{Y}_{1}-\bar{Y}_{2}\right)-\left(\mu_{1}-\mu_{2}\right)}{\sqrt{\frac{\hat{\sigma}_{1}^{2}}{n_{1}}+\frac{\hat{\sigma}_{2}^{2}}{n_{2}}}}\ \ \dot \sim \ \ t({\nu})
$$
Where,
$$
\nu=\frac{\left(\frac{\hat{\sigma}_{1}^{2}}{n_{1}}+\frac{\hat{\sigma}_{2}^{2}}{n_{2}}\right)^{2}}{\frac{\left(\hat{\sigma}_{1}^{2} / n_{1}\right)^{2}}{n_{1}-1}+\frac{\left(\hat{\sigma}_{2}^{2} / n_{2}\right)^{2}}{n_{2}-1}} \approx \min \left(n_{1}, n_{2}\right)-1
$$
Similarly, we have the observed $t$ parameter as,
$$
t=\frac{\hat{\mu}_{1}-\hat{\mu}_{2}}{\sqrt{\frac{\hat{\sigma}_{1}{ }^{2}}{n_{1}}+\frac{\hat{\sigma}_{2}{ }^{2}}{n_{2}}}}
$$

#### (8) Comparing Two Variances: F Test

In order to decide whether we can treate two different conditions with the same variance, we can perform another test called F test. If the result of F test shows that if we are able to use the Student's T test or the Welch's T test. The test statistic $T$ is defined as,
$$
T=\frac{\sigma_{1}^{2}}{\sigma_{2}^{2}} \sim F_{\left(n_{1}-1,\ n_{2}-1\right)}
$$
Similarly, we have the observed $t$ parameter as,
$$
t=\frac{\hat{\sigma}_{1}{ }^{2}}{\hat{\sigma}_{2}{ }^{2}}
$$

#### (9) Comparing Two Proportions

Next up, if we restrict the attention to the situation which the response variable of interest is binary, indicating whether an experimental unit did, or did not, perform some action of interest (e.g. click a button, sign up for email, bounce from webpages). In case like these we have the response variable $Y_{ij}$ follows,
$$
Y_{ij}\ \sim\ \text{BIN}(1, \pi_j)
$$
where $\pi_j$ represents the probability that $Y_{ij} = 1$.

Under this situation, we should use the observed data for hypothesis testing on the proportions. So the T statistics should be,
$$
T=\frac{\left(\bar{Y}_{1}-\bar{Y}_{2}\right)-\left(\pi_{1}-\pi_{2}\right)}{\sqrt{\pi (1-\pi)}\left(\frac{1}{n_{1}}+\frac{1}{n_{2}}\right)}  \ \ \dot \sim\ \ \mathrm{N}(0,1)
$$
This is a Z test because the null distribution is a normal distribution. Under the observed data, we have,
$$
t=\frac{\hat{\pi}_{1}-\hat{\pi}_{2}}{\sqrt{\hat{\pi}(1-\hat{\pi})\left(\frac{1}{n_{1}}+\frac{1}{\pi_{2}}\right)}}
$$
where,
$$
\hat{\pi}= \frac{n_{1} \hat{\pi}_{1}+n_{2} \hat{\pi}_{2}}{n_{1}+n_{2}}
$$