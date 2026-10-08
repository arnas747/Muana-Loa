import numpy as np
import matplotlib.pyplot as plt

# Leser dataen fra settet.
data = np.loadtxt("Datasett.dat")

# Separerer dataen i sine kategorier.
x = data[:, 0]  ## Alle radene, første kolonne.
y = data[:, 1]  ## Alle radene, andre kolonne.

# Plotter enkeltpunkter, med vektorene x, y
# "s" beskriver størrelsen på de enkelte punktene.
plt.scatter(x, y, s=10)

# Navnsetting av aksene.
plt.xlabel("x")
plt.ylabel("y")
plt.title("Oppgave 1")
plt.grid(True, alpha=0.3) #legger til rutelinjer

# Formatterer dataplotten og lagrer den som png
plt.tight_layout() #formatter slik at vi unngår overlapp
plt.savefig("dataset_plot.pdf", dpi=300) #lagrer som pdf
plt.show() #Viser grafen uten at vi må åpne lagrede bildet.


