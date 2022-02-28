### Lecture 7. Gradient Boosting

#### 1. Adaboosting

Suppose we have a binary classification tree defined as,
$$
\hat{y} = T_m(x) \in \{-1, 1\}
$$
Then the result of of a forest with $M$ trees should be,
$$
\hat{y} = sign(\sum_{m=1}^{M}\alpha_mT_m(x))
$$
Where $\alpha_m$ is the weight of the tree $M=m$.

Because we have,
$$
y \in \{-1, 1\} \\ 
\hat{y} \in \{-1, 1\}
$$
And if $y$ and $\hat{y}$ are correctly classified, we have,
$$
y\cdot \hat{y} > 0
$$
Which is equivalent to,
$$
y\cdot sign(\sum_{m=1}^{M}\alpha_mT_m(x)) > 0
$$
Because the sign won't impact this inequation, then
$$
y\cdot \sum_{m=1}^{M}\alpha_mT_m(x) > 0
$$
If we note $\sum_{m=1}^{M}\alpha_mT_m(x)$ as a function named $f$, then we can write the inequation above as,
$$
y\cdot f(x) > 0
$$
The left term in the binary classification problem is called the **margin**. Therefore, we can write,
$$
margin > 0 \Leftrightarrow y = \hat{y} \\
margin < 0 \Leftrightarrow y \neq \hat{y}
$$
But there remains one condition, and let's see what happens when we have $margin = 0$. This is equivalent to,
$$
y\cdot f(x) = 0
$$
Because,
$$
y \in \{-1,1\}
$$
we must have,
$$
f(x) = \sum_{m=1}^{M}\alpha_mT_m(x) = 0
$$
In this case, we have equal votes from both sides by M trees, so we can not make a clear classification on which class to predict. Because of that, $f(x) = 0$ is actually defined as the **decision boundary** of the two classes.









