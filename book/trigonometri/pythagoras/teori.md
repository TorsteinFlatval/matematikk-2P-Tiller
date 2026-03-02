# Pytagoras' setning

En **rettvinklet** trekant er en trekant der én av vinklene er $90 \degree$.
Pytagoras' setning er en setning som forteller oss hvordan sidene i en rettvinklet trekant henger sammen. 

:::::::::::::::{admonition} Pytagoras' setning
---
class: summary
---
For en rettvinklet trekant gjelder

$$
(\mathrm{hypotenus})^2 = (\mathrm{katet}_1)^2 + (\mathrm{katet}_2)^2
$$

Se figuren til venstre nedenfor. Merk det lille kvadratet ved hjørne $C$ - dette indikerer at vinkelen der er $90\degree$.

:::{figure} ./figurer/teori/merged_figure.svg
---
width: 100%
class: no-click, adaptive-figure
---
:::

Typisk navnsettes sidene i en rettvinklet trekant slik at den motstående siden til hjørne $A$ kalles for $a$, den motstående siden til hjørne $B$ kalles for $b$ og den motstående siden til $C$ kalles for $c$. Se figuren til høyre ovenfor. 

Da kan vi skrive ned Pytagoras' setning ved

$$
a^2 + b^2 = c^2
$$

Likevell er ikke alltid dette tilfellet, så hypotenusen kan være en annen side av trekanten.
:::::::::::::::

---

:::::::::::::::{example} Eksempel 1

Nedenfor vises en rettvinklet trekant der den ene kateten har lengde 4 og den andre kateten er 3.

:::{plot}
width: 45%
class: no-click, adaptive-figure
axis: off, equal
xmin: -0.8
xmax: 3.8
ymin: -0.8
ymax: 4.8
figsize: (5, 6)
fontsize: 24
fill-polygon: (0, 0), (3, 0), (0, 4), 0072b2, 0.1
line-segment: (0, 0), (3, 0), solid, black, 2
line-segment: (3, 0), (0, 4), solid, black, 2
line-segment: (0, 4), (0, 0), solid, black, 2
vline: 0.3, 0, 0.3, solid, black, 2
hline: 0.3, 0, 0.3, solid, black, 2
text: -0.4, -0.15, "$A$", center
text: 3.15, -0.15, "$B$", center
text: -0.2, 4.5, "$C$", center
text: 1.3, -0.25, "$3$", center
text: -0.4, 2, "$4$", center
text: 1.6, 2.2, "$x$", center
:::

Bestem hypotenusen $x$.

:::{margin}
**NB!** Likningen $x^2 = 25$ har to løsninger: $x = 5$ og $x = -5$.

Her er $x$ en lengde, så vi velger bare den positive løsningen: $x = 5$.
:::

::::{admonition} Løsning
---
class: solution
---

Vi bruker Pytagoras' læresetning $a^2 + b^2 = c^2$ der $a$ og $b$ er katetene og $c$ er hypotenusen.
Her er den ene kateten $a = 3$ og den andre kateten $b = 4$. Den ukjente siden $x$ er:

$$
\begin{aligned}
3^2 + 4^2 &= x^2 \\
9 + 16 &= x^2 \\
25 &= x^2 \\
x &= \sqrt{25} \\
x &=  5
\end{aligned}
$$

::::

:::::::::::::::

---

:::::::::::::::{example} Eksempel 2

Nedenfor vises en rettvinklet trekant der hypotenusen har lengde 10 og den ene kateten har lengde 8.

:::{plot}
width: 45%
class: no-click, adaptive-figure
axis: off, equal
xmin: -0.8
xmax: 8.8
ymin: -0.8
ymax: 6.8
figsize: (5, 4)
fontsize: 24
fill-polygon: (0, 0), (8, 0), (0, 6), 0072b2, 0.1
line-segment: (0, 0), (8, 0), solid, black, 2
line-segment: (8, 0), (0, 6), solid, black, 2
line-segment: (0, 6), (0, 0), solid, black, 2
vline: 0.5, 0, 0.5, solid, black, 2
hline: 0.5, 0, 0.5, solid, black, 2
text: -0.4, -0.2, "$A$", center
text: 8.2, -0.2, "$B$", center
text: -0.6, 7.0, "$C$", center
text: 4, -0.3, "$8$", center
text: -0.7, 3, "$x$", center
text: 4.3, 3.6, "$10$", center
:::

