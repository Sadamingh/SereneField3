### Advanced Machine Learning 5 | Introduction to NLP

![aml](../../image/aml.png)

#### 1. Natural Language Processing Techniques

**(1) Two NLP Workflows**

* **Classical NLP**: first use the technique to pre-processing the text, then use NLP models for training the data
* **NLP with Deep Learning**: first preprocessing the data (mostly by word embedding), and the train data based on the neural network

**(2) Classical NLP Techniques**

Here is a list of techniques that we use for classical NLP, and we will explain in the following parts of this section.

* Tokenization
* Lemmatization
* Stemming
* Sentence Segmentation
* POS (part of speech) tagging
* NER (named entity recognization)
* Dependency Parsing
* N-Gram Model
* BOW (Bag of word) Model

**(3) Classical NLP Problems**

* Sentiment Analysis
* Reading Comprehension

**(4) Word Representation Techniques**

* WordNet
* One-Hot Encoding
* Word2vec Embedding: CBOW
* Word2vec Embedding: Skip-gram
* GloVe Embedding

**(5) Text Cleaning Techniques**

* Fix spelling
* Remove punctuation
* Lower case
* Remove stopwords

#### 2. Classical NLP Techniques

**(1) Text Tokenization**

Text tokenization is the task of chopping up texts into pieces called tokens. It is usually used to build a vocabulary thst will be used to determine the inputs for the model. The difference between spliting by space is that the process of tokenization requires to split at some non-spaces. For example, with splitting by spaces, we have,

```
"They're not going to the Sam's Market."
["They're","not","going","to","the","Sam's","Market."]
```

However, with tokenization, this text will be splitted based on the tokens,

```
"They're not going to the Sam's Market."
["They","'re","not","going","to","the","Sam's","Market","."]
```

**(2) Subword Tokenization: Byte Pair Encoding (BPE)**

The text tokenization technique is not perfect because we can have so many tokens of the same meaning. For example, `low lower lowest` by text tokenization will be splitted to,

```
["low", "lower", "lowest"]
```

However, with BPE, this string will be splitted to tokens of,

```
["low", "er", "est"]
```

This technique is used by the famous NLP model BERT, and the goal of BPE is to find a way to represent the text with the least amount of tokens. So now let's see an example. Suppose we have the following string,

```
"low low low low low lowest lowest newer newer newer newer newer newer wider wider wider new new"
```

First, let's split by characters and the vocabulary should be,

```
["d", "e", "i", "l", "n", "o", "r", "s", "t", "w", " "]
```

Then, let's find the character pair with the highest frequency in the string, which should be `er`, so we combine `er` as a token and put it in the vocabulary. So we have,

```
Merge=("e", "r"), Vocab = ["d", "e", "i", "l", "n", "o", "r", "s", "t", "w", " ", "er"]
```

Continue this process, we will merge the following tokens in sequence,

```
("e", "r")
("er", " ")
("n", "e")
("ne", "w")
("l", "o")
("lo", "w")
("new", "er ")
("low", " ")
```

And the final vocabulary should be,

```
["d", "e", "i", "l", "n", "o", "r", "s", "t", "w", " ", "er", "er ", "ne", "new", "lo", "low", "newer ", "low "]
```

So according to the vocabulary above, for the following string,

```
"newer lower net"
```

We will split it as,

```
["newer ", "low", "er ", "ne", "t"]
```

The pseudo code for the BPE algorithm is,

<img src="/Users/apple/Dropbox/SereneField3/Blog/image/Screen Shot 2022-03-09 at 7.05.46 PM.png" alt="Screen Shot 2022-03-09 at 7.05.46 PM" style="zoom:40%;" />

**(3) Build Vocabulary From Tokenization**

So far, we have talked about how to take the tokenization of a text and now we would like to see how to build a vocabulary from the tokenization result. Our goal is to build a vocabulary with the following features,

* Stable for the rare words in the text
* Stable for predicting unknown words

In order to achieve these goals, we have to,

* Map all the words with frequency less than 5 to the word `UNK`
* Map all the out of vocabulary words to `UNK`

**(4) Lemmatization and Stemming** 

Lemmatization is the process where we take individual tokens from a sentence and we try to reduce them to their base form. Stemming is to find the stem of a token that can leads to some meaningless tokens or ambiguous tokens. 

For example, the lemmatization of the following words are,

```
cars -> car
car's -> car
careness -> care
carefully -> care
```

However, for stemming (e.g. Porter stemming), the result will be,

```
cars -> car
car's -> car
careness -> car
carefully -> car
```

With lemmatization and stemming, some different words will be mapped to the same token. For example,

```
am, is, are => be
I, you, she, he => pron
```

But because we ignore some information based on lemmatization and stemming, it will commonly lose some precision we have on the meanings of the words. So these techniques are generally used for,

* Test classification tasks on searching engines 
* Complex languages like Arabic and Spanish

**(5) Sentence Segmentation**

We can not commonly use the period `.` to split sentences because these values are going to be ambiguous. For example

