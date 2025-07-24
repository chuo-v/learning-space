# Bayes Theorem

Bayes' Theorem (or Bayes' Rule) allows us to express the probability of an event occuring when it is given that another event has occurred.

Let there be arbitrary events $A$ and $B$. The theorem states that the _posterior probability_ of $A$ occurring given $B$ has already occurred is:

$$
\begin{align}
P(A|B) = \frac{P(B|A)P(A)}{P(B)}
\end{align}
\tag{1}
$$

where $P(B)\neq 0$, and
- $P(B|A)$ is the _likelihood_ of $B$ occurring given that $A$ has occurred
- $P(A)$ is the _prior probability_ of $A$ occurring (i.e. before even considering about $B$)
- $P(B)$ is the _prior probability_ of $B$ occurring

## Deriving the theorem

Let's consider the same arbitrary events $A$ and $B$ as before.

### A note about $P(A,B)$

First we note that the probability of both events occurring is:

$$
\begin{align}
P(A,B)=P(A)P(B|A)=P(B)P(A|B)
\end{align}
\tag{2}
$$

where $P(A)$, $P(B)$, $P(A|B)$ and $P(B|A)$ are as defined above.

Intuitively, as a starting point, you can think of the probability of two events occurring being calculated as the multiplication of the probabilities of each event occurring. However, if the two events are not independent of each other (i.e. one event occurring may affect the probability of the other event occurring), then the calculation can be approached as follows:
1. Choose either event to start with. _For illustration purposes, let's choose_ $A$ _here._
2. Let's now assume the event chosen in the previous step has occurred, so we'll get the probability of it occurring. _We chose_ $A$ _previously, so the probability we need here is_ $P(A)$.
3. Since the previously chosen event is assumed to have already occurred, for the other event that was not chosen, we need to get the probability that it occurs _given that_ the event previously chosen had already occurred. _The event that was not previously chosen is_ $B$_, so the probability we need here is_ $P(B|A)$.
4. Multiply the probabilities from the previous 2 steps. _A simple multiplication gives us_ $P(A)P(B|A)$.

If we switch the example used in the steps above and choose $B$ first instead, we arrive at a similar result of $P(B)P(A|B)$.

As a side-note, if we can assume that $A$ and $B$ are independent, then it follows that the probability of one of the events occurring is not affected by whether the other event has already occurred, so $P(A|B)=P(A)$ and $P(B|A)=P(B)$, and thus $P(A,B)=P(A)P(B)$.

### Approach 1: Expanding on the equality from $P(A,B)$

From here, one approach to arriving at the theorem is to simply use the equation shown in (2).<br>
Let's remove $P(A,B)$ from this equation, and just look at the remaining expressions.

$$
\begin{align}
P(A)P(B|A)=P(B)P(A|B)
\end{align}
\tag{3}
$$

Let's isolate $P(A|B)$ by dividing $P(B)$ on both sides.

$$
\begin{align}
\frac{P(A)P(B|A)}{P(B)}=\frac{P(B)P(A|B)}{P(B)}
\end{align}
\tag{4}
$$

Simplfying the expressions, we then arrive at the theorem.

$$
\begin{align}
P(A|B)=\frac{P(A)P(B|A)}{P(B)}
\end{align}
\tag{5}
$$

Note that through similar steps, we can also check that the following is true.

$$
\begin{align}
P(B|A)=\frac{P(B)P(A|B)}{P(A)}
\end{align}
\tag{6}
$$

### Approach 2: Using the definition of conditional probability

Another approach to arriving at the theorem is to use the definition of conditional probability:

$$
\begin{align}
P(A|B)=\frac{P(A,B)}{P(B)}
\end{align}
\tag{7}
$$

Using the result from (2), this can then be rewritten as follows to arrive at the theorem.

$$
\begin{align}
P(A|B)=\frac{P(A)P(B|A)}{P(B)}
\end{align}
\tag{8}
$$

## Extending to 3 events

Let's now consider the case of 3 events.

Let there be arbitrary events $A$, $B$ and $C$. The probability of $A$ occurring _given that_ $B$ and $C$ had occurred is $P(A|B,C)$.

If we consider $B,C$ together as a unit, we can use the result from (7) to write:

$$
\begin{align}
P(A|B,C)=\frac{P(A,B,C)}{P(B,C)}
\end{align}
\tag{9}
$$

Similarly, we can write:

$$
\begin{align}
P(C|A,B)=\frac{P(A,B,C)}{P(A,B)}
\end{align}
\tag{10}
$$

which can be rewritten as follows after multiplying by $P(A,B)$ on both sides of the equation.

$$
\begin{align}
P(A,B,C)=P(C|A,B)P(A,B)
\end{align}
\tag{11}
$$

Substituting the result from (11) back into (9):

$$
\begin{align}
P(A|B,C)=\frac{P(C|A,B)P(A,B)}{P(B,C)}
\end{align}
\tag{12}
$$

Using the result from (2) to rewrite the $P(A,B)$ and $P(B,C)$ terms, this can then be rewritten as follows:

$$
\begin{align}
P(A|B,C)=\frac{P(C|A,B)P(A|B)P(B)}{P(C|B)P(B)}
\end{align}
\tag{13}
$$

which simplifies to:

$$
\begin{align}
P(A|B,C)=\frac{P(C|A,B)P(A|B)}{P(C|B)}
\end{align}
\tag{14}
$$

Using similar steps, we can also arrive at the following result.

$$
\begin{align}
P(A|B,C)=\frac{P(B|A,C)P(A|C)}{P(B|C)}
\end{align}
\tag{15}
$$

## Generalized form

Let's now consider the case where there are $n+1$ events $A,B_{1},\ldots,B_{n}$.

Considering $B_{1},\ldots,B_{n}$ together as a unit, we can use the result from (7) to write:

$$
\begin{align}
P(A|B_{1},\ldots,B_{n})=\frac{P(A,B_{1},\ldots,B_{n})}{P(B_{1},\ldots,B_{n})}
\end{align}
\tag{16}
$$

With similar steps used in previous sections, this equation can then be rewritten as follows:

$$
\begin{align}
P(A|B_{1},\ldots,B_{n})=\frac{P(B_{n}|A,B_{1},\ldots,B_{n-1}) \cdots P(B_{2}|A,B_{1})P(A|B_{1})P(B_{1})}{P(B_{n}|B_{1},\ldots,B_{n})\cdots P(B_{2}|B_{1})P(B_{1})}
\end{align}
\tag{17}
$$

which simplifies to:

$$
\begin{align}
P(A|B_{1},\ldots,B_{n})=\frac{P(B_{n}|A,B_{1},\ldots,B_{n-1}) \cdots P(B_{2}|A,B_{1})P(A|B_{1})}{P(B_{n}|B_{1},\ldots,B_{n-1})\cdots P(B_{3}|B_{1},B_{2}))P(B_{2}|B_{1})}
\end{align}
\tag{18}
$$

This is just one of the many ways in which this equation can be rewritten.