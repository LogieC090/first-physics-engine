# Oblique Collisions Between Two Spheres  
**Author:** Logan C  
**Date:** July 2026

---

## Introduction

Consider two spheres of masses $m_1$ and $m_2$, with initial velocities $\mathbf{u}_1$ and $\mathbf{u}_2$. During collision, the impulse acts along the *line of centres*, denoted by the unit vector $\mathbf{I}$.

Only the components of velocity **parallel** to $\mathbf{I}$ change during the collision; perpendicular components remain unchanged.

---

## Velocity Decomposition

For each sphere, decompose the velocity into parallel and perpendicular components:

$$
\mathbf{u}_i = u_{i\parallel}\mathbf{I} + \mathbf{u}_{i\perp},
\qquad i = 1,2.
$$

After the collision:

$$
\mathbf{v}_i = v_{i\parallel}\mathbf{I} + \mathbf{u}_{i\perp}.
$$

---

## Newton’s Law of Restitution

Newton’s law of restitution applies only to the parallel components:

$$
e = \frac{v_{2\parallel} - v_{1\parallel}}{u_{1\parallel} - u_{2\parallel}},
$$

where $e$ is the coefficient of restitution.

Rearranging:

$$
v_{2\parallel} - v_{1\parallel}
= -e\,(u_{2\parallel} - u_{1\parallel}).
$$

---

## Conservation of Momentum

Linear momentum parallel to $\mathbf{I}$ is conserved:

$$
m_1 u_{1\parallel} + m_2 u_{2\parallel}
= m_1 v_{1\parallel} + m_2 v_{2\parallel}.
$$

---

## Solving for the Final Velocities

Solving restitution + momentum conservation yields the standard 1D collision formulas:

$$
v_{1\parallel}
= \frac{m_1 u_{1\parallel} + m_2 u_{2\parallel}
      - m_2 e (u_{1\parallel} - u_{2\parallel})}
      {m_1 + m_2},
$$

$$
v_{2\parallel}
= \frac{m_1 u_{1\parallel} + m_2 u_{2\parallel}
      + m_1 e (u_{1\parallel} - u_{2\parallel})}
      {m_1 + m_2}.
$$

---

## Reconstructing the Final Velocity Vectors

The final velocity vectors are:

$$
\mathbf{v}_1 = v_{1\parallel}\mathbf{I} + \mathbf{u}_{1\perp},
\qquad
\mathbf{v}_2 = v_{2\parallel}\mathbf{I} + \mathbf{u}_{2\perp}.
$$

---

## Computing the Impulse Direction

Given sphere centres at $(x_1,y_1)$ and $(x_2,y_2)$, the line of centres is:

$$
\mathbf{I} =
\frac{(x_2 - x_1,\; y_2 - y_1)}
     {\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}}.
$$

Parallel and perpendicular components:

$$
u_{i\parallel} = \mathbf{u}_i \cdot \mathbf{I},
\qquad
\mathbf{u}_{i\perp} = \mathbf{u}_i - u_{i\parallel}\mathbf{I}.
$$

---

## Collision Condition

A collision occurs when the distance between centres satisfies:

$$
d = 2R,
$$

where $R$ is the radius of each sphere.

---

## Conclusion

This formulation allows efficient computation of post‑collision velocities for oblique collisions in a 2D physics engine. Only the parallel components change; perpendicular components remain unaffected.
