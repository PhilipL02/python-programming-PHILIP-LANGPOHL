## Laboration 3 - Linjär klassificering

Detta program läser data från <code>unlabelled_data.csv</code>, som är en fil som endast innehåller koordinater för punkter.
Denna fil, samt resultatet av klassificeringen (<code>labelled_data.csv</code>) ligger under mappen <code>Data</code>.
Mappen <code>Data</code> hittar du i samma mapp som denna README-fil.

### Klassificering

Punkterna från filen <code>unlabelled_data.csv</code> klassificeras med hjälp av den utvalda funktionen:
<code>calculate_y_on_separator(x) = -0.725x + 0.475</code>

För varje punkt jämförs dess y-koordinat med värdet som beräknas av funktionen för samma x-koordinat. Om punktens y-värde är större än funktionens värde, tilldelas den klass (label) 1, annars får den klass 0.

De klassificerade punkternas koordinater och deras tilldelade klass sparas i filen <code>labelled_data.csv</code>.

### Visualisering

Programmet använder biblioteket _matplotlib.pyplot_ för att visualisera punkterna från <code>unlabelled_data.csv</code>. Klassificerade punkter visas i olika färger beroende på klass, och den separerande linjen ritas också upp i grafen.

### Anpassa klassificeringsfunktionen

Den funktion som används för att klassificera punkterna anges via variabeln <code>function_for_classification</code>.
För nuvarande är detta <code>calculate_y_on_separator</code>, men denna kan bytas ut för att få en annan klassificering.

Till exempel kan du använda <code>f(x) = -0.489x</code> som finns definierad i <code>linear_classification_utils.py</code>. 
För att göra detta, importera funktionen och tilldela den till <code>function_for_classification</code>. Detta kommer att förändra både grafens utseende och resultatet i <code>labelled_data.csv</code>.

### Så här kör du programmet

Programmet körs från python-filen <code>linear_classification.py</code>.

#### Köra programmet från terminalen

Om du har klonat hela repot och befinner dig i huvudmappen, kör följande kommando i din terminal:
```bash
python Labs/Lab3/linear_classification.py
```
