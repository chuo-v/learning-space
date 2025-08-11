# Matrices

## Theorems

### Algebraic Properties of Matrices

#### Algebraic Properties of Matrix Addition and Scalar Multiplication

Let $A$, $B$ and $C$ be matrices of the same size, and let $s$ and $t$ be scalars.

- $A+B=B+A$ (commutativity)
- $(A+B)+C=A+(B+C)$ (associativity)
- $A+(-A)=O$
- $A+O=A$
- $s(tB)=(st)B$
- $s(A+B)=sA+sB$ (distributivity)
- $(s+t)C=sC+tC$ (distributivity)
- $1A=A$

#### Algebraic Properties of Matrix Multiplication

Let $A$, $B$ and $C$ be matrices where their sizes are such that the following operations can be done, and let $t$ be a scalar.

- $A(BC)=(AB)C$ (associativity)
- $A(B+C)=AB+AC$ (left distributivity)
- $(A+B)C=AC+BC$ (right distributivity)
- $t(AB)=(tA)B=A(tB)$
- $I_{m}C=C=CI_{n}$ if $C$ is $m \times n$ (multiplicative identity)

### Properties of Matrix Transpose

Let $A$ and $B$ be matrices where their sizes are such that the following operations can be done, and let $s$ be a scalar.

- $(A^{T})T=A$
- $(A+B)^{T}=A^{T}+B^{T}$
- $(AB)^{T}=B^{T}A^{T}$
- $(sA)^{T}=sA^{T}$
- $(A^{r})^{T}=(A^{T})^{r}$ for all nonnegative integers $r$

### Symmetric Matrices

- If $A$ is a square matrix, then $A+A^{T}$ is a symmetric matrix
- For any matrix $A$, $AA^{T}$ and $A^{T}A$ are symmetric matrices

### Matrix Inverses

- If $A$ is a $n \times n$ matrix, $A$ is invertible if it has an inverse $A'$ where $AA'=I$ and $A'A=I$, where the inverse is unique
- If $A$ is an invertible matrix, then $A^{-1}$ is invertible and $(A^{-1})^{-1}=A$
- If $A$ is an invertible matrix and s is a nonzero scalar, then $(sA)^{-1}=\frac{1}{s}A^{-1}$
- If $A$ and $B$ are invertible matrices of the same size, then $AB$ is invertible where $AB^{-1}=B^{-1}A^{-1}$
- If $A$ is an invertible matrix, then $A^{T}$ is invertible and $(A^{T})^{-1}=(A^{-1})^{T}$
- If $$A is an invertible matrix, then $A^{n}$ is invertible for all nonnegative integers $n$, and $(A^{n})^{-1}=(A^{-1})^{n}=A^{-n}$

### LU Factorization

- If $A$ is a square matrix, $A$ has a LU factorization if it can be reduced to row echelon form _without changing the order of its rows_
- If $A$ is an invertible matrix that has an LU factorization, then $L$ and $U$ are unique
- Every square matrix has a $P^{T}LU$ factorization, where $P$ is a **permutation matrix** (that performs row interchange to a matrix when multiplied with it)

### Subspaces

Let $A$ be a $m \times n$ matrix. Then
- $row(A)$, the _row space_ of $A$, is the subspace of $\mathbb{R}^{n}$ spanned by the rows of $A$
- $col(A)$, the _column space_ of $A$, is the subspace of $\mathbb{R}^{n}$ spanned by the columns of $A$
- $row(A)=row(B)$ if $B$ is a matrix that is _row equivalent_ to $A$
- The set of solutions of $A\boldsymbol{x}=\boldsymbol{0}$ is a subspace of $\mathbb{R}^{n}$
- The _null space_ of $A$, denoted as $null(A)$, is the subspace of the set of $\mathbb{R}^{n}$ that consists of solutions to $A\boldsymbol{x}=\boldsymbol{0}$
- A *basis* for a subspace of $\mathbb{R}^{n}$ is a set of vectors in the subspace that (1) spans the subspace, and (2) is linearly independent
- **The basis theorem** states that any two bases for a subspace of $\mathbb{R}^{n}$ have the same number of vectors, which is also referred to as the _dimension_ of the subspace
- $row(A)$ and $col(A)$ have the same dimension, which is equivalent to the *rank* of $A$, and is also equivalent to the *rank* of $A^{T}$.
- The _nullity_ of $A$ is the dimension of its null space
- **The rank theorem** states that $rank(A)+nullity(A)=n$
- $rank(A^{T}A)=rank(A)$
- $A^{T}A$ is only invertible if the $rank(A)=n$
- If $\mathbb{B}=\\{\boldsymbol{v_{1}},\boldsymbol{v_{2}},\dots,\boldsymbol{v_{k}}\\}$ is a _basis_ for a subspace of $\mathbb{R}^{n}$, then for every vector $\boldsymbol{v}$ in $\mathbb{R}^{n}$, there is exactly one way to write $\boldsymbol{v}$ as a _linear combination_ of the vectors in the _basis_ (i.e. as $\boldsymbol{v}=c_{1}\boldsymbol{v_{1}}+c_{2}\boldsymbol{v_{2}}+\cdots+c_{n}\boldsymbol{v_{k}}$)
  - the coefficients $c_{1},c_{2},\dots,c_{n}$ are called the _coordinates of_ $\boldsymbol{v}$ _with respect to_ $\mathbb{B}$, and the vector that comprises of the coefficients is called the _coordinate vector of_ $\boldsymbol{v}$ _with respect to_ $\mathbb{B}$.

### The Fundamental Theorem of Invertible Matrices

Let $A$ be a $n \times n$ matrix, and let $T: Y\rightarrow Z$ be a linear transformation where $A$ is the matrix of $[T]_{C \leftarrow B}$ with respect to the bases $B$ and $C$ of $Y$ and $Z$, respectively.

Then the following statements are equivalent:
- $A$ is invertible
- $A\boldsymbol{x}=\boldsymbol{b}$ has a unique solution for every $\boldsymbol{b}$ in $\mathbb{R}^{n}$
- There is only the trivial solution for $A\boldsymbol{x}=\boldsymbol{0}$
- The _reduced row echelon form_ of $A$ is $I_{n}$
- $A$ is a product of elementary matrices
- The column vectors of $A$ are linearly independent
- The column vectors of $A$ span $\mathbb{R}^{n}$
- The column vectors of $A$ form a basis for $\mathbb{R}^{n}$
- The row vectors of $A$ are linearly independent
- The row vectors of $A$ span $\mathbb{R}^{n}$
- The row vectors of $A$ form a basis for $\mathbb{R}^{n}$
- $nullity(A)=0$
- $rank(A)=n$
- $det(A)\neq 0$, where $det(A)$ is the determinant of $A$
- 0 is not an eigenvalue of $A$
- $T$ is invertible
- The kernel of $T$ is $\\{\boldsymbol{0}\\}$
- The range of $T$ is $Z$
- $T$ is one-to-one
- $T$ is onto


## Definitions

### Elementary Matrices

An **elementary matrix** is any matrix that results from elementary row operations being performed on an identity matrix. Each elementary matrix is invertible, where its inverse is also an elementary matrix.