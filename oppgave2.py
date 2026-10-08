import numpy as np
import matplotlib.pyplot as plt

from oppgave1 import (x, y)

# Beregner gjennomsnittet av x- og y- verdiene
x_mean = np.mean(x)
y_mean = np.mean(y)

# Beregner stigningstallet og skjæringspunktet via MKM.
beta = float(
    np.sum((x - x_mean) * (y - y_mean))
    / np.sum((x - x_mean)**2)
)

alpha = float(y_mean - beta * x_mean)

# Beregner y-verdiene på regresjonslinjen.
# y = a + b * x
y_predicted = alpha + beta * x

# Skriver ut resultatene
print(f"alpha = {alpha:.5f}")
print(f"beta = {beta:.5f}")
print(f"Best passende regresjons linje: y = "
      f"{alpha:.5f} + {beta:.5f}x")

# Beregner datapunktene og regresjonslinjen.

plt.scatter(x, y, s=10, label="Datapunkter")
plt.plot(x, y_predicted, color="red",
         label=f"y = {alpha:.5f} + {beta:.5f}x")

# Navnsetter aksene og figuren.
plt.xlabel("x")
plt.ylabel("y")
plt.title("Oppgave 2")
plt.legend()
plt.grid(True, alpha=0.3)

# Tilpasser oppsettet, lagrer og viser figuren.
plt.tight_layout()
plt.savefig("regression_plot.png", dpi=300)
plt.show()
