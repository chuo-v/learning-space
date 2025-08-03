# Viterbi algorithm

The **Viterbi algorithm** is the decoding algorithm for HMMs (see [Hidden Markov models](../../hidden-markov-models/)). It is a prime example of _dynamic programming_, which is a technique that optimizes complex problems into smaller, overlapping subproblems.

To find the most likely sequence of hidden states of a HMM given a sequence of observed events, the Viterbi algorithm breaks the problem down into smaller, overlapping subproblems by considering that the most likely path at a certain time step depends on the most likely paths to all previous states at the preceding time step. Since the result of each subproblem (the maximum probability, at each time step, of reaching each state) is stored, redundant calculations can be avoided as the same path probabilities do not need to be computed more than once.

## Python implementation of the Viterbi algorithm

Let's go through a Python implementation of the Viterbi algorithm to explain what happens at each step. The entire Python file can be found in the same directory [here](viterbi.py), but relevant sections of it will be pasted below as well.

The implementation of the algorithm can be found in the `viterbi` function in the file.

```
def viterbi(A, B, O, pi=None):
```

The parameter names may seem familiar, and they indeed correspond to the notation used in the sections of [Hidden Markov models](../../hidden-markov-models/) to refer to the:
- transition probability matrix ($A$)
- emission probabilities ($B$)
- sequence of observations ($O$)
- initial probability distribution ($pi$)

### Setup and Initialization

Next, some initial setup is done to set some variables that will be used later.

```
# Get the cardinality of the state space
N = A.shape[0]
# Set the initial state probabilities matrix with a uniform distribution if it was not given
pi = pi if pi is not None else np.full(N, 1 / N)
# Get the length of the observation sequence
T = len(O)
```

- The cardinality of the state space (i.e. how many states there are) is set as `N`.
- The initial state probabilities are set as `pi`.
- The length of the observation sequence is set as `T`.

Some matrices that will also be used in ensuing calculations are initialized.

```
viterbi_matrix = np.zeros((N, T))
backtracking_matrix = np.zeros((N, T)).astype(np.int32)
viterbi_matrix[:, 0] = pi * B[:, O[0]]
```

- The **_viterbi matrix_** (also called a _viterbi table_) is a probability matrix (or lattice) with one column for each observation $o_{t}$ and one row for each state, where each cell of the matrix $v(j,t)$ represents the probability that for a HMM $\lambda$, given the first $t$ observations and the most probable state sequence $q_{1}\dots q_{t-1}$, the HMM is in state $j$.
- The **_backtracking matrix_** is for keeping track of the most likely path so far. Like the viterbi matrix, each column of the backtracking matrix corresponds to an observation $o_{t}$, and each row corresponds to a state. Each cell of the matrix $b(j,t)$ represents the index of the state that is calculated to have the highest probability of being the _preceding_ state (at the $t-1$ th time step) to the state $j$ (at the $t$ th time step). When this matrix is filled out, the idea is to be able to determine which state is most likely to have come before a particular state, and to work backwards starting from the state at the $t$ th time step to construct the most likely sequence of (hidden) states.
- In addition to just setting all elements of both matrices to zeroes, the _viterbi matrix_'s first column is also set to be the product of the initial state probabilities (`pi`) and the probabilities of the first observation being generated from each state (`B[:, O[0]]`). In other words, this first column is set to be the probabilities that the first observation will be generated at the first time step for each of the states.

### Filling in the _viterbi_ and _backtracking_ matrices

After initialization and setup is complete, two for loops are used to step through all of the $T$ time steps apart from the first one (which was already handled previously when the first column of the _viterbi matrix_ was set), as well as through each of the $N$ states.

```
for t in range(1, T):
    for s in range(N):
        tmp_prod = viterbi_matrix[:, t - 1] * A[:, s]
        viterbi_matrix[s, t] = np.max(tmp_prod) * B[s, O[t]]
        backtracking_matrix[s, t] = np.argmax(tmp_prod)
```

The _viterbi_ and _backtracking_ matrices are updated as follows:
- first, the element-wise product of two columns from the _viterbi_ and transition probability matrices (`tmp_prod`) that will be used for updating the _viterbi_ and _backtracking_ matrices is calculated. The column from the _viterbi matrix_ represents the probabilities calculated for the _viterbi_matrix_ in the previous `t - 1`th time step (`viterbi_matrix[:, t - 1]`), and the column from the transition probability matrix represents the probabilities of transitioning from each state the state `s` (`A[:, s]`). These resulting probabilities calculated for `tmp_prod` are thus simply the probabilities that each of the states will be transitioned to at the current `t`th time step.
- each remaining unfilled column of the _viterbi matrix_ is then progressively filled for each time step `t` apart from the first one. The `t`th column is filled with the product of the maximum value found in `tmp_prod` that was computed previously (`np.max(tmp_prod)`) and the probabilities of the `t`th observation being generated from each state (`B[s, O[t]]`).
- each remaining unfilled column of the _backtracking_matrix_ is then progressively filled for each time step `t` apart from the first one. The `t`th column is filled with the indices of the maximum value in `tmp_prod` that was computed previously (`np.argmax(tmp_prod)`) for each state. The _back tracking_ matrix helps to keep track of the most likely path so far, and so the index of the maximum value found in `tmp_prod` is stored.

### Backtracking to get the optimal state sequence

With the _viterbi_ and _backtracking_ matrices completely filled, the optimal state sequence (i.e. the most likely sequence of hidden states given the sequence of observed events `O`) can simply be constructed by tracing through the `backtracking_matrix`, starting from its last column.
```
opt_state_sequence = np.zeros(T).astype(np.int32)
opt_state_sequence[-1] = int(np.argmax(viterbi_matrix[:, -1]))
for t in reversed(range(1, T)):
    opt_state_sequence[t - 1] = backtracking_matrix[opt_state_sequence[t], t]
```
The elements of `opt_state_sequence` are likewise filled in reverse order, starting from its last element, which is set to be the maximum value found from the last column of the _viterbi matrix_ (`int(np.argmax(viterbi_matrix[:, -1]))`). For each of the remaining elements of the `opt_state_sequence`, they are set as the term in `backtracking_matrix` that is in the `t + 1`th column and in the row that corresponds to the state previously filled in for the `t + 1`th element of `opt_state_sequence`. In other words, after the last element of `opt_state_sequence` (at time step `T`) is filled in using the _viterbi matrix_, the element (state) last filled-in and the _backtracking matrix_ is used to find the (index of the) state that was previously calculated to be most probable to be the preceding state (at the previous time step).