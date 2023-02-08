### Advanced Machine Learning 1 | Recommender System

![aml](../../image/aml.png)

#### 1. Trends in Today's Machine Learning

* Smart Compose: autocomplete in gmail
* AlphaGo: Machine Go player
*  Text Translation
  * Pivot Translation: use English as the pivot for translation
  * Zero-Shot Translation: Multilingual Neural Engine
* Text Generation
* Natural Language Processing
* Google Lens
* Now Playing
* Google Duplex
* Transfer Learning: improvement of learning in a new task through the transfer of knowledge from a related task that has already been learned (e.g. works for NLP and CV)
* Clickthrough Rate (CTR) Predictions
* Recommender Systems (e.g. Netflix, Quora, etc.)

#### 2. Recommender System

**(1) The Definition of Recommender System**

 Application that provide to users personalized recommendations about content they may be interested in.

**(2) Types of Recommender System**

* **Content-based System**

  Content-based System uses the similarity between items to recommend items similar to what a user likes.

  * Create **content features** for every item

  * Analysis of **content attributes** of items

* **Collaborative Filtering**

  Collaborative filtering uses similarities between users and items simultaneously to provide recommendations.

  * Uses **past user behaviors**

**(3) Types of User Feedbacks**

* Explicit Feedback: Direct ratings or reviews
* Implicit Feedback: User preference by actions (e.g. purchases, clicks, navigations history)

**(4) The Definition of Utility Matrix**

The utility matrix is a matrix used for showing the degree of preference that as user has for an item. 

```
            item A    item B   item C   item D
user 1        1                           3
user 2                  4        4
user 3                  2                 2
user 4        2                  5
```

We can also write this matrix in a tabular form,

```
user 1      item A      1
user 1      item D      3
user 2      item B      4
user 2      item C      4
user 3      item B      2
user 3      item D      2
user 4      item A      2
user 4      item C      5
```

The downside of this utility matrix is that the data is always very sparse with only 1% valid information. Also, the number of columns (or the number of items) can be very large so that finding matches to less popular items could be difficult.

**(5) Two Types of Collaborative Filtering Systems**

* Memory Based: memorize the utility matrix and make recommendatiions based on the relationship based on the KNN algorithm
* Model Based: fit a parameterized model to give utility matrix and then make recommendations based on that model. The common method of fitting this parameterized model is called matrix factorization or UV decomposition.

**(6) The Definition of Latent Factors**

The latent variables are variables that can not be observed, but they can be inferred from other variables that are observed. 

**(7) Utility Matrix Factorization**

In order to make predictions of the ratings, we have to decompose the utility matrix $Y$. Let's suppose we have $K$ latent factors and the user matrix $U$ is an $M \times K$ matrix (where $M$ is the number of the users), and $V$ is an $N \times K$ matrix (where $N$ is the number of items). So we have,
$$
Y \approx \hat{Y} = UV^T
$$
For example, suppose we have $K = 2$ latent factors with 7 users and 5 items. Then the following matrix fractorization can be give through our definition.

<img src="../../image/Screen Shot 2022-01-27 at 1.00.47 AM.png" alt="Screen Shot 2022-01-27 at 1.00.47 AM" style="zoom:47%;" />

**(8) Matrix Fractorization Optimization** 

To optimize the matrix fractorization, we can construct the loss function as,
$$
Loss = \text{training error} = \frac{1}{N} \sum_{(i, j): r_{i j}=1}\left(y_{i j}-u_{i} v_{j}\right)^{2}
$$
Where $r_{ij} = 1$ if the user $i$ rated item $j$. Otherwise, $r_{ij} = 0$.

Therefore, we have to minimize the loss for optimization.
$$
\min _{u_{i}, v_{j}} Loss
$$
Here, the method we are going to use is the gradient descent, which is generally,
$$
w \leftarrow w + \eta\nabla Loss
$$
We have talked about different gradient methods in [this article](./Blog/posts/IntrotoMachineLearning/2021-11-11_Intro-to-Machine-Learning-2---Linear-Model-Regularization-and-Various-Types-of-Gradient-Descents-2ea9f5aa1294.html) and please review them if you need. Notice that momentum gradient descent is a simple by efficency method that we can use for this optimization. The moving average of the current gradient and the history gradients are defined as,
$$
v \leftarrow \gamma v+(1-\gamma) \nabla Loss
$$
Then,
$$
w \leftarrow w + \eta v
$$
The gradients for the loss function we have above are,
$$
\begin{aligned}
&\frac{\partial E}{\partial u_{i k}}=-\frac{2}{N} \sum_{j: r_{i j}=1}\left(y_{i j}-u_{i} \cdot v_{j}\right) v_{j k} \\
&\frac{\partial E}{\partial v_{j k}}=-\frac{2}{N} \sum_{i: r_{i j}=1}\left(y_{i j}-u_{i} \cdot v_{j}\right) u_{i k}
\end{aligned}
$$
Which can also be written to the matrix form of
$$
\begin{aligned}
&\frac{\partial E}{\partial U}=-\frac{2}{N} \Delta \cdot V \\
&\frac{\partial E}{\partial V}=-\frac{2}{N} \Delta^{T} \cdot U
\end{aligned}
$$
Where $\Delta$ is defined as,
$$
\Delta=\left(Y-U \cdot V^{T}\right) \otimes R 
$$
And $\otimes $ means element-wise multiplication.

**(9) Predictions and Validations**

To make a prediction about the rating of user $i$ to item $j$ based on the model we have fitted, 
$$
\text{prediction}_{ij} = \hat{y}_{ij} = u_{i} v_{j}
$$
Based on the loss function above, we have known that the training error is,
$$
\text{training error} = \frac{1}{N} \sum_{(i, j):\ r_{i j}=1}\left(y_{i j}-u_{i} v_{j}\right)^{2}
$$
Then, suppose we are given a validation set with some user ratings not existing in training set (means $r_{ij} = 0$ ). Then with this new validation set, we can calculate the validation error as,
$$
\text{validation error} = \frac{1}{N} \sum_{(i, j):\ val_{i j}=1}\left(y_{i j}-u_{i} v_{j}\right)^{2}
$$
Where $val_{ij} = 1$ means the data point of user $i$ rated item $j$ in the validation set. 