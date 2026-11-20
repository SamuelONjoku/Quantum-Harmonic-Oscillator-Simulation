# Quantum Harmonic Oscillator Simulation

## Project Overview

This project investigates the one-dimensional quantum harmonic oscillator through mathematical formulation and computational simulation using Python.

The objective is to implement and visualize the quantum mechanical properties of the harmonic oscillator, including its energy eigenvalues, eigenfunctions, and probability density distributions.

This project serves as a foundation for computational studies in quantum mechanics and theoretical chemistry.

## Scientific Background

The one-dimensional quantum harmonic oscillator is described by the time-independent Schrödinger equation:

\[
\hat{H}\psi_n(x)=E_n\psi_n(x)
\]

where the Hamiltonian is

\[
\hat{H}=-\frac{\hbar^2}{2m}\frac{d^2}{dx^2}
+\frac{1}{2}m\omega^2x^2.
\]

Here:

- \(m\) is the particle mass.
- \(\omega\) is the angular frequency.
- \(\hbar\) is the reduced Planck constant.
- \(x\) is the position coordinate.
- \(\psi_n(x)\) is the nth energy eigenfunction.
- \(E_n\) is the corresponding energy eigenvalue.

The analytical energy eigenvalues are

\[
E_n=\hbar\omega\left(n+\frac{1}{2}\right),
\qquad n=0,1,2,\ldots
\]

## Project Objectives

1. Formulate the quantum harmonic oscillator Hamiltonian.
2. Calculate the analytical energy eigenvalues.
3. Compute and visualize quantum wavefunctions.
4. Plot probability density distributions.
5. Explore the behavior of different quantum energy states.
6. Compare numerical results with analytical solutions.

## Computational Tools

- Python
- NumPy
- SciPy
- Matplotlib

## Planned Project Structure

```text
Quantum-Harmonic-Oscillator-Simulation/
│
├── README.md
├── requirements.txt
├── src/
│   └── harmonic_oscillator.py
├── figures/
└── results/
```

## Project Status

**Status: Initial development**

The mathematical framework and computational objectives are established. Numerical implementation, visualization, and validation will be developed progressively.

## Expected Outcomes

The completed project will provide reproducible computational demonstrations of quantum harmonic oscillator energy levels, wavefunctions, and probability densities.

## Research Relevance

The quantum harmonic oscillator is a foundational model in quantum mechanics and theoretical chemistry. Understanding its analytical and numerical properties provides a basis for studying more complex quantum systems and computational quantum dynamics.

## Author

**Samuel O. Njoku**

Independent Researcher in Theoretical Chemistry

- GitHub: https://github.com/SamuelONjoku
- ORCID: https://orcid.org/0000-0002-0149-6269




## Reproducibility and Installation

The simulation can be reproduced using Python 3.12 and the scientific computing libraries listed in `requirements.txt`.

### 1. Clone the Repository

```bash
git clone https://github.com/SamuelONjoku/Quantum-Harmonic-Oscillator-Simulation.git
cd Quantum-Harmonic-Oscillator-Simulation
```

### 2. Create a Python Environment

Using Anaconda or Miniconda:

```bash
conda create -n quantum-research-312 python=3.12
conda activate quantum-research-312
```

### 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the Simulation

Execute the main Python script:

```bash
python src/harmonic_oscillator.py
```

The program calculates the analytical energy eigenvalues for the first four quantum harmonic oscillator states and generates the corresponding visualizations.

### 5. Generated Outputs

The simulation generates the following figures in the `figures/` directory:

- `wavefunctions.png` — Harmonic oscillator wavefunctions.
- `probability_densities.png` — Probability density distributions.
- `energy_levels.png` — Energy eigenvalue diagram.

### Computational Requirements

- Python 3.12
- NumPy
- SciPy
- Matplotlib

For details about the theoretical model, numerical checks, and validation results, see [VALIDATION.md](VALIDATION.md).


## Author

**Samuel O. Njoku**

Independent Researcher in Theoretical Chemistry

- GitHub: https://github.com/SamuelONjoku
- ORCID: https://orcid.org/0000-0002-0149-6269
