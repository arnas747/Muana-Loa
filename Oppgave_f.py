from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

# Leser datasettet fra samme mappe som skriptet
data = np.loadtxt(Path(__file__).with_name("Datasett.dat"))
x = data[:, 0]
y = data[:, 1]

# Parameterverdiene fra gradientmetoden i oppgave e)
a = 406.91766300
b = 2.86960568
c = 2.78204851
d = 6.29604630
f = -0.60909629

# Regresjonskoeffisientene fra oppgave b)
alpha = 407.09215357
beta = 2.87481790

# Lager 1000 x-verdier for å tegne jevne kurver
x_plot = np.linspace(x.min(), x.max(), 1000)

# Beregningen av modellen og regresjonslinjen
y_model = a + b * x_plot + c * np.sin(d * x_plot + f)
y_line = alpha + beta * x_plot

# Plotter datapunktene, modellen og regresjonslinjen sammen
plt.figure(figsize=(9, 5.4))
plt.scatter(x, y, s=24, color="black", label="Datapunkter", zorder=3)
plt.plot(x_plot, y_model, color="tab:blue", label="Tilpasset modell F(x)")
plt.plot(
    x_plot,
    y_line,
    "--",
    color="tab:orange",
    label="Regresjonslinje fra b)",
)

# Legger til aksetekst, tittel, rutenett og tegnforklaring
plt.xlabel("x")
plt.ylabel("y")
plt.title("Oppgave f): Modell, datapunkter og regresjonslinje")
plt.grid(True, alpha=0.25)
plt.legend()
plt.tight_layout()

# Lagrer plottet som et bilde i samme mappe som skriptet
plt.savefig(Path(__file__).with_name("oppgave_f.png"), dpi=300)
plt.show()