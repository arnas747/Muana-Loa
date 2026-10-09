from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

# Parameterverdiene fra oppgave e).
a = 406.91766300
b = 2.86960568
c = 2.78204851
d = 6.29604630
f = -0.60909629


def F(x):
    return a + b * x + c * np.sin(d * x + f)


# 1. januar 2027 tilsvarer x = 5.
co2_nyttaar = F(5)
print(f"Forventet CO₂-konsentrasjon 1. januar 2027: {co2_nyttaar:.2f} ppm")

# Fra 1. januar 2022 til og med hele 2027.
x_plot = np.linspace(0, 6, 2000)
y_plot = F(x_plot)

plt.figure(figsize=(10, 5.4))
plt.plot(x_plot, y_plot, label="Tilpasset modell F(x)")

# Marker starten på 2027.
plt.scatter(
    5,
    co2_nyttaar,
    color="black",
    label=f"1. januar 2027: {co2_nyttaar:.2f} ppm",
    zorder=3,
)

# Fremhever prognoseperioden for 2027.
plt.axvspan(5, 6, color="orange", alpha=0.15, label="Prognose for 2027")

plt.xticks(
    np.arange(7),
    ["2022", "2023", "2024", "2025", "2026", "2027", "2028"],
)
plt.xlim(0, 6)
plt.xlabel("År")
plt.ylabel("CO₂-konsentrasjon (ppm)")
plt.title("Oppgave h): CO₂-modell fra 2022 til og med 2027")
plt.grid(True, alpha=0.25)
plt.legend()
plt.tight_layout()

plt.savefig(Path(__file__).with_name("oppgave_h_2022_2027.png"), dpi=300)
plt.show()