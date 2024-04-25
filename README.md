#anturiAPI
Tämä ohjelma on tehty anturien lämpötila datan keräämiseen.

##Ohjelman käynnistys
Tarvitset python ympäristön, sekä uvicorn, fastapi ja sqlmodel kirjastot tämän ohjelman ajamiseen.

Käytä komentoa:
'''bash
uvicorn app.main --reload
'''
Siirry selaimessa promptin osoittamaan osoitteeseen. Lisää osoitteen perään '/docs' ja pääset käyttämään ohjelmaa rajapinnan kautta.

###Create Sensor
Luo uusi anturi antamalla tiedot lohkosta ja statuksesta. Status 1 on aktiivinen (oletus) ja 0 on virhetilassa.

###List Sensors
Listaa kaikki sensorit ja niiden tiedot.

###Get Sensor With Temps
Listaa tietyn sensorin lämpötila-arvot ja mittausten päivämäärät viimeisimmästä alkaen. Anturi haetaan ID:n perusteella ja valinnaisesti voidaan määritellä haettavien lämpötilojen määrä (oletus 10 kpl).

###Update Sensor Status
Päivittää anturin tilan. Annetaan päivitettävän anturin ID ja haluttaessa tila, johon päivitetään (oletus 1).

###Update Sensor Section
Päivittää anturin lohkon. Syötteenä anturin ID ja uusi lohko.

###Create Temp
Lämpötilojen luomista varten. Testausvaiheessa lämpötilat luodaan manuaalisesti, mutta tuotannossa tämä data saadaan suoraan antureilta. Syötteeksi annetaan anturin ID sekä mitattu lämpötila.

###Delete Temp
Poistaa yksittäisen lämpötilamittauksen ID:n perusteella.

