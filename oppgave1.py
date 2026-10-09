from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

# Leser dataen fra settet "Datasett.dat".
data = np.loadtxt(Path(__file__).with_name("Datasett.dat"))

# Separerer dataen i sine kategorier.
x = data[:, 0]  ## Alle radene, første kolonne.
y = data[:, 1]  ## Alle radene, andre kolonne.

# Kjører bare plottingen når oppgave1.py kjøres direkte.
if __name__ == "__main__":
    # Plotter datapunktene.
    plt.scatter(x, y, s=10)

    # Navnsetter aksene og figuren.
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Oppgave 1")
    plt.grid(True, alpha=0.3)

    # Tilpasser oppsettet, lagrer og viser figuren.
    plt.tight_layout()
    plt.savefig("dataset_plot.png", dpi=300)
    plt.show()


