# A Practical Example

1. Prove that $\frac{sin A}{1 + cos A} + \frac{cos A}{sin A} = csc A$:

**Solution**

$$
\text{Starting from left:}
\frac{sin A}{1 + cos A} + \frac{cos A}{sin A} = \frac{sin A \cdot sin A + cos A (1 + cos A)}{(1 + cos A) sin A}
\frac{sin^2 A + cos A + cos^2 A}{(1 + cos A) sin A} \\
\text{Then cancelling both $1 + cos A$:} \\
\frac{1 + cos A}{(1 + cos A) sin A} \\
\frac{1}{sin A} = csc A
$$

This example is generated with: `simtex -b -i='examples/2/example_2.md'  -T='A practical example' -a='iaacornus'`