* Abbreviation like `Inc.` or `Dr.`
* Numbers like `4.3` 
* Some quotations like `It is "Not good." that said by him.`

Because of these issues, we will build a binary classifier (i.e. decision tree) for deciding where is the end of sentences (EOSs). Here are some common decision boundaries,

```
- Is there one blank line after?
- Is the token before "." is an abbreviation?
- Is the case of word after "." is upper?
- Probability we have a word after ".".
- Probability we have a word before ".".
```

**(6) POS (part of speech) tagging**

Determine the part of speech tage for a particular instance of a word. Note that the same word can have more than one POS according to its context. For example

```
Apple -> Propn
is -> Verb
at -> Adp
$ -> Sym
1 -> Num
```

**(7) NER (named entity recognization)**

Find and classify different named entities in the text. For example,

```
Adam -> Name
2010 -> Date
Walgreens -> Organization
Los Angeles -> Location
```

This technique is frequently used for,

- Text classifications
- Sentiment analysis for named entities
- Question answering

**(8) Dependency Parsing**

The dependency structure of a text shows which word depend on which other words.

**(9) N-Gram Models**

N-gram models means to use $n$ continuous sequence of items from a given text. For example, let's say we have the following string for training,

```
"I would like to go"
```

And the unigram model have the following training set,

```
["I","would","like","to","go"]
```

The bigram model have the following training set,

```
[["I","would"],
 ["would","like"],
 ["like", "to"],
 ["to", "go"]]
```

And the trigram model have the following training set,

```
[["I","would","like"],
 ["would","like","to"],
 ["like", "to","go"]]
```

**(10) BOW (Bag of word) Model**

The BOW model is considered as a unigram model and each word in that model is considered as a feature. For example, suppose we have the following two texts,

```
"I would like to go"
"I would like not not to go"
```

Then the vocabulary of these texts should be,

```
["I","would","like","to","go","not"]
```

Now, let's see each of the texts above as a bag of words without order, and the texts above can be represented by the following two vectors with the frequency of each word in its bag.

```
[1, 1, 1, 1, 1, 0]
[1, 1, 1, 1, 1, 2]
```

We can find out in this case that because each word is considered a feature, it is a unigram model we have talked about.

#### 3. Word Representation Techniques

**(1) Downsides of WordNet and One-Hot Encoding**

We have encoded the data with the techniques we talked about above, but how can we actually encode the meaning of a word?

One way is to use a WordNet for explaining the word, but there are some downsides,

* Missing nuance of the word
* Missing new meanings of the word
* The analyzed results can be subjective
* It requires human labor to create and adapt
* It can not compute accurate word similarity

Another way is to use one-hot encoding, but there are also some defects,

* The vector has a large dimension of the length of the vocabulary
* Different word vectors are orthogonal so that there's no natural notation for one-hot vectors

Therefore, in order to vector for representing a word, we have to develop some other techniques.

**(2) Word2Vec Embedding: CBOW**

The continuous bag of word (CBOW) is a model used for creating the embedding matrix of the vocabulary. Then from this embedding matrix, we can then extract the corresponding word and turn that word to a vector from the embedding matrix. Given the context window of $2k+1$, which means we take the $k$ words before the center word and $k$ words after the center word as the input. 

```
["I","would","to","go"] -> like
```

So for each of the continuous context bags of word containing $2k$ words, we use this input for fitting an embedding matrix, then take the summation of each column in the embedding matrix (because the values from the same column is from the same context). Finally, we fit a linear layer to derive the output predictions.

```python
class CBOW(torch.nn.Module):
    def __init__(self, vocab_size, embedding_dim):
        super(CBOW, self).__init__()
        self.embeddings = nn.Embedding(vocab_size, embedding_dim)
        self.linear = nn.Linear(embedding_dim, vocab_size)

    def forward(self, inputs):
        embeds = sum(self.embeddings(inputs)).view(1,-1)
        out = self.linear(embeds)
        return out

    def get_word_emdedding(self, word_idx):
        return self.embeddings(word_idx).view(1,-1)
```

Suppose we have $K = 2k$, the vocabulary size $V$ and the embedding size $D$. Then the number of parameters are,
$$
V \times D + (D + 1) \times V
$$
**(3) Deep CBOW**

Because we have only one linear layer in the CBOW model above, the performance may not be good enough. What we can improve is to add multiple linear layers followed by activations into the CBOW model and make it as a DeepCBOW model.

```python
class DeepCBOW(torch.nn.Module):
    def __init__(self, vocab_size, embedding_dim):
        super(DeepCBOW, self).__init__()
        self.embeddings = nn.Embedding(vocab_size, embedding_dim)
        self.linear1 = nn.Linear(embedding_dim, 128)
        self.linear2 = nn.Linear(128, vocab_size)
        self.relu = nn.ReLU()

    def forward(self, inputs):
        embeds = sum(self.embeddings(inputs)).view(1,-1)
        out = self.linear1(embeds)
        out = self.relu(out)
        out = self.linear2(embeds)
        return out

    def get_word_emdedding(self, word_idx):
        return self.embeddings(word_idx).view(1,-1)
```