Bestem den ukjente kateten $x$.

:::{margin}
Det forventes at dere kjenner til kvadrattallene opp til 100, slik at dere kan finne kvadratrøttene raskt.

$1^2 = 1$ $\qquad$ $6^2 = 36$

$2^2 = 4$ $\qquad$ $7^2 = 49$

$3^2 = 9$ $\qquad$ $8^2 = 64$

$4^2 = 16$ $\qquad$ $9^2 = 81$

$5^2 = 25$ $\qquad$ $10^2 = 100$
:::

::::{admonition} Løsning
---
class: solution
---

Vi bruker Pytagoras' læresetning $a^2 + b^2 = c^2$ der $a$ og $b$ er katetene og $c$ er hypotenusen.
Her er hypotenusen $c = 10$ og den ene kateten $a = 8$. Den ukjente kateten $x$ er:

$$
\begin{align*}
8^2 + x^2 &= 10^2 \\
64 + x^2 &= 100 \\
x^2 &= 100 - 64 \\
x^2 &= 36 \\
x &= \sqrt{36} = 6
\end{align*}
$$

::::

:::::::::::::::

---

:::::::::::::::{example} Eksempel 3

Nedenfor vises en rettvinklet trekant med vinklene $90\degree$, $60\degree$ og $30\degree$.

:::{plot}
width: 45%
class: no-click, adaptive-figure
axis: off, equal
xmin: -1.2
xmax: 6.5
ymin: -0.8
ymax: 3.8
figsize: (6, 4)
fontsize: 24
fill-polygon: (0, 0), (5.196, 0), (0, 3), 0072b2, 0.1
line-segment: (0, 0), (5.196, 0), solid, black, 2
line-segment: (5.196, 0), (0, 3), solid, black, 2
line-segment: (0, 3), (0, 0), solid, black, 2
vline: 0.4, 0, 0.4, solid, black, 2
hline: 0.4, 0, 0.4, solid, black, 2
angle-arc: (5.196, 0), 0.5, 150, 180
angle-arc: (0, 3), 0.5, 270, 330
text: -0.4, -0.2, "$A$", center
text: 5.8, -0.2, "$B$", center
text: -0.4, 3.4, "$C$", center
text: 2.3, -0.15, "$8.66$", center
text: -0.6, 1.5, "$x$", center
text: 2.5, 2.2, "$10$", center
text: 3.8, 0.5, "30°", center
text: 0.1, 2.5, "60°", center
:::

I en trekant med vinkene $30\degree$-$60\degree$-$90\degree$ trekant gjelder følgende forhold:

Den korteste kateten er halvparten av lengden til hypotenusen.

Bruk dette til å finne $x$.

::::{admonition} Løsning
---
class: solution
---

Den korteste kateten er halvparten av lengden til hypotenusen. Dermed er $x$ halvparten av 10.

$$
x = \frac{10}{2} = 5
$$


::::

:::::::::::::::

---

:::::::::::::::{admonition} Utforsk 1
---
class: explore
---

:::{figure} ./Videoer/Pythagoras_1.gif
---
class: no-click, adaptive-figure
width: 80%
---
:::

<br>

Nedenfor vises et CAS-vindu som løser likningene

\begin{align*}
    3^2 + 4^2 = c^2 \\
    30^2 + b^2 = 50^2
\end{align*}

:::{ggb} 600 300
---
material_id: kwevpver
toolbar: "true"
---
:::

<br>

Fra utskriften i **celle 1** og **celle 2**, kan vi lese av at løsningene er:

$ c = 5 $ og $b = 40$. Her også forkaster vi de negative løsningene for $b$ og $c$.

:::::::::::::::

:::::{admonition} Utforsk 2
---
class: explore
name: programmering-if-else-utforsk-1
---
Under vises et kort interaktivt program. 

Utforsk og kjør programmet, og forklar hva programmet gjør.

:::{raw} html
---
file: ./python/utforsk/utforsk_1.html
---
:::

:::::::::::::::{admonition} Underveisoppgave 1
---
class: check
---

Sorter stegene i riktig rekkefølge for å lage et program som beregner hypotenusen i en rettvinklet trekant der katetene er $5$ og $12$.

:::{parsons-puzzle}
a = 5
b = 12
c = sqrt(a**2 + b**2)
print(c)
:::

:::::::::::::::

:::::
