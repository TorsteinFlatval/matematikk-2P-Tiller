# Oppgaver: Løkker og vekstfaktor

## Grunnleggende vekstfaktor

:::::{exercise} Oppgave 1
Du har 2000 kr som spares med 5% årlig rente.

Skriv et program som bruker formelen `ny_verdi = gammel_verdi * vekstfaktor^t` til å finne beløpet etter 4 år.

:::{interactive-code}
# Skriv programmet ditt her




:::

:::::{answer}
Utskrift:

```text
2431.01
```
:::::

:::::{solution}
:::{code-block} python
---
linenos:
---
gammel_verdi = 2000
vekstfaktor = 1.05
t = 4
ny_verdi = gammel_verdi * vekstfaktor ** t
print(round(ny_verdi, 2))
:::
:::::
:::::::::::::::

:::::{exercise} Oppgave 2
En laptop koster 10 000 kr og mister 15% av verdien hvert år.

Hvor mye er den verdt etter 3 år? Bruk formelen for vekst.

:::{interactive-code}
# Skriv programmet ditt her




:::

:::::{answer}
Utskrift:

```text
6141.04
```
:::::

:::::{solution}
:::{code-block} python
---
linenos:
---
verdi = 10000
vekstfaktor = 0.85  # 15% nedgang
t = 3
ny_verdi = verdi * vekstfaktor ** t
print(round(ny_verdi, 2))
:::
:::::
:::::::::::::::

## Vekst og nedgang over tid med for-løkker

:::::{exercise} Oppgave 3
En nettbank-konto starter med 5000 kr og vokser med 2% per år.

Skriv et program som viser beløpet for hvert år i 6 år.

:::{interactive-code}
# Skriv programmet ditt her




:::

:::::{answer}
Utskrift:

```text
År 1 : 5100.0
År 2 : 5202.0
År 3 : 5306.04
År 4 : 5412.16
År 5 : 5520.41
År 6 : 5631.02
```
:::::

:::::{solution}
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
:::::
:::::::::::::::

:::::{exercise} Oppgave 4
En bil er verdt 200 000 kr og mister 10% av verdien hvert år.

Skriv et program som viser verdien hver år i 5 år.

:::{interactive-code}
# Skriv programmet ditt her




:::

:::::{answer}
Utskrift:

```text
År 1 : 180000.0
År 2 : 162000.0
År 3 : 145800.0
År 4 : 131220.0
År 5 : 118098.0
```
:::::

:::::{solution}
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
:::::
:::::::::::::::

:::::{exercise} Oppgave 5
En YouTube-kanal har 100 abonnenter og vokser med 20% per måned.

Skriv et program som finner hvor mange måneder det tar før kanalen har minst 10 000 abonnenter.

:::{interactive-code}
# Skriv programmet ditt her




:::

:::::{answer}
Utskrift:

```text
Antall måneder: 19
Antall abonnenter: 10239
```
:::::

:::::{solution}
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
print("Antall abonnenter:", round(abonnenter))
:::
:::::
:::::::::::::::

:::::{exercise} Oppgave 6
En radioaktiv stoff har 1000 gram og halvert seg hver gang (50% nedgang per periode).

Hvor mange perioder tar det før det er mindre enn 10 gram igjen?

:::{interactive-code}
# Skriv programmet ditt her




:::

:::::{answer}
Utskrift:

```text
Antall perioder: 7
Resterende gram: 7.81
```
:::::

:::::{solution}
:::{code-block} python
---
linenos:
---
gram = 1000
vekstfaktor = 0.50
perioder = 0

while gram > 10:
    gram = gram * vekstfaktor
    perioder = perioder + 1

print("Antall perioder:", perioder)
print("Resterende gram:", round(gram, 2))
:::
:::::
:::::::::::::::

---

## Mer utfordrende oppgaver

:::::{exercise} Oppgave 7
Du har 0 kr på konto og setter inn 500 kr hver måned. Pengene vokser med 1% rente hver måned.

Skriv et program som finner hvor mange måneder det tar før du har minst 6000 kr. Skriv ut både antall måneder og sluttbeløpet.

:::{interactive-code}
# Skriv programmet ditt her




:::

:::::{solution}
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
print("Sluttbeløp:", round(beløp, 2))
:::
:::::
:::::::::::::::

:::::{exercise} Oppgave 8
En by har 50 000 innbyggere. Hver år øker befolkningen med 1.5%, men samtidig emigrerer 500 mennesker.

