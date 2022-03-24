# axelrod


## Hogy csinálj új játékost:

Új játékost (statégiát) a Player abstrakt osztály megvalósításával készíthetsz!

Az osztályt a players.py mappába helyezd el!

Az implementálandó metódusok:

1. move:
   Itt kell megadnod, hogy mit szeretnél lépni. A visszatérési érték egy egész szám, aminek 2 értelmes értéke van:
      - 0 -> nem kooperál
      - 1 -> kooperál
2. learn:
   Paraméterként megkapod, hogy mit lépett az ellenfeled az előző körben.

## Hogy tesztelhetsz:

A runner.py fájlt kell futtatnod, ami 2 paramétert vár: 
- -g hány játszma alapján válasszon nyertest
- -m egy játszma hány körből álljon

## Kimenet magyarázat:

- class: az adott osztály neve a tiéd players.ANEVAMITMEGADTAL lesz.
- wins: hány játszmát nyert meg
- won_against: mely játékosokat vert meg
- lost_against: kik ellen veszített

## Számítási sajátosságok:

- Minden játékos 2x játszik, egyszer kihívóként, egyszer pedig kihívottként.
- Egy játszma során a játékosok m alkalommal lépnek, és a lenti kifizetési mátrix alapján kapnak pontot.
- Egy játszmát az nyer, aki több pontot ért el.
- Egy meccset az nyer, aki több játszmát nyert.
- Minden döntetlen esetén a kihívott nyer.
- A kifizetési mátrix: (6,6), (0,8); (8,0); (2,2)