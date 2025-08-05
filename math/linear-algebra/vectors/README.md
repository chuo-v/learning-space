# Vectors

## Theorems

### Algebraic Properties of Vectors in $\mathbb{R}^{n}$

Let $\boldsymbol{u}$, $\boldsymbol{v}$ and $\boldsymbol{w}$ be vectors in $\mathbb{R}^{n}$, and let $c$ and $d$ be scalars. Then

- $\boldsymbol{u} + \boldsymbol{v} = \boldsymbol{v} + \boldsymbol{u}$ (commutativity)
- $(\boldsymbol{u} + \boldsymbol{v}) + \boldsymbol{w} = \boldsymbol{u} + (\boldsymbol{v} + \boldsymbol{w})$ (associativity)
- $\boldsymbol{u} + (\boldsymbol{-u}) = 0$
- $\boldsymbol{u} + \boldsymbol{0} = \boldsymbol{u}$
- $c(\boldsymbol{u} + \boldsymbol{v})=c\boldsymbol{u} + c\boldsymbol{v}$ (distributivity)
- $(c+d)\boldsymbol{u}=c\boldsymbol{u}+d\boldsymbol{u}$ (distributivity)
- $c(d\boldsymbol{u})=(cd)\boldsymbol{u}$
- $1\boldsymbol{u}=\boldsymbol{u}$

### Main Properties of the Dot Product

Let $\boldsymbol{u}$, $\boldsymbol{v}$ and $\boldsymbol{w}$ be vectors in $\mathbb{R}^{n}$, and let $c$ be a scalar. Then
- $\boldsymbol{u}\cdot\boldsymbol{v}=\boldsymbol{v}\cdot\boldsymbol{u}$ (commutativity)
- $\boldsymbol{u}\cdot(\boldsymbol{v}+\boldsymbol{w})=\boldsymbol{u}\cdot\boldsymbol{v}+\boldsymbol{u}\cdot\boldsymbol{w}$ (distributivity)
- $(c\boldsymbol{u})\cdot\boldsymbol{v}=c(\boldsymbol{u}\cdot\boldsymbol{v})$
- $\boldsymbol{u}\cdot\boldsymbol{u}\geq 0$ and $\boldsymbol{u}\cdot\boldsymbol{u}=0$ if and only if $\boldsymbol{u}=\boldsymbol{0}$

### Main Properties of Vector Length

Let $\boldsymbol{u}$ be a vector in $\mathbb{R}^{n}$, and let $c$ be a scalar. Then
- $\lVert\boldsymbol{u}\rVert=0$ if and only if $\boldsymbol{u}=\boldsymbol{0}$
- $\lVert c\boldsymbol{u}\rVert=\lvert c\rvert\lVert\boldsymbol{u}\rVert$

### The Cauchy-Schwarz Inequality

For all vectors $\boldsymbol{u}$ and $\boldsymbol{v}$ in $\mathbb{R}^{n}$,

$$
\lvert\boldsymbol{u}\cdot\boldsymbol{v}\rvert\leq\lVert\boldsymbol{u}\rVert\lVert\boldsymbol{v}\rVert
$$

### The Triangle Inequality

For all vectors $\boldsymbol{u}$ and $\boldsymbol{v}$ in $\mathbb{R}^{n}$,

$$
\lVert\boldsymbol{u}+\boldsymbol{v}\rVert\leq\lVert\boldsymbol{u}\rVert+\lVert\boldsymbol{v}\rVert
$$

### Pythagoras' Theorem

For all vectors $\boldsymbol{u}$ and $\boldsymbol{v}$ in $\mathbb{R}^{n}$, the following is true if and only if $\boldsymbol{u}$ and $\boldsymbol{v}$ are orthogonal.

$$
\lVert\boldsymbol{u}+\boldsymbol{v}\rVert^{2}=\lVert\boldsymbol{u}\rVert^{2}+\lVert\boldsymbol{v}\rVert^{2}
$$

## Definitions

### Dot Product and Angles

For nonzero vectors $\boldsymbol{u}$ and $\boldsymbol{v}$ in $\mathbb{R}^{n}$,

$$
cos\ \theta=\frac{\boldsymbol{u}\cdot\boldsymbol{v}}{\lVert\boldsymbol{u}\rVert\lVert\boldsymbol{v}\rVert}
$$

### Orthogonal Vectors

Two vectors  $\boldsymbol{u}$ and $\boldsymbol{v}$ in $\mathbb{R}^{n}$ are orthogonal to each other if $\boldsymbol{u}\cdot\boldsymbol{v}=0$

### Projections

For vectors $\boldsymbol{u}$ and $\boldsymbol{v}$ in $\mathbb{R}^{n}$, if $\boldsymbol{u}\neq\boldsymbol{0}$, then the projection of $\boldsymbol{v}$ onto $\boldsymbol{u}$ is

$$
proj_{\boldsymbol{u}}(\boldsymbol{v})=\biggl(\frac{\boldsymbol{u}\cdot\boldsymbol{v}}{\lVert\boldsymbol{u}\rVert^{2}}\biggr)\boldsymbol{u}=\biggl(\frac{\boldsymbol{u}\cdot\boldsymbol{v}}{\boldsymbol{u}\cdot\boldsymbol{u}}\biggr)\boldsymbol{u}
$$