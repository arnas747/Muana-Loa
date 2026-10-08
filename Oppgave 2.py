import numpy as np

#Importerer datablokken
data = np.loadtxt("Datasett.dat")

#Kategoriserer datablokken inn i vektorene
x = data[:, 0]
y = data[:, 1]

# Beregner gjennomsnittet av x- og y- verdiene
x_mean = np.mean(x)
y_mean = np.mean(y)

# Beregner stigningstallet og skjæringspunktet via MKM.
beta = np.sum((x - x_mean) * (y - y_mean)) / np.sum((x - x_mean)**2)
alpha = y_mean - beta * x_mean

print(f"alpha = {alpha:.5f}")
print(f"beta = {beta:.5f}")
print(f"Best passende regresjons linje: y = {alpha:.5f} + {beta:.5f}x")