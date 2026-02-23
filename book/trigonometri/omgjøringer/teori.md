# Omgjøringer

I denne seksjonen skal vi lære hvordan vi konverterer mellom ulike enheter for lengde, areal og volum.

## Lengdeenheter

De vanligste lengdeenhetene er meter (m), desimeter (dm), centimeter (cm) og millimeter (mm). De forholder seg til hverandre slik:

$$1 \text{ m} = 10 \text{ dm} = 100 \text{ cm} = 1000 \text{ mm}$$

```{plot}
width: 100%
class: no-click, adaptive-figure
axis: off, equal
xmin: 0
xmax: 10
ymin: 0
ymax: 3
fontsize: 16

line-segment: (0.5,2), (2,2), solid, black, 3
text: 1.25, 2.4, "1 m", center, fontsize: 14

line-segment: (2.2,2), (3.7,2), solid, black, 3
text: 2.95, 2.4, "= 10 dm", center, fontsize: 14

line-segment: (3.9,2), (5.4,2), solid, black, 3
text: 4.65, 2.4, "= 100 cm", center, fontsize: 14

line-segment: (5.6,2), (7.1,2), solid, black, 3
text: 6.35, 2.4, "= 1000 mm", center, fontsize: 14

text: 1.25, 1.3, "÷10", center, fontsize: 12, weight: bold
text: 1.25, 0.8, "eller", center, fontsize: 11
text: 1.25, 0.3, "×10", center, fontsize: 12, weight: bold

text: 2.95, 1.3, "÷10", center, fontsize: 12, weight: bold
text: 2.95, 0.8, "eller", center, fontsize: 11
text: 2.95, 0.3, "×10", center, fontsize: 12, weight: bold

text: 4.65, 1.3, "÷10", center, fontsize: 12, weight: bold
text: 4.65, 0.8, "eller", center, fontsize: 11
text: 4.65, 0.3, "×10", center, fontsize: 12, weight: bold
```

**Regel for lengdeenheter:**
- Når vi går fra større enhet til mindre enhet, **multipliserer vi med 10** for hvert steg
- Når vi går fra mindre enhet til større enhet, **deler vi med 10** for hvert steg

---

## Arealenheter

Arealet av en firkant med side $a$ cm har areal $a^2$ cm². Hvis vi konverterer til dm, blir siden $\frac{a}{10}$ dm, og arealet blir $\left(\frac{a}{10}\right)^2 = \frac{a^2}{100}$ dm².

Dette betyr:

$$1 \text{ m}^2 = 100 \text{ dm}^2 = 10\,000 \text{ cm}^2$$

```{plot}
width: 80%
class: no-click, adaptive-figure
axis: off, equal
xmin: 0
xmax: 10
ymin: 0
ymax: 4
fontsize: 14

fill-polygon: (3.5,2), (3.2,2.7), (2.5,3), (1.8,2.7), (1.5,2), (1.8,1.3), (2.5,1), (3.2,1.3), #0072b2, 0.2
line-segment: (3.5,2), (3.2,2.7), solid, black, 1.5
line-segment: (3.2,2.7), (2.5,3), solid, black, 1.5
line-segment: (2.5,3), (1.8,2.7), solid, black, 1.5
line-segment: (1.8,2.7), (1.5,2), solid, black, 1.5
line-segment: (1.5,2), (1.8,1.3), solid, black, 1.5
line-segment: (1.8,1.3), (2.5,1), solid, black, 1.5
line-segment: (2.5,1), (3.2,1.3), solid, black, 1.5
line-segment: (3.2,1.3), (3.5,2), solid, black, 1.5
text: 2.5, 2, "$m^2$", center, fontsize: 14

fill-polygon: (8.5,2), (8.2,2.7), (7.5,3), (6.8,2.7), (6.5,2), (6.8,1.3), (7.5,1), (8.2,1.3), #0072b2, 0.2
line-segment: (8.5,2), (8.2,2.7), solid, black, 1.5
line-segment: (8.2,2.7), (7.5,3), solid, black, 1.5
line-segment: (7.5,3), (6.8,2.7), solid, black, 1.5
line-segment: (6.8,2.7), (6.5,2), solid, black, 1.5
line-segment: (6.5,2), (6.8,1.3), solid, black, 1.5
line-segment: (6.8,1.3), (7.5,1), solid, black, 1.5
line-segment: (7.5,1), (8.2,1.3), solid, black, 1.5
line-segment: (8.2,1.3), (8.5,2), solid, black, 1.5
text: 7.5, 2, "$dm^2$", center, fontsize: 14

line-segment: (3.6,2.7), (5,3.2), solid, black, 1.5
line-segment: (5,3.2), (6.4,2.7), solid, black, 1.5
line-segment: (6.4,2.7), (6.2,2.85), solid, black, 1.5
line-segment: (6.4,2.7), (6.2,2.55), solid, black, 1.5
text: 5, 3.45, "/10^2", center, fontsize: 12

line-segment: (6.4,1.3), (5,0.8), solid, black, 1.5
line-segment: (5,0.8), (3.6,1.3), solid, black, 1.5
line-segment: (3.6,1.3), (3.8,1.45), solid, black, 1.5
line-segment: (3.6,1.3), (3.8,1.15), solid, black, 1.5
text: 5, 0.55, "*10^2", center, fontsize: 12
```

