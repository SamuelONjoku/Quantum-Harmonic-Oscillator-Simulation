# Scientific Validation

## 1. Overview

This document presents the theoretical and numerical validation of the Quantum Harmonic Oscillator Simulation.

The simulation calculates the analytical energy eigenvalues and eigenfunctions of a one-dimensional quantum harmonic oscillator. The implementation was tested using energy-spectrum verification, wavefunction normalization, and eigenfunction orthogonality.

## 2. Theoretical Model

The dimensionless Hamiltonian of the one-dimensional quantum harmonic oscillator is

\[
\hat{H}=-\frac{1}{2}\frac{d^2}{dx^2}+\frac{1}{2}x^2.
\]

The analytical energy eigenvalues are

\[
E_n=n+\frac{1}{2}, \qquad n=0,1,2,\ldots
\]

The normalized analytical eigenfunctions are

\[
\psi_n(x)=
\frac{H_n(x)e^{-x^2/2}}
{\pi^{1/4}\sqrt{2^n n!}},
\]

where \(H_n(x)\) represents the physicists' Hermite polynomial.

The probability density is

\[
P_n(x)=|\psi_n(x)|^2.
\]

## 3. Computational Implementation

The simulation uses Python with the following scientific libraries:

- NumPy: numerical arrays and integration.
- SciPy: Hermite polynomial evaluation and mathematical functions.
- Matplotlib: scientific visualization.

The computational grid consists of 1,000 equally spaced points over the interval

\[
-5\leq x\leq 5.
\]

The first four quantum states, \(n=0,1,2,3\), were evaluated.

## 4. Energy Eigenvalue Verification

The calculated energy eigenvalues were compared with the analytical spectrum.

| Quantum number | Calculated energy | Analytical energy |
|---|---:|---:|
| 0 | 0.5000 | 0.5000 |
| 1 | 1.5000 | 1.5000 |
| 2 | 2.5000 | 2.5000 |
| 3 | 3.5000 | 3.5000 |

The calculated values agree with the analytical energy spectrum.

## 5. Wavefunction Normalization

The normalization condition is

\[
\int_{-\infty}^{+\infty}|\psi_n(x)|^2\,dx=1.
\]

Numerical integration over the computational grid produced the following results:

| Quantum state | Numerical integral |
|---|---:|
| n = 0 | 1.00000000 |
| n = 1 | 1.00000000 |
| n = 2 | 1.00000000 |
| n = 3 | 0.99999997 |

The results demonstrate excellent numerical normalization over the selected finite spatial interval.

## 6. Eigenfunction Orthogonality

The orthogonality condition is

\[
\int_{-\infty}^{+\infty}
\psi_m^*(x)\psi_n(x)\,dx=\delta_{mn}.
\]

The calculated overlap matrix, rounded to eight decimal places, is

\[
S\approx
\begin{pmatrix}
1&0&0&0\\
0&1&0&0\\
0&0&1&0\\
0&0&0&0.99999997
\end{pmatrix}.
\]

The diagonal elements are approximately unity, while the off-diagonal elements are approximately zero.

This confirms the expected orthonormality of the first four harmonic oscillator eigenfunctions to numerical accuracy.

## 7. Generated Visualizations

The simulation successfully generated three figures:

1. `figures/wavefunctions.png` — first four harmonic oscillator eigenfunctions.
2. `figures/probability_densities.png` — probability densities of the first four quantum states.
3. `figures/energy_levels.png` — energy eigenvalue spectrum.

## 8. Validation Summary

The following checks were completed successfully:

- Analytical energy eigenvalue verification.
- Numerical wavefunction normalization.
- Numerical eigenfunction orthogonality.
- Generation of scientific visualization figures.

The results are consistent with the analytical solution of the one-dimensional quantum harmonic oscillator.

## 9. Limitations and Future Improvements

The current implementation evaluates analytical eigenfunctions rather than independently solving the Schrödinger equation numerically.

Future improvements may include:

- Numerical solution of the time-independent Schrödinger equation.
- Comparison between analytical and numerical eigenvalues.
- Investigation of higher excited states.
- Grid-resolution and spatial-domain convergence studies.
- Extension to anharmonic oscillator potentials.

## 10. Conclusion

The implementation reproduces the expected analytical energy spectrum and eigenfunction properties of the one-dimensional quantum harmonic oscillator.

The normalization and orthogonality tests provide numerical evidence supporting the correctness of the implemented analytical wavefunctions.

This project establishes a foundation for further computational investigations in quantum mechanics and theoretical chemistry.
