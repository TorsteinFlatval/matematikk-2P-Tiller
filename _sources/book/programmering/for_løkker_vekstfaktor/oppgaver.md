# Oppgaver: Løkker og vekstfaktor

## Grunnleggende vekstfaktor

:::::{exercise} Oppgave 1
Du har 2000 kr som spares med 5% årlig rente.

Skriv et program som bruker formelen `ny_verdi = gammel_verdi * vekstfaktor ** t`{l=python} til å finne beløpet etter 4 år.

:::{interactive-code}
gammel_verdi = 
vekstfaktor = 
t = 

:::

::::{answer}
Utskrift:

```text
2431.0125
```
::::

::::{solution}
:::{code-block} python
---
linenos:
---
gammel_verdi = 2000
vekstfaktor = 1.05
t = 4
ny_verdi = gammel_verdi * vekstfaktor ** t
print(ny_verdi)
:::
:::::
:::::::::::::::

:::::{exercise} Oppgave 2
En laptop koster 10 000 kr og mister 15% av verdien hvert år.

Hvor mye er den verdt etter 3 år? Bruk formelen for vekst.

:::{interactive-code}
verdi = 
vekstfaktor = 
t = 

:::

::::{answer}
Utskrift:

```text
6141.25
```
::::

::::{solution}
:::{code-block} python
---
linenos:
---
verdi = 10000
vekstfaktor = 0.85  # 15% nedgang
t = 3
ny_verdi = verdi * vekstfaktor ** t
print(ny_verdi)
:::
:::::
:::::::::::::::

## Vekst og nedgang over tid med for-løkker

:::::{exercise} Oppgave 3
En nettbank-konto starter med 5000 kr og vokser med 2% per år.

Skriv et program som viser beløpet for hvert år i 6 år.

:::{interactive-code}
beløp = 
vekstfaktor = 

for år in range(1, 7):
    # Skriv resten av løkken her
:::

::::{answer}
Utskrift:

```text
År 1 : 5100.0
År 2 : 5202.0
År 3 : 5306.04
År 4 : 5412.1608
År 5 : 5520.4040159999995
År 6 : 5630.81209632
```
::::

::::{solution}
:::{code-block} python
---
linenos:
---
beløp = 5000
vekstfaktor = 1.02

for år in range(1, 7):
    beløp = beløp * vekstfaktor
    print("År", år, ":", beløp)
:::
::::
::::::::::::::::

:::::{exercise} Oppgave 4
En bil er verdt 200 000 kr og mister 10% av verdien hvert år.

Skriv et program som viser verdien hver år i 5 år.

:::{interactive-code}
verdi = 
vekstfaktor = 

for år in range(1, 6):
    # Skriv resten av løkken her
:::

::::{answer}
Utskrift:

```text
År 1 : 180000.0
År 2 : 162000.0
År 3 : 145800.0
År 4 : 131220.0
År 5 : 118098.0
```
::::

::::{solution}
:::{code-block} python
---
linenos:
---
verdi = 200000
vekstfaktor = 0.90

for år in range(1, 6):
    verdi = verdi * vekstfaktor
    print("År", år, ":", verdi)
:::
::::
::::::::::::::::

## While-løkker: Finne når et mål er nådd

:::::{exercise} Oppgave 5
En YouTube-kanal har 100 abonnenter og vokser med 20% per måned.

Skriv et program som finner hvor mange måneder det tar før kanalen har minst 10 000 abonnenter.

:::{interactive-code}
abonnenter = 
vekstfaktor = 
måneder = 

while abonnenter < 10000:
    # Skriv resten av løkken her
:::

::::{answer}
Utskrift:

```text
Antall måneder: 26
Antall abonnenter: 11447.545997288275
```
::::

::::{solution}
:::{code-block} python
---
linenos:
---
abonnenter = 100
vekstfaktor = 1.20
måneder = 0

while abonnenter < 10000:
    abonnenter = abonnenter * vekstfaktor
    måneder = måneder + 1

