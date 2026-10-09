
# Oppgave e2 og e3
# Pensum "Praktisk introduksjon til numeriske metodar"
# s. 13: analytiske partiellderiverte og radientens lengde.
# s.15-16, Brattaste vegen ned.
# s.18-19, MKM med gradientmetodenAAAAAAAAAAAAAAAAAAAAAAAAA.

from pathlib import Path
import numpy as np

# kobler opp datasettet seperat
data = np.loadtxt(Path(__file__).with_name("Datasett.dat"))

x = data[:, 0]
y = data[:, 1]

# definerer modellen vår
def F(x, a, b, c, d, f):
    return a + b * x + c*np.sin(d*x + f)

# Summen av kvadrerte avvik, som vi skal minimere
def S(a, b, c, d, f):
    return np.sum((y - F(x, a, b, c, d, f))**2)

# Definerer funksjonen og kalkulerer avvikkene
def gradient (a, b, c, d, f):
    r = y - F(x, a, b, c, d, f)
    # kalkulerer avviket mellom observerte verdien
    # og verdien modellen beregner.
    v = d * x + f

#Partiell deriverte
    dSda = -2 * np.sum(r)
    dSdb = -2 * np.sum(r * x)
    dSdc = -2 * np.sum(r * np.sin(v))
    dSdd = -2 * np.sum(r * c * x * np.cos(v))
    dSdf = -2 * np.sum(r * c * np.cos(v))

    return dSda, dSdb, dSdc, dSdd, dSdf

# Valgte verdier fra oppgave e.1)
a = 407.09254
b = 2.87461
c = 2.0
d = 2 * np.pi
f = np.pi / 4

# Læringsraten tilsvarer gamma i boka og lambda i oppgaven
laeringsrate = 1e-4

# Stoppkriterier
endring_min = 1e-8
grad_min = 1e-4

maks_iterasjoner = 200_000

for n in range(1, maks_iterasjoner + 1):
    # e2: Beregner alle deriverte ved de samme parameterverdiene
    dSda, dSdb, dSdc, dSdd, dSdf = gradient(a, b, c, d, f)

    # Gradientens lengde, som i boka, men med fem komponenter
    grad_lengde = np.sqrt(
        dSda ** 2
        + dSdb ** 2
        + dSdc ** 2
        + dSdd ** 2
        + dSdf ** 2
    )

    # Gradientmetoden: Går i motsatt retning av gradienten
    a_ny = a - laeringsrate * dSda
    b_ny = b - laeringsrate * dSdb
    c_ny = c - laeringsrate * dSdc
    d_ny = d - laeringsrate * dSdd
    f_ny = f - laeringsrate * dSdf

    # e3: Finner den største absolutte parameterendringen
    endring = max(
        abs(a_ny - a),
        abs(b_ny - b),
        abs(c_ny - c),
        abs(d_ny - d),
        abs(f_ny - f),
    )

    # Tar i bruk de nye parameterverdiene
    a, b, c, d, f = a_ny, b_ny, c_ny, d_ny, f_ny

    # Stopper med en feilmelding hvis beregningen divergerer
    if not np.all(np.isfinite([a, b, c, d, f, grad_lengde])):
        raise RuntimeError(
            "Beregningen divergerer. Prøv lavere læringsrate."
        )

    # Skriver fremdriften til skjermen
    if n == 1 or n % 1000 == 0:
        print(
            f"Steg {n}: "
            f"a={a:.8f}, b={b:.8f}, c={c:.8f}, "
            f"d={d:.8f}, f={f:.8f}, "
            f"endring={endring:.2e}"
        )

    # Stopper når både endringene og gradienten er små nok
    if endring < endring_min and grad_lengde < grad_min:
        print(f"\nKonvergert etter {n} iterasjoner.")
        break

else:
    # Kjøres bare hvis løkken avsluttes uten break
    raise RuntimeError(
        "Maks antall iterasjoner nådd uten konvergens."
    )

# Skriver ut resultatene
print(f"Største parameterendring: {endring:.3e}")

print(
    f"Gradientlengde ved slutt: "
    f"{np.linalg.norm(gradient(a, b, c, d, f)):.3e}"
)

print(f"a = {a:.8f}")
print(f"b = {b:.8f}")
print(f"c = {c:.8f}")
print(f"d = {d:.8f}")
print(f"f = {f:.8f}")