Skriv et program som sjekker: Hvor mange år tar det før befolkningen blir mindre enn 45 000?

:::{interactive-code}
# Skriv programmet ditt her




:::

:::::{solution}
:::{code-block} python
---
linenos:
---
befolkning = 50000
vekstfaktor = 1.015
emigrasjon = 500
år = 0

while befolkning > 45000:
    befolkning = befolkning * vekstfaktor
    befolkning -= emigrasjon
    år += 1

print("Antall år:", år)
print("Befolkning:", round(befolkning))
:::
:::::
:::::::::::::::

:::::{exercise} Oppgave 9
En bedrift produserer biler. Første år produserer de 1000 biler. Hver år øker produksjonen med 8%, men kostnaden per bil synker med 2%.

Hvis utgangskostnaden per bil er 200 000 kr, hva blir den totale produksjonskostnaden hvert år i 5 år? (Bruk både vekst og nedgang!)

:::{interactive-code}
# Skriv programmet ditt her




:::

:::::{solution}
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
    print("År", år, "- Biler:", round(biler), "- Total kostnad:", round(total_kostnad))
:::
:::::
:::::::::::::::

:::::{exercise} Oppgave 10
En bakteriekultur starter med 100 bakterier. Den vokser med 25% hver time det første døgnet (24 timer). 

Skriv et program som:
- Viser antallet bakterier hver 6. time (time 0, 6, 12, 18, 24)
- Finner total økning i prosent fra start til slutt

:::{interactive-code}
# Skriv programmet ditt her
# Hint: Bruk en løkke og en teller




:::

:::::{solution}
:::{code-block} python
---
linenos:
---
bakterier_start = 100
bakterier = 100
vekstfaktor = 1.25
teller = 0

for time in range(1, 25):
    bakterier = bakterier * vekstfaktor
    teller += 1
    
    if teller == 6:
        print("Time", time, ":", round(bakterier))
        teller = 0

# Siste måling (time 24)
print("Time 24:", round(bakterier))

# Prosent økning
prosent_okning = ((bakterier - bakterier_start) / bakterier_start) * 100
print("Total økning: {:.1f}%".format(prosent_okning))
:::
:::::
:::::::::::::::

:::::{exercise} Oppgave 11
To investeringer:
- **Investering A:** 10 000 kr med 4% årlig rente
- **Investering B:** 10 000 kr med 3% årlig rente de 5 første årene, så 5% fra år 6

Skriv et program som sammenligner de to investeringene og finner når investering B blir større enn investering A.

:::{interactive-code}
# Skriv programmet ditt her




:::

:::::{solution}
:::{code-block} python
---
linenos:
---
inv_a = 10000
inv_b = 10000
år = 0

while inv_a >= inv_b:
    år += 1
    inv_a = inv_a * 1.04
    
    if år <= 5:
        inv_b = inv_b * 1.03
    else:
        inv_b = inv_b * 1.05

print("År:", år)
print("Investering A:", round(inv_a, 2))
print("Investering B:", round(inv_b, 2))
:::
:::::
:::::::::::::::

:::::{exercise} Oppgave 12
En app har 500 brukere. Hver dag slutter 2% av brukerne og 100 nye brukere registrerer seg.

Skriv et program som simulerer 30 dager og finner:
- Antall brukere etter 30 dager
- Hvilken dag brukerne var på sitt laveste/høyeste
- Om appen har vekst eller nedgang totalt

:::{interactive-code}
# Skriv programmet ditt her
# Denne må du tenke litt på selv!




:::

:::::{solution}
:::{code-block} python
---
linenos:
---
brukere = 500
brukere_min = 500
brukere_maks = 500
dag_min = 0
dag_maks = 0

for dag in range(1, 31):
    brukere = brukere * 0.98  # Mister 2%
    brukere += 100  # Legger til 100 nye
    
    if brukere < brukere_min:
        brukere_min = brukere
        dag_min = dag
    
    if brukere > brukere_maks:
        brukere_maks = brukere
        dag_maks = dag

print("Brukere etter 30 dager:", round(brukere))
print("Laveste:", round(brukere_min), "- dag", dag_min)
print("Høyeste:", round(brukere_maks), "- dag", dag_maks)

if brukere > 500:
    print("Appen har vekst!")
else:
    print("Appen har nedgang!")
:::
:::::
:::::::::::::::
