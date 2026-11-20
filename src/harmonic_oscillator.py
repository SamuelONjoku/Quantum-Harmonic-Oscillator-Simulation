
"""
Quantum Harmonic Oscillator Simulation

Analytical calculation and visualization of the
one-dimensional quantum harmonic oscillator.

Dimensionless units are used:
hbar = m = omega = 1.
"""

import numpy as np
import matplotlib.pyplot as plt

from pathlib import Path
from scipy.special import eval_hermite, gammaln


# --------------------------------------------------
# 1. Model parameters
# --------------------------------------------------

MAX_STATE = 4
X_MIN = -5.0
X_MAX = 5.0
NUM_POINTS = 1000

x = np.linspace(X_MIN, X_MAX, NUM_POINTS)


# --------------------------------------------------
# 2. Analytical energy eigenvalues
# --------------------------------------------------

def energy_eigenvalue(n):
    """
    Calculate the dimensionless energy eigenvalue.

    E_n = n + 1/2

    Parameters
    ----------
    n : int
        Quantum number (n >= 0).

    Returns
    -------
    float
        Dimensionless energy eigenvalue.
    """
    if not isinstance(n, (int, np.integer)) or n < 0:
        raise ValueError("Quantum number must be a non-negative integer.")

    return n + 0.5


# --------------------------------------------------
# 3. Normalized wavefunctions
# --------------------------------------------------

def wavefunction(n, x):
    """
    Calculate the normalized harmonic oscillator
    eigenfunction in dimensionless coordinates.

    psi_n(x) = N_n H_n(x) exp(-x^2 / 2)
    """
    if not isinstance(n, (int, np.integer)) or n < 0:
        raise ValueError("Quantum number must be a non-negative integer.")

    normalization = np.exp(
        -0.25 * np.log(np.pi)
        -0.5 * (n * np.log(2) + gammaln(n + 1))
    )

    hermite_polynomial = eval_hermite(n, x)

    return (
        normalization
        * hermite_polynomial
        * np.exp(-0.5 * x**2)
    )


# --------------------------------------------------
# 4. Probability density
# --------------------------------------------------

def probability_density(n, x):
    """
    Calculate the probability density |psi_n(x)|^2.
    """
    psi = wavefunction(n, x)
    return np.abs(psi)**2


# --------------------------------------------------
# 5. Output directory
# --------------------------------------------------

output_dir = Path("figures")
output_dir.mkdir(exist_ok=True)


# --------------------------------------------------
# 6. Plot wavefunctions
# --------------------------------------------------

plt.figure(figsize=(9, 6))

for n in range(MAX_STATE):
    psi = wavefunction(n, x)
    plt.plot(x, psi, label=f"n = {n}")

plt.xlabel("Dimensionless position")
plt.ylabel("Wavefunction")
plt.title("Quantum Harmonic Oscillator Wavefunctions")
plt.axhline(0, linewidth=0.8)
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()

plt.savefig(
    output_dir / "wavefunctions.png",
    dpi=300
)


# --------------------------------------------------
# 7. Plot probability densities
# --------------------------------------------------

plt.figure(figsize=(9, 6))

for n in range(MAX_STATE):
    density = probability_density(n, x)
    plt.plot(x, density, label=f"n = {n}")

plt.xlabel("Dimensionless position")
plt.ylabel("Probability density")
plt.title("Quantum Harmonic Oscillator Probability Densities")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()

plt.savefig(
    output_dir / "probability_densities.png",
    dpi=300
)


# --------------------------------------------------
# 8. Plot energy eigenvalues
# --------------------------------------------------

plt.figure(figsize=(8, 5))

for n in range(MAX_STATE):
    energy = energy_eigenvalue(n)

    plt.hlines(
        energy,
        -1,
        1,
        label=f"n = {n}, E = {energy:.1f}"
    )

plt.xlabel("Position (arbitrary)")
plt.ylabel("Dimensionless energy")
plt.title("Quantum Harmonic Oscillator Energy Levels")
plt.yticks(
    [energy_eigenvalue(n) for n in range(MAX_STATE)]
)
plt.legend()
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()

plt.savefig(
    output_dir / "energy_levels.png",
    dpi=300
)

plt.show()


# --------------------------------------------------
# 9. Print energy eigenvalues
# --------------------------------------------------

print("Quantum Harmonic Oscillator Energy Eigenvalues")
print("----------------------------------------------")

for n in range(MAX_STATE):
    print(
        f"n = {n}: "
        f"E_n = {energy_eigenvalue(n):.4f}"
    )
