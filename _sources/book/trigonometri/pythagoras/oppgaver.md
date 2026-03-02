# Oppgaver

## Pytagoras' setning

:::::::::::::::{exercise} Oppgave 1 🚫
---
level: 1
---

**Hjelpemiddel:** Ikke tillatt.

Bestem $x$ i trekanten nedenfor.

:::{figure} ./figurer/underveisoppgaver/figur.svg
---
width: 60%
class: no-click, adaptive-figure
---
:::

:::{answer}
$$
x = 6
$$
:::

::::{solution}

Vi bruker Pytagoras' setning:

$$
a^2 + b^2 = c^2
$$

Der $c$ er hypotenusen. Fra figuren kan vi se at vi har en rettvinklet trekant med kjente sidelengder.

**Algebraisk manipulasjon:**

Setter inn de kjente verdiene i Pytagoras' setning:

$$
x^2 = 3^2 + 4^2
$$

Beregner kvadratene:

$$
x^2 = 9 + 16
$$

Adderer på høyre side:

$$
x^2 = 25
$$

Tar kvadratroten av begge sider:

$$
x = \sqrt{25} = 6
$$

Løsningen er:

$$
x = 6
$$

::::

:::::::::::::::

---

:::::::::::::::{exercise} Oppgave 2 🔑
---
level: 1
---

**Hjelpemiddel:** Tillatt.

Nedenfor vises en rettvinklet trekant.

:::{figure} ./figurer/oppgaver/oppgave_2/figur.svg
---
width: 70%
class: no-click, adaptive-figure
---
:::

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Bestem $x$.

:::{answer}
$$
x &\approx 8.7 \\
$$
:::

::::{solution}

Vi bruker Pytagoras' læresetning:
$a^2 + b^2 = c^2$.

Her er katetene $5$ og $x$, og hypotenusen er $10$. Da får vi:

$$
\begin{align*}
5^2 + x^2 &= 10^2 \\
25 + x^2 &= 100 \\
x^2 &= 100 - 25 \\
x^2 &= 75 \\
x &= \sqrt{75} \\
x &\approx 8.7 \\
\end{align*}
$$


::::

:::::::::::::

:::::::::::::{tab-item} b
Bruk CAS-vinduet til å bestemme $x$.
:::{cas-popup} 400 500
:::

:::{answer}
$$
x &\approx 8.7
$$
:::

::::{solution}
<!-- Løsning for b) is temporarily empty -->
::::

:::::::::::::

:::::::::::::::

---

:::::::::::::::{exercise} Oppgave 3 🔑
---
level: 1
---

**Hjelpemiddel:** Tillatt.

En stige på 5 meter lener seg inntil et tre. Bunnen av stigen er plassert 1,5 meter fra trestammen på flat mark. Vi antar at treet står vinkelrett på bakken.

Se figuren nedenfor.

:::{figure} ./figurer/oppgaver/oppgave_3/figur.svg
---
width: 60%
class: no-click, adaptive-figure
---
:::

::::::::::::::{tab-set}
---
class: tabs-parts
---
:::::::::::::{tab-item} a
Hvor høyt opp på treet når stigen? Bestem høyden $h$.

:::{answer}
$$
h \approx 4.8 \text{ m}.
$$
:::

::::{solution}
Siden treet står vinkelrett på bakken, danner stigen, bakken og treet en rettvinklet trekant.
* Hypotenusen er stigen: $c = 5$ m.
* Den ene kateten er avstanden langs bakken: $a = 1,5$ m.
* Den andre kateten er høyden opp på treet: $b = h$.

Vi bruker Pytagoras' læresetning ($a^2 + b^2 = c^2$) og setter inn tallene:

$$
\begin{aligned}
1,5^2 + h^2 &= 5^2 \\
2,25 + h^2 &= 25 \\
h^2 &= 25 - 2,25 \\
h^2 &= 22,75 \\
h &= \sqrt{22,75} \\
h &\approx 4.8
\end{aligned}
$$

Siden høyden må være positiv, forkaster vi den negative løsningen.
Stigen når ca. 4,77 meter opp på treet.
::::

:::::::::::::

:::::::::::::{tab-item} b
Hvor høyt opp på treet når stigen? Bruk CAS til å bestemme høyden $h$.
:::{cas-popup} 400 500
:::

:::{answer}
$$
h \approx 4.8 \text{ m}.
$$
:::

::::{solution}
<!-- Løsning for b) is temporarily empty -->
::::

:::::::::::::

:::::::::::::::

---

:::::::::::::::{exercise} Oppgave 4 🔑
---
level: 1
---

**Hjelpemiddel:** Tillatt.

En trekant har sidelengdene 7, 24 og 25.

Undersøk om trekanten er rettvinklet.

:::{answer}
Ja, trekanten er rettvinklet.
:::

::::{solution}
Vi bruker Pytagoras' setning baklengs for å sjekke om trekanten er rettvinklet.

Den lengste siden er $25$, så vi tester om

$$
7^2 + 24^2 = 25^2.
$$

Vi regner ut:

$$
7^2 + 24^2 = 49 + 576 = 625
$$

og

$$
25^2 = 625.
$$

Siden begge sider blir like, er trekanten rettvinklet.
::::

:::::::::::::::


