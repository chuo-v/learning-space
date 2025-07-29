# N-Gram Language Models

The **n-gram** language model is the simplest kind of language model.

Language models are machine learning models that predict the words that may follow a sequence of words.<br>
Consider the unfinished sentence, and try to think what word will likely follow it:

$$
\begin{align}
the\ sky\ is\ so\ \dots
\end{align}
\tag{1}
$$

Perhaps "blue", "cloudy" or "beautiful" may have come to mind. A language model assigns a probability to each possible word that could come next, and can even assign a probability to an entire sentence. For example, even though the following two sentences consist of the same words, the words are ordered differently in each, and a language model can tell us which of the sequences has a higher probability of appearing in some text:

$$
the\ passengers\ boarded\ the\ plane
$$
$$
boarded\ passengers\ the\ plane\ the
$$

Here are some examples of how word prediction is useful:
- to be able to choose words that fit the context better (e.g. for spell/grammar checking)
- to enable a speech system to recognize what was said by choosing the more probable word sequence
- to enable **augmentative and alternative communication** (AAC) systems for people who are physically unable to speak or sign, but can use other methods to select words from an interface
- use in **large language models**

## N-Grams

An **n-gram** is a sequence of $n$ words. A 2-gram (or a **bigram**) is a sequence of 2 words, like:

$$
the\ sky,\ sky\ is,\ is\ so,\ so\ blue
$$

A 3-gram (or a **trigram**) is a sequence of 3 words, like:

$$
the\ sky\ is,\ sky\ is\ so,\ is\ so\ blue
$$

However, a 'n-gram' is also used to refer to a probabilistic model that can:
- given a sequence of $n-1$ words, calculate the probability of a word following the sequence
- calculate probabilities for entire sequences (which can tell us which is more probable to appear in some text)

Suppose we want to know the probability that the next word that comes after (1) is $blue$:

$$
\begin{align}
P(blue|the\ sky\ is\ so)
\end{align}
\tag{2}
$$

One way to estimate this probability is by counting _relative frequency_. Some large _corpus_ can be used to count the number of times $the\ sky\ is\ so$ appears in it, and to count the number of times this sequence is followed by $blue$, and our estimate would simply be the ratio of the two counts:

$$
\begin{align}
P(blue|the\ sky\ is\ so)=\frac{count(the\ sky\ is\ so\ blue)}{count(the\ sky\ is\ so)}
\end{align}
\tag{3}
$$

However, as language is creative, with new sentences being invented all the time, it's not feasible to expect to be able to get accurate counts for longer sequences, even if the entire web is used.

## Estimating probabilities

We need some better way to estimate the probability of a word $w$ given a history $h$, or the probability of a sequence of words $W$.

Let $w_{1}\dots w_{n}$ be a sequence of words, and $P(w_{1},\dots,w_{n})$ be the joint probability of each word in the sequence having a particular value. If we use the **chain rule of probability**:

$$
\begin{align}
P(X_{1}\dots X_{n})=P(X_{1})P(X_{2}|X_{1})P(X_{3}|X_{1}X_{2})\dots P(X_{n}|X_{1}\dots X_{n-1})
\end{align}
\tag{4}
$$

and apply it to the words:

$$
\begin{align}
P(w_{1}\dots w_{n})=P(w_{1})P(w_{2}|w_{1})P(w_{3}|w_{1}w_{2})\dots P(w_{n}|w_{1}\dots w_{n-1})
\end{align}
\tag{5}
$$

(5) suggests that we can multiply several conditional probabilities together to estimate the joint probability of a sequence of words, but the conditional probabilities like $P(w_{n}|w_{1}\dots w_{n-1})$ that are the probabilities of word given a _long sequence_ of words is still difficult to calculate.

One idea is to, instead of using the entire history, just use the last few words as an _approximation_ of the history. For example, the **bigram** model makes this approximation as follows:

$$
\begin{align}
P(w_{n}|w_{1}\dots w_{n-1})\approx P(w_{n}|w_{n-1})
\end{align}
\tag{6}
$$

Using our "blue sky" example in (2), the following approximation would be made:

$$
\begin{align}
P(blue|the\ sky\ is\ so)\approx P(blue|so)
\end{align}
\tag{7}
$$

This is called a **Markov assumption** (see [Hidden Markov Models](../../parts-of-speech-tagging/hidden-markov-models/) as well), where the probability of a word depends only on the previous word.

For a n-gram model, this approximation can be written as follows:

$$
\begin{align}
P(w_{n}|w_{1}\dots w_{n-1})\approx P(w_{n}|w_{n-N+1}\dots w_{n-1})
\end{align}
\tag{8}
$$

### Maximum Likelihood Estimation

Now we have approximations for the bigram and n-gram models, but we need a way to estimate the probabilities in (6) and (8). One way to do so is **Maximum Likelihood Estimation** (MLE). For a n-gram model, we can get such a MLE estimate by using counts from a corpus, then **normalizing** them so they lie between 0 and 1.

For example, the bigram probability for a word $w_{n}$ given the previous word is $w_{n-1}$ can be calculated as:

$$
\begin{align}
P(w_{n}|w_{n-1})=\frac{count(w_{n-1}w)}{\sum_{w}count(w_{n-1}w)}
\end{align}
\tag{9}
$$

However, since the unigram count of $w_{n-1}$ is the same as the sum of all bigram counts that start with $w_{n-1}$, (9) can be simplified as:

$$
\begin{align}
P(w_{n}|w_{n-1})=\frac{count(w_{n-1}w)}{count(w_{n-1})}
\end{align}
\tag{10}
$$

This ratio of the counts of a sequence ($w_{n-1}w$) to the counts of a prefix of it ($w_{n-1}$) is called a **relative frequency**.

### Bigram probabilities example

Let's calculate some of the bigram probabilities for a small example using a corpus of just the following three sentences:

$$
I\ like\ that
$$
$$
John\ and\ I\ ran
$$
$$
That\ is\ something\ I\ like\ more
$$

Here are the calculations for some of the bigram probabilities:

$$
P(like|I)=\frac{2}{3}\quad P(ran|I)=\frac{1}{3}
$$
$$
P(that|like)=\frac{1}{2}\quad P(more|like)=\frac{1}{2}
$$

## Using Log Probabilities for Large N-Gram Models

When language models get very large in practice, the probabilities often have to be stored and computed as **log probabilities**. Due to probabilities being less than or equal to 1, the more probabilities are multiplied with each other, the smaller the result becomes, and if it becomes small enough that it cannot be stored in the intended format without needing a rounding error that is larger than usual, _numerical underflow_ can occur. Multiplication in linear space is the same as addition in log space, so all computation for the models can be done and stored in log space, and only converted back to probabilities at the end by taking the $exp$ of the log probability:

$$
\begin{align}
p_{1} \times p_{2} \times p_{3}=exp(ln(p_{1})+ln(p_{2})+ln(p_{3}))
\end{align}
\tag{11}
$$