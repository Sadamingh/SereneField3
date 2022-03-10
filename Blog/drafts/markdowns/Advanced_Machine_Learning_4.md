### Advanced Machine Learning 4 | Neural Networks

![aml](../../image/aml.png)

#### 1. Introduction of Neural Networks

**(1) Recall: Logistic Regression**

Remember we have a logistic model which is a linear model with a sigmoid function in the end. The loss function of this model is,
$$
L = - [ y\log\hat{y} + (1-y)\log(1-\hat{y})]
$$
Recall the reason why we use a sigmoid function in the end is that we would like to make the final decision function differentiable compared with a indication function.

**(2) Recall: Backpropagation**

Recall in the section 2, we have talked about the backpropagation and it is used for computing the gradient of the loss function on parameters. It is actually a special case of a more general algorithm called reversemode automatic differentiation that can compute the gradient of any differentiable function efficiently.

**(3) Basic Model of Neural Network**

Now, let's see the basic model of the neural network. Suppose we have the training set $X$ with shape $N \times K$ with $N$ records, and $x^{(i)}$ is the $i^{th}$ record in that training set with length $K$. Then the first layer in the network is defined as the linear layer,
$$
z_1 = \vec{w}_1x^{(i)} + b_1
$$
Then we take the activation function of the result from the first layer, and we have,
$$
a_1 = h(z_1)
$$
Suppose we have a hidden layer with M neurons, then we have,
$$
z_2 = \vec{w}_2a_1 + b_2
$$
And the final output of this network is,
$$
\hat{y}^{(i)} = z_2
$$
We can plot this network as follows.

<img src="../../image/Screen Shot 2022-03-09 at 1.31.11 PM.png" alt="Screen Shot 2022-03-09 at 1.31.11 PM" style="zoom:40%;" />

**(4) Matrix Form of Neural Network**

We have talked about the one record neural network, and now it's time to go through the matrix expressions. It is quite trick that the dataset $X$ is a $N \times K$ matrix and we have to transpose this matrix to $K \times N$ before fitting it into the layer.
$$
Z_1 = W_1X^T + \vec{b}_1
$$
Where, $W_1$ is a matrix of shape $M \times K$ and $\vec{b}_1$ is a column vector with length $M$. As a result, the output $Z_1$ in this layer has a shape of $M \times N$.

The activation layer then takes place to transform $Z_1$ to $A_1$ with the same shape. Then in the hidden layer, the $W_2$ is a matrix with shape $1 \times M$ because we have only one node in the output layer. 
$$
Z_2 = W_2A_1 + b_2
$$
**(5) Number of Parameters in a Neural Network**

Let's continue to see the parameters we have in the network above. The number of the parameters equals the number of elements in all the $W$ matrics and $b$ vectors. Suppose in one layer we have the weights parameter matrix $W_i$ and the intercept vector $\vec{b}_i$. Then the shape of $W_i$ will be,
$$
\text{shape}(W_i) = \text{# of neurons in the next layer} \times \text{# of neurons in the last layer}
$$
And the length of vector $\vec{b}_i$ should be,
$$
\text{len}({\vec{b}_i}) = \text{# of neurons in the next layer}
$$
So in a layer $i$ with the # of neurons in the last layer as $M_{i-1}$ and the # of neurons in the next layer as $M_{i+1}$, we will have the total number of parameters as,
$$
\text{# of params} = (M_{i-1} + 1) \times M_{i+1}
$$
**(6) Example of Neural Network Parameters**

Now, let's see a real case example. Suppose we have a dataset `X` with `N` records and `D` features, and we have two hidden layers with `M_1` neurons and `M_2​` neurons, respectively. Suppose we have a multiple classification problem with the number of classes as `n_classes`. Then how many parameters do we have in the model with the following PyTorch definition?

```
model = nn.Sequential(
          nn.Linear(D, M_1),
          nn.ReLU(),
          nn.Linear(M_1, M_2),
          nn.ReLU(),
          nn.Linear(M_2, n_classes),
          nn.Softmax()
        )
```

So based on the conclusion we have above,

```
# of params in the first layer = (D + 1) * M_1
# of params in the second layer = (M_1 + 1) * M_2
# of params in the last layer = (M_2 + 1) * n_classes
total # of params = (D + 1) * M_1 + (M_1 + 1) * M_2 + (M_2 + 1) * n_classes
```

Note that this result is totally irrelevant to $N$, so the number of the records we used to fit the neural network won't affect the number of parameters we have in that model.

#### 2. Categorical Embedding

**(1) Problems of Traditional Encoding Methods**

For categorical variables, we usually encode them with one-hot encoding or hash encoding. But are these traditional techniques good for deep learning models? Nope, because there are several problems. 

For one-hot encoding,

- **Too many features**: even though we can perform PCA for dimension reduction, this also means that we will lose some information
- **Lose some information**: if we see these informations as completely discrete variables, we will lose some information. For example, the state `california` and `nevada` is close to each other but if we encode them as discrete variables with the same distance, we will lose the position information.

For hash encoding,

* **Hard to find hyperparameter $k$**: we don't actually know how many hyperparameters we should use for this encoding
* **Conflicts between elements**

However, is there a technique that can encode categorical variables from the information it learn from the model? 

**(2) The Definition of Categorical Embedding**

For categorical embedding, we map each value of a categorical variable to a $D$ dimensional vector. So for a class value $o_c$, the embedded value of this class has a length of $D$,
$$
\text{len }E \ o_c = \text{len } e_c = D
$$
Suppose we have $N$ classes for a categorical variable, then the size of the embedding matrix is,
$$
N \times D
$$
If we want to embed a specific class $o_c$, the first step is to find that class in the embeddding matrix by its rows. And then extract that corresponding row $e_c$ as the embedded vector of the class $c$.

**(3) Case Study: Pinterest Related Pins**

Please refer to the following article [Related Pins at Pinterest](https://arxiv.org/pdf/1702.07969.pdf) for more information. 

- Pins: Pins are bookmarks that people use to save content they love on Pinterest.
- Boards: A Pinterest board is a collection where users save specific pins.

Suppose we have the pin ids and we would like to know which pins are related to each other, then what should we do is to, first embedding pins to pin vectors. Consider a pin ID encoded by one-hot encoding $\vec{x}$ with size $M$, where the value $M$ is the maximum ID we have for a pin. Then, we will use the embedding matrix $E$ with size $D \times M$ (where $D$ is the embedding size) for embeding this $\vec{x}$ , 
$$
\vec{e}_x = E\cdot\vec{x}
$$
We can also compute this on a related pin ID and then make it as our target,
$$
\vec{e}_y = E\cdot\vec{y}
$$
Then we will fit the following softmax model,
$$
z = ELU(\vec{e}_x) \\
\hat{\vec{y}} = softmax(Wz + b)
$$
For this model, we can also write it as a matrix form. Suppose we have a dataset $X$ with shape $N \times M$, where $N$ is the number of records in our dataset and $M$ is the maximum number pin ID (we can also call it as vocabulary size). So the model should be,
$$
Z = ELU(E \cdot X^T) \\
\hat{\vec{y}} = softmax(WZ + b)
$$
So in this model we have the number of parameters as,
$$
\text{# of params} = D \times M + (D+1) \times M = (2D + 1)M
$$
We do not use this model for predictions. Intead, we will extract the final embedding matrix $E$ in this model because it perfectly contains the information we need for each pin ID. So in this case, we can then use the transpose of this embedding matrix of $M \times D$ as our training set to fit another KNN model. And the result of that K-nearest neighbourhood model will tell us that the pins that are clustered together are supposed to have strong relations.