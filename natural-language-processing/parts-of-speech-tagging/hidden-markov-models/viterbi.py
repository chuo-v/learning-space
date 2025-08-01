#!/usr/bin/env python3

import numpy as np

def viterbi(A, B, O, pi=None):
    """
    Implementation of the Viterbi algorithm to find the most likely sequence of hidden states in a
    Hidden Markov Model given a sequence of observations.

    Parameters
    ----------
    A : np.ndarray (N x N)
        State transition probability matrix
    B : np.ndarray (N x K)
        Emission probabilities matrix.
    O : np.ndarray (T x 1)
        Observation sequence.
    pi: np.ndarray, optional (N x 1)
        Initial state probabilities matrix. If None, the distribution is assumed to be uniformly
        distributed.

    Returns
    -------
    opt_state_sequence : np.ndarray (T x 1)
        The optimal state sequence.
    viterbi_matrix     : np.ndarray (N x T)
        Path probability matrix for tracking the probability of the most likely path so far.
    backtracking_matrix: np.ndarray (N x T)
        Backtracking matrix to keep track of the most likely path so far.
    """
    # Get the cardinality of the state space
    N = A.shape[0]
    # Set the initial state probabilities matrix with a uniform distribution if it was not given
    pi = pi if pi is not None else np.full(N, 1 / N)
    # Get the length of the observation sequence
    T = len(O)

    # Initialize matrices
    viterbi_matrix = np.zeros((N, T))
    backtracking_matrix = np.zeros((N, T)).astype(np.int32)
    viterbi_matrix[:, 0] = pi * B[:, O[0]]

    # Calculate probabilities using a nested loop
    for t in range(1, T):
        for s in range(N):
            tmp_prod = viterbi_matrix[:, t - 1] * A[:, s]
            viterbi_matrix[s, t] = np.max(tmp_prod) * B[s, O[t]]
            backtracking_matrix[s, t] = np.argmax(tmp_prod)

    # Backtrack to find optimal state sequence
    opt_state_sequence = np.zeros(T).astype(np.int32)
    opt_state_sequence[-1] = int(np.argmax(viterbi_matrix[:, -1]))
    for t in reversed(range(1, T)):
        opt_state_sequence[t - 1] = backtracking_matrix[opt_state_sequence[t], t]

    return opt_state_sequence, viterbi_matrix, backtracking_matrix


## Examples

# Example 1

A = np.array([
    [0.3, 0.7],
    [0.6, 0.4]
])
B = np.array([
    [0.4, 0.5, 0.1],
    [0.1, 0.6, 0.3]
])
O = np.array([0, 1, 2])
pi = [0.7, 0.3]

opt_state_sequence, viterbi_matrix, backtracking_matrix = viterbi(A, B, O, pi)
print(opt_state_sequence) # output: [0 1 1]

# Example 2

A = np.array([[0.3, 0.6, 0.1],
              [0.7, 0.1, 0.2],
              [0.3, 0.1, 0.6]])
B = np.array([[0.5, 0.0, 0.5],
              [0.0, 0.8, 0.2],
              [0.0, 0.3, 0.7]])
O = np.array([1, 0, 1, 2, 1, 2])

opt_state_sequence, viterbi_matrix, backtracking_matrix = viterbi(A, B, O)
print(opt_state_sequence) # output: [1 0 1 0 1 0]