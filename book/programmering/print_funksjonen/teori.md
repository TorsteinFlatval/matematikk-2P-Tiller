# `print`{l=python}-funksjonen

:::::{admonition} Læringsmål
---
class: tip
---
* Forstå hva `print`{l=python}-funksjonen gjør
* Kunne skrive ut tekst og tall i Python
* Kunne skrive ut verdien av variabler
:::::

`print`{l=python}-funksjonen brukes for å skrive noe ut i konsollen. Dette er nyttig når vi vil se hva programmet gjør underveis.

:::::::::::::::{summary} `print`{l=python}
Syntaksen er:

:::{code-block} python
print(verdi)
:::

`verdi` kan være tekst, tall eller en variabel.
:::::::::::::::

:::::::::::::::{example} Eksempel 1: Skrive ut tekst
:::{code-block} python
print("Hei!")
:::

Utskrift:
```text
Hei!
```
:::::::::::::::

:::::::::::::::{example} Eksempel 2: Skrive ut tall
:::{code-block} python
print(5)
print(3 + 2)
:::

Utskrift:
```text
5
5
```
:::::::::::::::

:::::::::::::::{exercise} Underveisoppgave 1
Ta quizen!

:::{quiz}
Q: Hva skrives ut av programmet? <pre><code class="python">print("Hei")</code></pre>
+ Hei
- "Hei"
- Ingenting
- print("Hei")

Q: Hva skrives ut av programmet? <pre><code class="python">x = 4\nprint(x + 3)</code></pre>
+ 7
- 43
- x + 3
- Feilmelding
:::
:::::::::::::::

:::::::::::::::{example} Eksempel 3: Skrive ut tekst og variabler sammen
:::{code-block} python
navn = "Ada"
alder = 16
print("Navnet er", navn, "og alderen er", alder)
:::

Utskrift:
```text
Navnet er Ada og alderen er 16
```

Vi kan gi `print()`{l=python} flere argumenter atskilt med komma. Teksten og variablene skrives ut med mellomrom mellom dem.
:::::::::::::::

:::::::::::::::{exercise} Underveisoppgave 2
Skriv et program som

- lager variabelen `fornavn`{l=python} med verdien `"Kari"`{l=python}
- lager variabelen `hobby`{l=python} med verdien `"maling"`{l=python}
- skriver ut setningen: "Fornavn er Kari og hobbyen er maling"

:::{interactive-code}
# Skriv programmet ditt her



:::

:::::{answer}
Utskrift:

```text
Fornavn er Kari og hobbyen er maling
```
:::::

:::::{solution}
:::{code-block} python
---
linenos:
---
fornavn = "Kari"
hobby = "maling"
print("Fornavn er", fornavn, "og hobbyen er", hobby)
:::
:::::
:::::::::::::::

:::{margin}
Et tips er å bruke `print`{l=python} ofte når du programmerer. Da er det lettere å se om programmet gjør det du forventer.
:::
