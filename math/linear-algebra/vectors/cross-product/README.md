# Cross Product

## Definition of the Cross Product

The cross product of two vectors, $\boldsymbol{a}=\langle a_{1},\,a_{2},\,a_{3} \rangle$ and $\boldsymbol{b}=\langle b_{1},\,b_{2},\,b_{3} \rangle$ is the vector

$$
\boldsymbol{a}\times\boldsymbol{b}=\langle a_{2}b_{3}-a_{3}b_{2},\,a_{3}b_{1}-a_{1}b_{3},\,a_{1}b_{2}-a_{2}b_{1} \rangle
$$

Another way to remember this is as follows, where $\boldsymbol{i}$, $\boldsymbol{j}$, $\boldsymbol{k}$ are the standard unit vectors.

$$
\boldsymbol{a}\times\boldsymbol{b}=\begin{vmatrix}a_{2}&a_{3} \\\ b_{2}&b_{3}\end{vmatrix}\boldsymbol{i}-\begin{vmatrix}a_{1}&a_{3} \\\ b_{1}&b_{3}\end{vmatrix}\boldsymbol{j}+\begin{vmatrix}a_{1}&a_{2} \\\ b_{2}&b_{1}\end{vmatrix}\boldsymbol{k}
$$

## Properties of the Cross Product

$$
\boldsymbol{a} \times \boldsymbol{b}=-\boldsymbol{b} \times \boldsymbol{a}
$$
$$
\boldsymbol{a} \times (\boldsymbol{b}+\boldsymbol{c})=\boldsymbol{a} \times \boldsymbol{b} + \boldsymbol{a} \times \boldsymbol{c}
$$
$$
(\boldsymbol{a}+\boldsymbol{b}) \times \boldsymbol{c}=\boldsymbol{a} \times \boldsymbol{c} + \boldsymbol{b} \times \boldsymbol{c}
$$
$$(c\boldsymbol{a})\times\boldsymbol{b}=c(\boldsymbol{a}\times\boldsymbol{b})=\boldsymbol{a}\times(c\boldsymbol{b})
$$
$$\boldsymbol{a}\cdot(\boldsymbol{b}\times\boldsymbol{c})=(\boldsymbol{a}\times\boldsymbol{b})\cdot\boldsymbol{c}
$$
$$\boldsymbol{a}\times(\boldsymbol{b}\times\boldsymbol{c})=(\boldsymbol{a}\cdot\boldsymbol{c})\boldsymbol{b}-(\boldsymbol{a}\cdot\boldsymbol{b})\boldsymbol{c}
$$

The following is also known:
- $\boldsymbol{a}\times\boldsymbol{b}$ is orthogonal to both $\boldsymbol{a}$ and $\boldsymbol{b}$
- The length of the cross product is $|\boldsymbol{a} \times \boldsymbol{b}|=|\boldsymbol{a}||\boldsymbol{b}|sin(\theta)$, where $\theta$ is the angle between $\boldsymbol{a}$ and $\boldsymbol{b}$
  - this length is equal to the area of the parallelogram determined by $\boldsymbol{a}$ and $\boldsymbol{b}$
- Two non-zero vectors $\boldsymbol{a}$ and $\boldsymbol{b}$ are parallel if and only if $\boldsymbol{a}\times\boldsymbol{b}=\boldsymbol{0}$

## Standard Basis Vectors

The following are the cross products of the standard basis vectors.

$$
\boldsymbol{i}\times\boldsymbol{j}=\boldsymbol{k}\quad\quad\boldsymbol{j}\times\boldsymbol{i}=-\boldsymbol{k}
$$
$$
\boldsymbol{j}\times\boldsymbol{k}=\boldsymbol{i}\quad\quad\boldsymbol{k}\times\boldsymbol{j}=-\boldsymbol{i}
$$
$$
\boldsymbol{k}\times\boldsymbol{i}=\boldsymbol{j}\quad\quad\boldsymbol{i}\times\boldsymbol{k}=-\boldsymbol{j}
$$

## Triple Products

The product $\boldsymbol{a}\cdot(\boldsymbol{b}\times\boldsymbol{c})$ is the scalar triple product of the three vectors $\boldsymbol{a}$, $\boldsymbol{b}$ and $\boldsymbol{c}$, where

$$
\boldsymbol{a}\cdot(\boldsymbol{b}\times\boldsymbol{c})=\begin{vmatrix}a_{1}&a_{2}&a_{3} \\\ b_{1}&b_{2}&b_{3} \\\ c_{1}&c_{2}&c_{3}\end{vmatrix}
$$

The volume of the parallelepiped determined by $\boldsymbol{a}$, $\boldsymbol{b}$ and $\boldsymbol{c}$ is the magnitude of their scalar product:

$$
V=|\boldsymbol{a}\cdot(\boldsymbol{b}\times\boldsymbol{c})|
$$