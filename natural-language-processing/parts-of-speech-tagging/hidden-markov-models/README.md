# Hidden Markov Models

Hidden Markov models have a wide range of applications to pattern recognition, signal processing, economics, and more. This document will focus on their applications to Parts-of-Speech tagging, which is a core task in natural language processing.

## Parts-of-Speech Tagging

Parts-of-Speech (POS) tagging is the process of going through some given text and assigning each word a corresponding part of speech (e.g. noun, verb, adjective, adverb). This additional context obtained can help facilitate better understanding of sentence structure and meaning, and allow machines to perform better at tasks requiring language processing (e.g. information retrieval, sentiment analysis).

For example, for the following sentence, we would like to obtain the POS tags specified below each word in parantheses.

$$
\underset{(pronoun)}{\text{I}} \quad \underset{(verb)}{\text{exercise}} \quad \underset{(preposition)}{\text{at}} \quad \underset{(determiner)}{\text{a}} \quad \underset{(noun)}{\text{gym}}
$$

While this may seem like a simple mapping exercise, there are words that can be used as multiple POS. Take the word "well" for example:
- [_noun_] I dug a **well** 5 meters deep
- [_verb_] Tears **well** up in the movie's audience
- [_adjective_] She's not feeling **well**
- [_adverb_] Business is going **well** recently
- [_interjection_] **Well**, it depends on the traffic

Hence, tagging is a **disambiguation** task, where the objective is to resolve any ambiguities and find the correct tag for the context.

## Markov Model

The Hidden Markov model is based on augmentation of the Markov model.

A Markov model is a stochastic model that predicts future states based only on the current state. The simplest Markov model is the **Markov chain**, which models the state of a system using a random variable that changes through time.

### Predicting rain

Suppose we want to predict the probabilities that it will rain in the upcoming future. The **Markov assumption** indicates that when conducting such predictions, only the present (and not the past) matters. In other words, predicting about whether it will rain tomorrow will only depend on today, and not on past weather conditions.

More formally, let $q_{1},\dots,q_{i}$ be a sequence of state variables. The Markov assumption can be written as:

$$
\begin{align}
P(q_{i}=a|q_{1}\dots q_{i-1}) = P(q_{i}=a|q_{i-1})
\end{align}
\tag{1}
$$

Let's also define the _state space_ (the space containing all possible states) to be $\{R, NR\}$ for the set of "rain" and "no rain". From (1), the probability of a state variable being assigned a certain state is only dependent on the previous state variable, so the probability of $q_{2}=R$ only depends on $q_{1}$. Hence, if we know the _transition probabilities_ from a state to the next state, we would be able to get the probability of any state variable being assigned a state. For a Markov chain, these probabilities are specified using a **transition probability matrix**.

However, note that, by definition, there is no state variable before $q_{1}$, so using transition probabilities for it would seem a bit out of place. Instead, for a Markov chain, an **initial probability distribution** over the states is provided that specifies the probabilities of each state being assigned to the _initial_ state variable (that starts the Markov chain).

Putting all of the above together, the following components specify a first-order Markov chain:
- a set of $N$ **states** $S=\{s_{1},\dots,s_{N}\}$
- **a transition probability matrix**: $A$, where each element $a_{ij}$ represents the probability of moving from state $i$ to state $j$, and $\sum_{j=1}^{N}a_{ij}=1$ for all $i$
- an **initial probability distribution** over the states: $\pi=\pi_{1},\dots,\pi_{N}$, where $\pi_{i}$ is the probability the Markov chain starts in state $i$, and $\sum_{i=1}^{N}\pi_{i}=1$

This Markov chain is a _first-order_ one as it only looks _one_ state back (the previous state) when making predictions about a state (as per the Markov assumption).

### Specifying values for our rain prediction example

Let's specify some values for the example of predicting rain to calculate some probabilities for a few scenarios.

For the sake of brevity, suppose we would like to predict whether it would rain over the next 3 days. We'll use the same state space as before that has $N=2$ possible states: $S=\{R,NR\}$, where for $A$ and $\pi$ below, we'll consider $R$ as the first state and $NR$ to be the second.

For the transition probability matrix with element $a_{ij}$, we'll just assign it arbitrary values that satisfy $\sum_{j=1}^{2}a_{ij}=1$:

$$
A=
\begin{bmatrix}
0.6 & 0.4 \\
0.3 & 0.7
\end{bmatrix}
$$

Similarly, we'll assign arbitrary values for the initial probability distribution that satisfy $\sum_{i=1}^{2}\pi_{i}=1$:

$$
\pi =
\begin{bmatrix}
0.2 & 0.8
\end{bmatrix}
$$

#### Example sequence 1

Let's try predicting the probability of the following sequence occurring over the next three days:

