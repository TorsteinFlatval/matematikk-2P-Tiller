# Løkker og vekstfaktor

:::::{admonition} Læringsmål
---
class: tip
---
* Forstå hva vekstfaktor betyr (både økning og nedgang)
* Kunne bruke formelen for vekst med vekstfaktor
* Kunne bruke `for`{l=python}- og `while`{l=python}-løkker til å simulere vekst og nedgang
* Forstå når man bruker `+=` operatoren
:::::

## Hva er vekstfaktor?

En **vekstfaktor** brukes for å beskrive prosentvis endring - både økning og nedgang.

- Hvis noe øker med 5%, multipliserer vi med vekstfaktoren **1.05**
- Hvis noe minker med 10%, multipliserer vi med vekstfaktoren **0.90**

:::::::::::::::{summary} Vekstfaktor
$$\text{vekstfaktor} = 1 + \frac{\text{prosentvis endring}}{100}$$

**Eksempler:**
- 3% økning → vekstfaktor = 1.03
- 10% nedgang → vekstfaktor = 0.90
- 20% nedgang → vekstfaktor = 0.80
:::::::::::::::

## Formelen for vekst

Når vi vet hvor mange perioder noe skal vokse eller minke:

:::::::::::::::{summary} Vekstformel
$$\text{ny verdi} = \text{gammel verdi} \cdot \text{vekstfaktor}^t$$

der $t$ er antall perioder (år, måneder, timer osv.).
:::::::::::::::

:::::::::::::::{example} Eksempel 1: Bruk av vekstformelen
Du har 1000 kr som vokser med 5% per år. Hvor mye har du etter 3 år?

:::{code-block} python
---
linenos:
---
gammel_verdi = 1000
vekstfaktor = 1.05
t = 3
ny_verdi = gammel_verdi * vekstfaktor ** t
print(ny_verdi)
:::

Utskrift:
```text
1157.625
```
:::::::::::::::

:::::::::::::::{exercise} Underveisoppgave 1
Du har 2000 kr som vokser med 3% per år. Bruk vekstformelen til å finne hvor mye du har etter 2 år.

:::{interactive-code}
gammel_verdi = 2000
vekstfaktor = 1.03
t = 2
ny_verdi = # ... fyll inn resten




:::

:::::{solution}
:::{code-block} python
---
linenos:
---
gammel_verdi = 2000
vekstfaktor = 1.03
t = 2
ny_verdi = gammel_verdi * vekstfaktor ** t
print(ny_verdi)
:::
:::::
:::::::::::::::

:::::::::::::::{example} Eksempel 2: Nedgang
En bil er verdt 200 000 kr og mister 15% av verdien per år. Hvor mye er den verdt etter 3 år?

:::{code-block} python
---
linenos:
---
verdi = 200000
vekstfaktor = 0.85  # 15% nedgang
t = 3
ny_verdi = verdi * vekstfaktor ** t
print(round(ny_verdi, 2))
:::

Utskrift:
```text
122462.5
```
::::::::::::::::



## Vekst over tid med `for`{l=python}-løkker

Vekstformelen forteller oss hvor vi ender opp etter en bestemt tid, men ofte vil vi se **hvordan veksten skjer steg for steg**. Da bruker vi løkker.

:::::::::::::::{example} Eksempel 3: Se vekst år for år
:::{code-block} python
---
linenos:
---
beløp = 1000
vekstfaktor = 1.05

for år in range(1, 6):
    beløp = beløp * vekstfaktor
    print("År", år, ":", beløp)
:::

Utskrift:
```text
År 1 : 1050.0
År 2 : 1102.5
År 3 : 1157.625
År 4 : 1215.51
År 5 : 1276.28
```

**Hva skjer?**
- Vi starter med 1000 kr: `beløp = 1000`{l=python}
- Vekstfaktoren er 1.05: `vekstfaktor = 1.05`{l=python}
- Hver gang løkken kjører, multipliserer vi `beløp = beløp * vekstfaktor`{l=python}
- Vi gjentar dette 5 ganger med `for år in range(1, 6)`{l=python}
- Vi skriver ut `beløp`{l=python} etter hver iterasjon
:::::::::::::::

:::::::::::::::{exercise} Underveisoppgave 2
En bakteriekultur starter med 100 bakterier og vokser med 2% hver time. Skriv et program som viser hvor mange bakterier det er etter hver time i 5 timer.

:::{interactive-code}
bakterier = 100
vekstfaktor = 1.02

for time in range(...):
    # ... fyll inn resten




:::

:::::{solution}
:::{code-block} python
---
linenos:
---
bakterier = 100
vekstfaktor = 1.02

for time in range(1, 6):
    bakterier = bakterier * vekstfaktor
    print("Time", time, ":", round(bakterier, 2))
:::
:::::
:::::::::::::::



## Finne når et mål er nådd med `while`{l=python}-løkker

Noen ganger vet vi ikke på forhånd hvor lang tid noe tar. En **`while`{l=python}-løkke** kjører helt til en betingelse er oppfylt.

:::::::::::::::{example} Eksempel 3b: Enkel while-løkke
Et enkelt eksempel på en `while`{l=python}-løkke er å spare penger:

:::{code-block} python
---
linenos:
---
penger = 0
while penger < 500:
    penger = penger + 100
    print("Har spart:", penger, "kr")
print("Målet på 500 kr er nådd!")
:::

Utskrift:
```text
Har spart: 100 kr
Har spart: 200 kr
Har spart: 300 kr
Har spart: 400 kr
Har spart: 500 kr
Målet på 500 kr er nådd!
```
:::::::::::::::