print("Antall måneder:", måneder)
print("Antall abonnenter:", abonnenter)
:::
::::
::::::::::::::::

:::::{exercise} Oppgave 6
Et radioaktivt stoff er 1000 gram og halverer seg hver dag.

Hvor mange dager tar det før det er mindre enn 10 gram igjen?

:::{interactive-code}
gram = 
vekstfaktor = 
dager = 

while gram > 10:
    # Skriv resten av løkken her
:::

::::{answer}
Utskrift:

```text
Antall dager: 7
Resterende gram: 7.8125
```
::::

::::{solution}
:::{code-block} python
---
linenos:
---
gram = 1000
vekstfaktor = 0.50
dager = 0

while gram > 10:
    gram = gram * vekstfaktor
    dager = dager + 1

print("Antall dager:", dager)
print("Resterende gram:", gram)
:::
::::
::::::::::::::::

---

## Mer utfordrende oppgaver

:::::{exercise} Oppgave 7
Du har 0 kr på konto og setter inn 500 kr hver måned. Pengene vokser med 1% rente hver måned.

Skriv et program som finner hvor mange måneder det tar før du har minst 6000 kr. Skriv ut både antall måneder og sluttbeløpet.

:::{interactive-code}
# Skriv programmet ditt her




:::

::::{answer}
Utskrift:

```text
Antall måneder: 12
Sluttbeløp: 6404.66402166447
```
::::

::::{solution}
:::{code-block} python
---
linenos:
---
beløp = 0
vekstfaktor = 1.01
innskudd = 500
måneder = 0

while beløp < 6000:
    beløp += innskudd
    beløp = beløp * vekstfaktor
    måneder += 1

print("Antall måneder:", måneder)
print("Sluttbeløp:", beløp)
:::
::::
::::::::::::::::

:::::{exercise} Oppgave 8
En by har 50 000 innbyggere. Hver år mister den 1.5% av befolkningen, og samtidig emigrerer 500 mennesker til.

Skriv et program som sjekker: Hvor mange år tar det før befolkningen blir mindre enn 45 000?

:::{interactive-code}
# Skriv programmet ditt her




:::

::::{answer}
Utskrift:

```text
Antall år: 5
Befolkning: 43934.70853046875
```
::::

::::{solution}
:::{code-block} python
---
linenos:
---
befolkning = 50000
vekstfaktor = 0.985  # 1.5% nedgang
emigrasjon = 500
år = 0

while befolkning > 45000:
    befolkning = befolkning * vekstfaktor
    befolkning -= emigrasjon
    år += 1

print("Antall år:", år)
print("Befolkning:", befolkning)
:::
::::
::::::::::::::::

:::::{exercise} Oppgave 9
En bedrift produserer biler. Første år produserer de 1000 biler. Hver år øker produksjonen med 8%, men kostnaden per bil synker med 2%.

Hvis utgangskostnaden per bil er 200 000 kr, hva blir den totale produksjonskostnaden hvert år i 5 år? (Bruk både vekst og nedgang!)

:::{interactive-code}
# Skriv programmet ditt her




:::

::::{answer}
Utskrift:

```text
År 1 - Biler: 1080.0 - Total kostnad: 211680000.0
År 2 - Biler: 1166.4 - Total kostnad: 224042112.00000003
År 3 - Biler: 1259.7120000000002 - Total kostnad: 237126171.34080005
År 4 - Biler: 1360.4889600000004 - Total kostnad: 250974339.74710277
År 5 - Biler: 1469.3280768000004 - Total kostnad: 265631241.18833357
```
::::

::::{solution}
:::{code-block} python
---
linenos:
---
biler = 1000
vekst_biler = 1.08
kostnad_per_bil = 200000
synking_kostnad = 0.98

for år in range(1, 6):
    biler = biler * vekst_biler
    kostnad_per_bil = kostnad_per_bil * synking_kostnad
    total_kostnad = biler * kostnad_per_bil
    print("År", år, "- Biler:", biler, "- Total kostnad:", total_kostnad)
:::
::::
::::::::::::::::
