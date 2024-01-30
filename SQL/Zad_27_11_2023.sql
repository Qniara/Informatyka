Grupowanie: (creditcard z AW)

1. Policz ile jest wszystkich kart
SELECT COUNT(creditcard.CreditCardID) 
FROM creditcard

2. Policz ile kart wygasa w 2008 roku
SELECT ExpYear, count(creditcard.CardNumber)
FROM creditcard
WHERE creditcard.ExpYear=2008
GROUP BY creditcard.ExpYear;

3. Policz ile kard wygasa w 2008 roku w październiku
SELECT ExpYear, count(creditcard.CardNumber)
FROM creditcard
WHERE creditcard.ExpYear=2008
AND creditcard.ExpMonth=10
GROUP BY creditcard.ExpYear;

4. Policz ilość kart Vista
SELECT count(creditcard.CardNumber)
FROM creditcard
WHERE creditcard.CardType='Vista';

5. Stwórz zostawienie ilości kart (po CardType) wygasających w styczniu
SELECT creditcard.CardType, COUNT(creditcard.CreditCardID)
FROM creditcard
WHERE creditcard.ExpMonth=1
GROUP BY creditcard.CardType;

6. Wypisz 3 najliczniejsze miesiące kiedy wygasają karty Vista w 2007 roku.
SELECT creditcard.ExpMonth, COUNT(creditcard.CreditCardID) AS ilosc_kart
FROM creditcard
WHERE creditcard.ExpYear=2007
GROUP BY creditcard.ExpMonth 
ORDER BY ilosc_kart desc
LIMIT 3;

7. W którym roku wygasa najmniej kart w miesiącach letnich?
SELECT ExpYear 
FROM creditcard 
WHERE ExpMonth REGEXP "^[6-8]$"
GROUP BY ExpYear
ORDER BY COUNT(*) ASC
LIMIT 1;

8. Utwórz zestawienie typów kart wraz z ilośćiami zkaładając, że wygasają w miesiącach nieparzystych.
SELECT CardType, COUNT(*) FROM creditcard 
WHERE ExpMonth%2=1
GROUP BY CardType;
