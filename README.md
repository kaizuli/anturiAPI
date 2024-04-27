# anturiAPI
Tämä ohjelma on tehty anturien lämpötila datan keräämiseen.

## Ohjelman käynnistys
Tarvitset python ympäristön, sekä uvicorn, fastapi ja sqlmodel kirjastot tämän ohjelman ajamiseen.

Käytä komentoa:
``` bash
uvicorn app.main --reload
```
Siirry selaimessa promptin osoittamaan osoitteeseen. Lisää osoitteen perään _/docs#_ ja pääset käyttämään ohjelmaa rajapinnan kautta.

Ohjelmassa on hallinnallisia ja dataa esittäviä toimia.

Hallinnalliset toimet ovat:

### Create Sensor
Luo uusi anturi antamalla tiedot lohkosta ja statuksesta. Status 1 on aktiivinen (oletus) ja 0 on virhetilassa.

### Update Sensor Status
Päivittää anturin tilan. Annetaan päivitettävän anturin ID ja haluttaessa tila, johon päivitetään (oletus 1).

### Update Sensor Section
Päivittää anturin lohkon. Syötteenä anturin ID ja uusi lohko.

### Create Temp
Lämpötilojen luomista varten. Testausvaiheessa lämpötilat luodaan manuaalisesti, mutta tuotannossa tämä data saadaan suoraan antureilta. Syötteeksi annetaan anturin ID sekä mitattu lämpötila.

### Delete Temp
Poistaa yksittäisen lämpötilamittauksen ID:n perusteella.

Dataa esittävät toimet:

### List Sensors
Listaa kaikki sensorit ja niiden tiedot.

### Get Sensor With Temps
Listaa tietyn sensorin lämpötila-arvot ja mittausten päivämäärät viimeisimmästä alkaen. Anturi haetaan ID:n perusteella ja valinnaisesti voidaan määritellä haettavien lämpötilojen määrä (oletus 10 kpl). Lisäksi lämpötila-arvoja voi suodattaa mittaamisajan mukaan. Suodattimet ovat vapaaehtoisia, ja niistä voi käyttää halutessaan vain toista.

### List Sensors By Status
Listaa kaikki anturit, joilla on tietty status. Syötteeksi annetaan status, jota antureilta haetaan.

### List Sensors By Section
Listaa kaikki tietyn lohkon anturit. Syötteeksi annetaan lohko, jonka antureita haetaan.
