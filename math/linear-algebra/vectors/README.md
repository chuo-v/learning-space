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

### Equations of a line

The **normal form** of the equation of a line $L$ in in $\mathbb{R}^{2}$ is

$$
\boldsymbol{n}\cdot(\boldsymbol{x}-\boldsymbol{p})=0
$$

where $\boldsymbol{n}\neq 0$ is the normal vector for $L$, and $\boldsymbol{p}$ is a point on $L$.

The **vector form** of the equation of a line $L$ in in $\mathbb{R}^{2}$ or $\mathbb{R}^{3}$ is

$$
\boldsymbol{x}=\boldsymbol{p}+t\boldsymbol{d}
$$

where $\boldsymbol{d}\neq\boldsymbol{0}$ is a direction vector for $L$, and $\boldsymbol{p}$ is a point on $L$.

### Equations of a plane

The **normal form** of the equation of a plane $P$ in in $\mathbb{R}^{3}$ is

$$
\boldsymbol{n}\cdot(\boldsymbol{x}-\boldsymbol{p})=0
$$

where $\boldsymbol{n}\neq 0$ is the normal vector for $P$, and $\boldsymbol{p}$ is a point on $P$.

The **vector form** of the equation of a plane $P$ in in $\mathbb{R}^{3}$ is

$$
\boldsymbol{x}=\boldsymbol{p}+s\boldsymbol{d}+t\boldsymbol{e}
$$

where $\boldsymbol{d}\neq\boldsymbol{0}$ and $\boldsymbol{e}\neq\boldsymbol{0}$ are a direction vectors for $P$ that are not parallel to each other, and $\boldsymbol{p}$ is a point on $P$.

### Cross Product

A way to get the normal vector for a plane in $\mathbb{R}^{3}$ with the following vector form is the cross product of $\boldsymbol{d}$ and $\boldsymbol{e}$.

$$
\boldsymbol{x}=\boldsymbol{p}+s\boldsymbol{d}+t\boldsymbol{e}
$$

The cross product of $\boldsymbol{d}$ and $\boldsymbol{e}$ is

$$
\boldsymbol{d} \times \boldsymbol{e}=
\begin{bmatrix}
d_{2}e_{3}-d_{3}e_{2} \\
d_{3}e_{1}-d_{1}e_{3} \\
d_{1}e_{2}-d_{2}e_{1}
\end{bmatrix}
$$

where $d_{i}$ and $e_{i}$ for $i=1,2,3$ are the elements of $\boldsymbol{d}$ and $\boldsymbol{e}$, repsectively.

## Miscellaneous Formulas

### "Balancing Formula" for Dimensions

The "balancing formula" gives the relationship between the following
- dimension of an object (e.g. line, plane)
- number of equations needed to represent the object
- dimension of the space (e.g. 2 for $\mathbb{R}^{2}$, 3 for $\mathbb{R}^{3}$)

as

$$
(dimension\ of\ the\ object)\ +\ (number\ of\ equations)=dimension\ of\ the\ space
$$

e.g. A plane in $\mathbb{R}^{3}$ needs $3-2=1$ equation.

### Distances to a line

If line $L$ is in $\mathbb{R}^{2}$ with the general form $ax+by=c$, then the distance from a point $P=(x_{0},y_{0})$ to the line is given as

$$
\frac{\lvert ax_{0}+by_{0}-c \rvert}{\sqrt{a^{2}+b^{2}}}
$$

### Distances to a plane

If plane $P$ is in $\mathbb{R}^{3}$ with the general form $ax+by+cz=d$, then the distance from a point $P=(x_{0},y_{0},z_{0})$ to the plane is given as

$$
\frac{\lvert ax_{0}+by_{0}+cz_{0}-d \rvert}{\sqrt{a^{2}+b^{2}+c^{2}}}
$$