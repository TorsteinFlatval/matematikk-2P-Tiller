# Variabler, tall og matematikk i Python

:::::{admonition} Læringsmål
---
class: tip
---
* Kunne lage og bruke variabler i Python
* Kunne regne med tall i Python
* Kunne bruke resultatene i enkle programmer
:::::

Før vi jobber videre med `print`{l=python}, `if`{l=python}, `for`{l=python} og `while`{l=python}, trenger vi et godt grunnlag i variabler og regning i Python.

:::::::::::::::{summary} Variabler
En variabel er et navn som peker på en verdi.

:::{code-block} python
x = 5
navn = "Ada"
:::

`=` i Python betyr **tilordning**: verdien på høyre side lagres i variabelen på venstre side.
:::::::::::::::

:::::::::::::::{example} Eksempel 1: Lage variabler
:::{code-block} python
---
linenos:
---
a = 3
b = 4
sum = a + b
print(sum)
:::

Utskrift:
```text
7
```
:::::::::::::::

:::::::::::::::{exercise} Underveisoppgave 1
Skriv kode som beregner summen av tallene `8` og `12`, og skriv ut svaret.

:::{interactive-code}
# Skriv programmet ditt her



:::

:::::{solution}
:::{code-block} python
---
linenos:
---
sum = 8 + 12
print(sum)
:::
:::::
:::::::::::::::

## Talltyper

De vanligste talltypene i Python er:

- `int`{l=python}: heltall, for eksempel `5`{l=python}, `-2`{l=python}
- `float`{l=python}: desimaltall, for eksempel `3.5`{l=python}, `-0.25`{l=python}

:::::::::::::::{example} Eksempel 2: Heltall og desimaltall
:::{code-block} python
---
linenos:
---
x = 5
y = 2
print(x + y)
print(x - y)
print(x * y)
print(x / y)
:::

Utskrift:
```text
7
3
10
2.5
```

Nå viser vi flere operasjoner med samme variabler. `/` gir vanlig divisjon (desimaltall), mens `+`, `-` og `*` gir heltall.
:::::::::::::::

:::::::::::::::{exercise} Underveisoppgave 2
La `a = 10` og `b = 3`.

Skriv ut:
- `a + b`
- `a - b`
- `a * b`
- `a / b`

:::{interactive-code}
# Skriv programmet ditt her



:::

:::::{solution}
:::{code-block} python
---
linenos:
---
a = 10
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b)
:::
:::::
:::::::::::::::

## Regneoperatorer

:::::::::::::::{summary} Vanlige operatorer
| Operator | Betydning | Eksempel | Vanlig notasjon |
|----------|-----------|----------|-------|
| `+`{l=python} | addisjon | `3 + 2` | $3 + 2$ |
| `-`{l=python} | subtraksjon | `7 - 4` | $7 - 4$ |
| `*`{l=python} | multiplikasjon | `3 * 5` | $3 \cdot 5$ |
| `/`{l=python} | divisjon | `7 / 2` | $\frac{7}{2}$ |
| `**`{l=python} | potens | `2 ** 3` | $2^3$ |
:::::::::::::::

:::::::::::::::{example} Eksempel 3: Regneuttrykk
:::{code-block} python
---
linenos:
---
x = 2
y = 5
print(x + y)
print(y - x)
print(x * y)
print(y ** x)
:::

Utskrift:
```text
7
3
10
25
```
:::::::::::::::

:::::::::::::::{exercise} Underveisoppgave 3
Skriv kode som regner ut arealet av et rektangel med lengde `7` og bredde `4`.

:::{interactive-code}
# Skriv programmet ditt her



:::

:::::{solution}
:::{code-block} python
---
linenos:
---
lengde = 7
bredde = 4
areal = lengde * bredde
print(areal)
:::
:::::
:::::::::::::::

:::{margin}
Tips: Bruk tydelige variabelnavn. Det gjør koden lettere å lese senere.
:::
