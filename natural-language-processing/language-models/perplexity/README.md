# Perplexity

Perplexity is an important metric used in natural language processing for evaluating language models.

A language model (that predicts which word will come next in a sequence) is considered to be better if it assigns a higher probability to each of the words that occur in the test set (a set whose main role is to allow evaluation of the model). In other words, such a language model would guess each next word correctly more of the times (i.e. it assigns each of the words a higher probability). Thus, a perfect language model would assign each of the words with a probability 1, and all other words (that are not the next word being predicted) with a probability 0.

However, as a test set consists of more words that form longer sequences, the probability of it becomes smaller, and so a better metric would be one that could allow comparisons between texts of different lengths. An idea is to use a metric that is normalized in some way using the length of the test set, and one such important metric is **perplexity**, which is a function of probability.

The perplexity of a language model on a test set is calculated by taking the inverse of the probablity of the test set, which is then normalized by the number of words $N$ by taking the Nth root. For a test set $w_{1}\dots w_{N}$, the perplexity of it is:

$$
\begin{align}
P(w_{1}\dots w_{N})^{-\frac{1}{N}}=\sqrt[N]{\frac{1}{P(w_{1}\dots w_{n})}}
\end{align}
\tag{1}
$$

Using the chain rule of probability to expand the probability of the test set, (2) can be rewritten as:

$$
\begin{align}
\sqrt[N]{\prod_{i=1}^{N}\frac{1}{P(w_{i}|w_{1}\dots w_{i-1})}}
\end{align}
\tag{2}
$$

Note that due to the inverse relationship of probability and perplexity, better models will have a lower perplexity.

## Perplexity of N-Gram Language Models

The details of how perplexity is calculated depends on the language model used. The perplexity of some n-gram language models (see [N-Gram Language Models](../n-gram-language-models/)) are provided below.

### Unigram Language Models

The perplexity of a unigram language model on a test set $w_{1}\dots w_{n}$ is simply the _geometric mean_ of the inverse of the unigram probabilities:

$$
\begin{align}
\sqrt[N]{\prod_{i=1}^{N}\frac{1}{P(w_{i})}}
\end{align}
\tag{3}
$$

### Bigram Language Models

The perplexity of a bigram language model on a test set $w_{1}\dots w_{n}$ is simply the _geometric mean_ of the inverse of the bigram probabilities:

$$
\begin{align}
\sqrt[N]{\prod_{i=1}^{N}\frac{1}{P(w_{i}|w_{i-1})}}
\end{align}
\tag{4}
$$