$$
R \rightarrow R \rightarrow R
$$

We know from the
- initial probability distribution that $P(q_{1}=R)=\pi_{1}=0.2$
- transition probability matrix that
  - $P(q_{2}=R|q_{1}=R)=a_{11}=0.6$
  - $P(q_{3}=R|q_{2}=R)=a_{11}=0.6$

so the resulting probability is calculated as follows.

$$
0.2 \times 0.6 \times 0.6 = 0.072
$$

#### Example sequence 2

Next, let's try predicting the probability of the following sequence occurring over the next three days:
$$R \rightarrow NR \rightarrow R$$

We know from the
- initial probability distribution that $P(q_{1}=R)=\pi_{1}=0.2$
- transition probability matrix that
  - $P(q_{2}=NR|q_{1}=R)=a_{12}=0.4$
  - $P(q_{3}=R|q_{2}=NR)=a_{21}=0.3$

so the resulting probability is calculated as follows.

$$
0.2 \times 0.4 \times 0.3 = 0.024
$$

#### Example sequence 3

Now let's try predict the probability of the following sequence occurring over the next three days:
$$NR \rightarrow NR \rightarrow R$$

We know from the
- initial probability distribution that $P(q_{1}=NR)=\pi_{2}=0.8$
- transition probability matrix that
  - $P(q_{2}=NR|q_{1}=NR)=a_{22}=0.7$
  - $P(q_{3}=R|q_{2}=NR)=a_{21}=0.3$

so the resulting probability is calculated as follows.

$$
0.8 \times 0.7 \times 0.3 = 0.168
$$

## Hidden Markov Model

A Markov chain can be used to calculate a probability of a sequence of observable events, like a sequence of whether it rained each day over a period of a month.

However, for POS tagging, the inputs to the process are text that are not normally accompanied by their corresponding POS tags, so we cannot directly _observe_ the POS tags from the inputs. In this sense, we can call the tags to be _hidden_.

A Hidden Markov model (HMM) differs from a Markov model in that it allows us to talk about both _observed_ and _hidden_ events, where the latter may be thought of as causal factors in the probabilistic model.

The components that specify a HMM are almost the same as a Markov chain, with the exception of an additional sequence of likelihoods:
- a set of $N$ **states** $S=\{s_{1},\dots,s_{N}\}$
- a **transition probability matrix**: $A$, where each element $a_{ij}$ represents the probability of moving from state $i$ to state $j$, and $\sum_{j=1}^{N}a_{ij}=1$ for all $i$
- a sequence of **observation likelihoods** $B=b_{i}(o_{t})$ (also called **emission probabilities**) that express the probability of an observation $o_{t}$ being generated from a state $q_{i}$
- an **initial probability distribution** over the states: $\pi=\pi_{1},\dots,\pi_{N}$, where $\pi_{i}$ is the probability the Markov chain starts in state $i$, and $\sum_{i=1}^{N}\pi_{i}=1$

The input to the HMM is a sequence of T observations $O=o_{1}o_{2}\dots o_{T}$, where each observation is drawn from a pre-defined _vocabulary_, which is a set of unique symbols that the HMM can generate as observations.

A first-order HMM makes two assumptions. First is the same **Markov assumption** as (1), which indicates that the probability of a particular state only depends on the previous state. Second, the probability of observation $o_{i}$ as an output depends only on $q_{i}$, the state that produced the observation, and not on any other states or observations. This is often referred to as the **output independence assumption**, and can be formally written as:

$$
\begin{align}
P(o_{i}|q_{1},\dots q_{i}\dots q_{T},o_{1},\dots o_{i}\dots o_{T})=P(o_{i}|q_{i})
\end{align}
\tag{2}
$$

### Back to predicting rain

Let's return to our example of predicting rain for a moment. In our example, we were able to directly _observe_ the event (whether it rains on a day), so we'll have to modify it a bit first.

Consider John and Mary, who stay in different countries far apart from each other. For any given day, Mary does not know whether it is raining where John lives, but she does know that on any given day, Bob will do one of three of his favorite activities: going to the bookstore, running outside or eating out at a restaurant. Suppose each of the choices depends exclusively on whether it is a rainy day, so while Mary cannot directly observe whether it is raining for John, she calls John daily and is informed about the activity that John chose to do that day.

Using a HMM, Mary can try predicting whether it rains on a day for John, treating such events as _hidden_, and the activity that John chose on a day to be the directly _observable_ events. A HMM considers that the hidden states (whether it is raining for John) produce the observations (the activities that John chooses), where each state generates an observation with a fixed probability provided in $B=b_{i}(o_{t})$, the sequence of observation likelihoods (or emission probabilities).

### Applying a HMM for POS tagging

(_contents being prepared_)