:::::::::::::::{exercise} Underveisoppgave 2b
Du har sparepenger på 0 kr. Hver dag legger du til 150 kr. Skriv et program som viser hvor mange dager det tar før du har minst 1000 kr.

:::{interactive-code}
penger = 0
dager = 

# ... skriv resten av koden din her




:::

:::::{solution}
:::{code-block} python
---
linenos:
---
penger = 0
dager = 0

while penger < 1000:
    penger = penger + 150
    dager = dager + 1

print("Antall dager:", dager)
print("Sparepenger:", penger, "kr")
:::
:::::
:::::::::::::::

:::::::::::::::{example} Eksempel 4: Når nås målet?
Hvor mange år tar det før 1000 kr vokser til 2000 kr med 5% årlig rente?

:::{code-block} python
---
linenos:
---
beløp = 1000
vekstfaktor = 1.05
år = 0

while beløp < 2000:
    beløp = beløp * vekstfaktor
    år = år + 1

print("Antall år:", år)
print("Sluttbeløp:", round(beløp, 2))
:::

Utskrift:
```text
Antall år: 15
Sluttbeløp: 2078.93
```

**Hva skjer?**
- Vi starter med 1000 kr: `beløp = 1000`{l=python}
- Vekstfaktoren er 1.05: `vekstfaktor = 1.05`{l=python}
- Vi teller år med `år = 0`{l=python}
- Løkken kjøres så lenge `beløp < 2000`{l=python}
- I hver iterasjon gjør vi `beløp = beløp * vekstfaktor`{l=python} og `år = år + 1`{l=python}
- Når beløpet blir over 2000, stopper løkken
:::::::::::::::

:::::::::::::::{exercise} Underveisoppgave 3
Hvor mange dager tar det før 500 kr vokser til 1000 kr hvis det vokser med 5% hver dag?

:::{interactive-code}
beløp = 500
vekstfaktor = 
dager = 

# ... skriv resten av koden din her




:::

:::::{solution}
:::{code-block} python
---
linenos:
---
beløp = 500
vekstfaktor = 1.05
dager = 0

while beløp < 1000:
    beløp = beløp * vekstfaktor
    dager = dager + 1

print("Antall dager:", dager)
print("Sluttbeløp:", round(beløp, 2))
:::
:::::
:::::::::::::::



## Forkortet skriving med `+=` operator

Når vi skal legge til eller multiplisere i en variabel, kan vi bruke forkortede operatorer. Dette gjør koden lettere å lese.

:::::::::::::::{summary} Forkortede operatorer
- `variabel += verdi` er det samme som `variabel = variabel + verdi`
- `variabel -= verdi` er det samme som `variabel = variabel - verdi`
- `variabel *= verdi` er det samme som `variabel = variabel * verdi`
:::::::::::::::

**Eksempel på `+=`:**

```python
penger = 100
penger += 50  # Det samme som: penger = penger + 50
print(penger)  # Utskrift: 150
```

:::::::::::::::{example} Eksempel 5: Sparing med innskudd og rente
Du setter inn 1000 kr hver måned, og pengene vokser med 1% per måned.

:::{code-block} python
---
linenos:
---
beløp = 0
vekstfaktor = 1.01
innskudd = 1000

for måned in range(1, 7):
    beløp += innskudd  # Legger til innskudd
    beløp = beløp * vekstfaktor  # Legger til rente
    print("Måned", måned, ":", round(beløp, 2))
:::

Utskrift:
```text
Måned 1 : 1010.0
Måned 2 : 2030.1
Måned 3 : 3060.4
Måned 4 : 4101.01
Måned 5 : 5152.02
Måned 6 : 6213.54
```

**Hva skjer?**
- Vi starter med 0 kr: `beløp = 0`{l=python}
- Hver iterasjon legger vi til med `beløp += innskudd`{l=python} (1000 kr)
- Deretter ganges hele beløpet med 1.01: `beløp = beløp * vekstfaktor`{l=python}
- Dette simulerer at vi legger inn penger og får rente på alt vi har spart
- Vi gjentar for 6 måneder: `for måned in range(1, 7)`{l=python}
:::::::::::::::

:::::::::::::::{exercise} Underveisoppgave 4
Du lagrer 100 kr hver dag i en sparegris. Hver dag forsvinner 2% av pengene (fordi de glir ut gjennom en liten åpning - oops!). Skriv et program som viser hvor mye du har etter hver dag i 7 dager.

:::{interactive-code}
penger = 0

# ... skriv resten av koden din her




:::

:::::{solution}
:::{code-block} python
---
linenos:
---
penger = 0

for dag in range(1, 8):
    penger += 100  # Legger til 100 kr
    penger *= 0.98  # Mister 2% hver dag
    print("Dag", dag, ":", round(penger, 2))
:::
:::::
:::::::::::::::



## Samlet oppgave

Noen ganger må du kombinere flere konsepter. Her er et eksempel hvor vi bruker både `for`{l=python}-løkke, `+=` og vekstfaktor:

:::::::::::::::{exercise} Underveisoppgave 5
En befolkning på 50 000 personer vokser med 2% per år, men 300 personer emigrerer hvert år. Skriv et program som viser befolkningsstørrelsen hver år i 10 år.

:::{interactive-code}
befolkning = 50000
vekstfaktor = 1.02
emigrasjon = 300

# ... skriv resten av koden din her




:::

:::::{solution}
:::{code-block} python
---
linenos:
---
befolkning = 50000
vekstfaktor = 1.02
emigrasjon = 300

for år in range(1, 11):
    befolkning = befolkning * vekstfaktor
    befolkning -= emigrasjon
    print("År", år, ":", round(befolkning))
:::
:::::
:::::::::::::::

---

Gå til [Oppgaver](oppgaver.md) for å øve med flere eksempler!
