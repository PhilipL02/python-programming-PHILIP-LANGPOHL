## Laboration 3 - Linjär klassificering

Detta program läser data från "unlabelled_data.csv", som är en fil som endast innehåller koordinater för punkter.
Denna fil, samt resultatet av klassificeringen (labelled_data.csv) ligger under mappen "Data".
Data-mappen finner du i samma mapp som denna README-fil.

Punkterna från denna fil kommer sedan klassificeras med den utvalda funktionen:
calculate_y_on_separator(x) = -0.725x + 0.475

För varje punkt som klassificerats så skrivs koordinaterna ihop med den label som punkten har fått till "labelled_data.csv".

Punkterna från "unlabelled_data.csv" kommer även målas upp i en graf med hjälp av _matplotlib.pyplot_.
I denna graf är punkterna klassificerade och målas då upp i olika färger beroende på klass.
Här visas även den linje som avskiljer klasserna.

Den funktion/ekvation som ska användas för att klassificera punkterna sätts till variabeln "function_for_classification".
I detta fall är det då "calculate_y_on_separator", men denna kan bytas ut för att få en annan klassificering.
Om man vill testa med t.ex. f(x) som finns i linear_classification_utils.py, så kan denna importeras och sättas till "function_for_classification".
Då kommer grafen se annorlunda ut, samt "labelled_data.csv" kommer få annat resultat.

För att se att "labelled_data.csv" genereras när program körs, kan denna fil tas bort innan program körs.

Programmet körs från python-filen linear_classification.py.
För att köra python-filen kan du använda kommandot "python Labs/Lab3/linear_classification.py" i din terminal, om du har klonat hela repositoryt och befinner dig i huvudmappen för repot.