## Data Science Experiments 3 | Sample Size Determination and Multiple-Condition Experiments

![exp](../../../Blog/image/exp.png)

### 1. 

#### (1) Rejection Region

Suppose we have a null hypothesis following normal distribution and the T statistic is calculated by,
$$
T=\frac{\left(\bar{Y}_{1}-\bar{Y}_{2}\right)-\left(\theta_{1}-\theta_{2}\right)}{\sqrt{\frac{\operatorname{Var}\left[Y_{1}\right]}{n}+\frac{\operatorname{Var}\left[Y_{2}\right]}{n}}} \sim \mathrm{N}(0,1)
$$
Then it will be useful if we define the **rejection region**, which is the set of all values of the observed test statistic $t$ that would lead to the rejection of $H_0$. This concept is represented by $\mathcal{R}$.

* $t \in \mathcal{R} \Rightarrow \text{Reject}\ H_0$ 
* $t \in \mathcal{R}^c \Rightarrow \text{Do Not Reject}\ H_0$ 