```{plot}
width: 100%
class: no-click, adaptive-figure
axis: off, equal
xmin: 0
xmax: 10
ymin: 0
ymax: 5
fontsize: 14

fill-polygon: (0.5,3), (2.5,3), (2.5,4.5), (0.5,4.5), #0072b2, 0.2
line-segment: (0.5,3), (2.5,3), solid, black, 2
line-segment: (2.5,3), (2.5,4.5), solid, black, 2
line-segment: (2.5,4.5), (0.5,4.5), solid, black, 2
line-segment: (0.5,4.5), (0.5,3), solid, black, 2
text: 1.5, 2.6, "10 cm × 10 cm", center, fontsize: 12
text: 1.5, 2.1, "= 100 cm²", center, fontsize: 12, weight: bold

text: 3.5, 3.75, "konvertert til dm", center, fontsize: 11

fill-polygon: (5,3), (6,3), (6,4), (5,4), #0072b2, 0.2
line-segment: (5,3), (6,3), solid, black, 2
line-segment: (6,3), (6,4), solid, black, 2
line-segment: (6,4), (5,4), solid, black, 2
line-segment: (5,4), (5,3), solid, black, 2
text: 5.5, 2.6, "1 dm × 1 dm", center, fontsize: 12
text: 5.5, 2.1, "= 1 dm²", center, fontsize: 12, weight: bold

text: 8, 3.75, "100 cm² = 1 dm²", center, fontsize: 11, weight: bold
```

**Regel for arealenheter:**
- Når vi går fra en enhet til den neste mindre enhet, **multipliserer vi med 10²** = 100
- Når vi går fra en enhet til den neste større enhet, **deler vi med 10²** = 100

**Eksempler:**
- 1 m² = 100 dm² (fordi 10² = 100)
- 1 dm² = 100 cm² (fordi 10² = 100)  
- 1 m² = 10 000 cm² (fordi 100² = 10 000)

---

## Volumenheter

For volum gjelder det samme prinsippet, men nå med tredje potens. En kube med side $a$ cm har volum $a^3$ cm³. Hvis vi konverterer til dm, blir siden $\frac{a}{10}$ dm, og volumet blir $\left(\frac{a}{10}\right)^3 = \frac{a^3}{1000}$ dm³.

Dette betyr:

$$1 \text{ m}^3 = 1\,000 \text{ dm}^3 = 1\,000\,000 \text{ cm}^3$$

```{plot}
width: 100%
class: no-click, adaptive-figure
axis: off, equal
xmin: 0
xmax: 10
ymin: 0
ymax: 5
fontsize: 14

fill-polygon: (0.5,2.5), (2,2.5), (2.5,3), (1,3), #0072b2, 0.3
line-segment: (0.5,2.5), (2,2.5), solid, black, 1.5
line-segment: (2,2.5), (2.5,3), solid, black, 1.5
line-segment: (2.5,3), (1,3), solid, black, 1.5
line-segment: (1,3), (0.5,2.5), solid, black, 1.5
line-segment: (0.5,2.5), (1,3), solid, black, 1.5
text: 1.5, 2, "10 cm × 10 cm × 10 cm", center, fontsize: 11
text: 1.5, 1.5, "= 1000 cm³", center, fontsize: 12, weight: bold

text: 3.5, 2.5, "konvertert til dm", center, fontsize: 11

fill-polygon: (5.5,2.5), (6.5,2.5), (6.8,3.2), (5.8,3.2), #0072b2, 0.3
line-segment: (5.5,2.5), (6.5,2.5), solid, black, 1.5
line-segment: (6.5,2.5), (6.8,3.2), solid, black, 1.5
line-segment: (6.8,3.2), (5.8,3.2), solid, black, 1.5
line-segment: (5.8,3.2), (5.5,2.5), solid, black, 1.5
line-segment: (5.5,2.5), (5.8,3.2), solid, black, 1.5
text: 6.15, 2, "1 dm × 1 dm × 1 dm", center, fontsize: 11
text: 6.15, 1.5, "= 1 dm³", center, fontsize: 12, weight: bold

text: 8.2, 2.5, "1000 cm³ = 1 dm³", center, fontsize: 11, weight: bold
```

**Regel for volumenheter:**
- Når vi går fra en enhet til den neste mindre enhet, **multipliserer vi med 10³** = 1 000
- Når vi går fra en enhet til den neste større enhet, **deler vi med 10³** = 1 000

**Eksempler:**
- 1 m³ = 1 000 dm³ (fordi 10³ = 1 000)
- 1 dm³ = 1 000 cm³ (fordi 10³ = 1 000)
- 1 m³ = 1 000 000 cm³ (fordi 100³ = 1 000 000)

---

:::::::::::::::{admonition} Sammendrag: Konverteringsregler
---
class: summary
---

| **Enhettype** | **Konvertering per steg** | **Eksempel** |
|---|---|---|
| **Lengde** | ÷10 eller ×10 | 1 m = 10 dm = 100 cm = 1000 mm |
| **Areal** | ÷100 eller ×100 (dvs. 10²) | 1 m² = 100 dm² = 10 000 cm² |
| **Volum** | ÷1000 eller ×1000 (dvs. 10³) | 1 m³ = 1000 dm³ = 1 000 000 cm³ |

:::::::::::::::

