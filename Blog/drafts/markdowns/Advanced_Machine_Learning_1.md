### Advanced Machine Learning 1 | Recommender System

![aml](/Users/apple/Dropbox/SereneField3/Blog/image/aml.png)

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

**(5) The Definition of Latent Factors**

The latent variables are variables that can not be observed, but they can be inferred from other variables that are observed. 

**(6) Utility Matrix Fractorization**

In order to make predictions of the ratings, we have to decompose the utility matrix $Y$. Let's suppose we have $K$ latent factors and the user matrix $U$ is an $M \times K$ matrix (where $M$ is the number of the users), and $V$ is an $N \times K$ matrix (where $N$ is the number of items). So we have,
$$
Y \approx \hat{Y} = UV^T
$$
For example, suppose we have $K = 2$ latent factors with 7 users and 5 items. Then the following matrix fractorization can be give through our definition.

<img src="/Users/apple/Dropbox/SereneField3/Blog/image/Screen Shot 2022-01-27 at 1.00.47 AM.png" alt="Screen Shot 2022-01-27 at 1.00.47 AM" style="zoom:47%;" />

**(7) Matrix Fractorization Optimization** 

To optimize the matrix fractorization, we can construct the loss function as,
$$
\min _{u_{i}, v_{j}} \frac{1}{N} \sum_{(i, j): r_{i j}=1}\left(y_{i j}-u_{i} v_{j}\right)^{2}
$$
Where $r_{ij} = 1$ if the user $i$ rated item $j$. Otherwise, $r_{ij} = 0$.