**(4) N-gram of Neural Bags**

One problem for CBOW is that we can not capture the order of the words because the words in bag are unordered. So we can leverage the n-gram model to obtain some sequence information. However, there are several downsides of this model,

* Similar n-grams are considered as different features

* Still lose the global sequence order
* Too many pairs of grams lead to a large vocabulary

Therefore, most of NLP tasks use a sequence representation learning problem, which takes a neural sequence model instead.

**(4) Word2Vec Embedding: Skip-gram**

The skip-gram is the inverse model of CBOW which select a word as the training record, and then random select one word from the context of this word as its target. So for the example above, we can have the training set as,

```
like -> would
like -> I
like -> to
like -> go
```

So the embedding vector $e_c$ of word $c$ as $x$ and embedding vector $\theta_t$ of word $t$ as $y$. Then we have the  following estimation of the target probability as,
$$
\hat{y}_{t}=P(t \mid c)=\frac{e^{\theta_{t} \cdot e_{c}}}{\sum_{j=1}^{V} e^{\theta_{j} \cdot e_{c}}}
$$
Therefore, 

```python
class SkipGram(torch.nn.Module):
    def __init__(self, vocab_size, embedding_dim):
        super(SkipGram, self).__init__()
        self.embedding_x = nn.Embedding(vocab_size, embedding_dim)
        self.embedding_y = nn.Embedding(vocab_size, embedding_dim)

    def forward(self, x, y):
        x = self.embedding_x(x)
        y = self.embedding_y(y)
        return x * y

    def get_word_emdedding(self, word_idx):
        return self.embedding_x(word_idx).view(1,-1)
```

Note that we can also write a naive model with the linear layer for representing the y embedding.

```python
class SkipGram(torch.nn.Module):
    def __init__(self, vocab_size, embedding_dim):
        super(SkipGram, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embedding_dim)
        self.linear = nn.Linear(embedding_dim, vocab_sizen, bias=False)

    def forward(self, x):
        x = self.embedding(x)
        x = self.linear(x)
        return x

    def get_word_emdedding(self, word_idx):
        return self.embedding(word_idx).view(1,-1)
```

Note that here we select $E$ as our final embedding, and in both of the cases, we have $2VD$ parameters.

**(5) Skip-gram with Negative Sampling**

In order to make this example easier, a trick here is to convert this softmax problem to a binary classification problem by assigning all the pairs as 1.

```
like would 1
like I     1
like go    1
like to    1
```

Similar to matrix factorization problem, this matrix does not have negative values so that we have to conduct some negative samplings to this dataset. Commonly we can sample 5-20 negatives for each positive value for a small dataset and 2-5 negatives for each positive value for a large dataset. So what we can do is to add these negative to our dataset,

```
like would 1
like car   0
like shop  0
like apple 0
like note  0
```

Because we take these negative samples from the whlole corpora, there is another problem. The stop words appear too much in the corpora so that we have to reduce the probability for choosing them. For example,

```
like the   0
```

So the probability of choosing a word $w_i$ for sampling is combuted based on,
$$
P\left(w_{i}\right)=\frac{f\left(w_{i}\right)^{3 / 4}}{\sum_{j=1}^{V} f\left(w_{j}\right)^{3 / 4}}
$$
Where $f\left(w_{i}\right)$ is the frequency of this word. 

```python
class SkipGram_neg(torch.nn.Module):
    def __init__(self, vocab_size, embedding_dim):
        super(SkipGram_neg, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embedding_dim)
        self.linear = nn.Linear(embedding_dim, vocab_sizen, bias=False)

    def forward(self, x):
        x = self.embedding(x)
        x = self.linear(x)
        return x

    def get_word_emdedding(self, word_idx):
        return self.embedding(word_idx).view(1,-1)
```

Note that we should apply `binary_cross_entropy` as our loss function here.

**(5) GloVe Embedding**

We are not look into the details of this one but the basic idea of GloVe is to puish the model with the frequently appeared words (like stop words). Let's define $X_{ij}$ as the number oftimes a word $i$ appears in the context of word $j$. Then the loss function of GloVe is,
$$
J = \sum_{i=1}^{V} \sum_{j=1}^{V} f\left(X_{i j}\right)\left(\theta_{i} \cdot e_{j}+b_{i}+b_{j}^{\prime}-\log \left(X_{i j}\right)\right)^{2}
$$
Where,
$$
f(x)=\left\{\begin{array}{cc}
\left(x / x_{\max }\right)^{\alpha} & \text { if } x<x_{\max } \\
1 & \text { otherwise }
\end{array}\right.
$$
From this formula, we can know that the number of parameters in this model is $2V(D+1)$, and the final embedding should be the average of embedding matrix $\Theta$ and $E$,
$$
\tilde{e}_{i}=\frac{\theta_{i}+e_{i}}{2}
$$
**(6) t-SNE**

t-SNE is a nonlinear nondeterministic algorithm that tries to preserve local neighbourhoods in the data, often at the expense of distorting the global structure.