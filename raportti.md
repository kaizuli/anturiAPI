#anturiAPI

Tämä projekti on lopputyö backend kurssille, jossa olemme harjoitelleet rest API:n luomista.

##Suunnitelma
Toimin pääosin intuitiivisesti, kuten opiskellessa on tapana. 
Ainoa tarkka suunnitelma, jonka toteutin, oli tietokantojen rakenteet, sillä ne ovat itselleni helpoimmat hahmottaa. Lähdinkin koko projektin rakentamiseen oikeastaan niiden kautta. Anturit ovat yhdessä taulussa, jossa on ID, lohko ja mahdollisen virhetilan osoittava status. Mitatut lämpötilat ovat omassa taulussaan, joista viitataan arvon mitanneeseen anturiin viiteavaimella. Samankaltaisia tauluja voi tarvittaessa lisätä, jos halutaan mitata jotain toisia arvoja myös.
Päätin toteuttaa yksinkertaista tiedostorakennetta, jossa tietokannat ja reitittimet ovat erillisissä kansioissa. Näihin voidaan jatkossa lisätä tiedostoja, jos tarvitaan toiminnallisuuksia muiden arvojen mittaamiseen.

##Rakenne
Pidin rakenteen suhteellisen kaksijakoisena, pitäen pääosassa anturit ja niiden keräämän datan. Päädyin kuitenkin jakamaan tietokantojen skeemat omaan tiedostoonsa, ja muut modelit omaansa. Tämä parantaa mielestäni koodin luettavuutta, sekä antaa enemmän tilaa uusille malleille, joita jatkossa voi tarvita. Mallitiedostoakin voisi harkita jakavansa useampaan osaan, jos niitä alkaa muodostua kovin paljon, esimerkiksi 'sensor_models' & 'temperature_models'. 
En koe, että eri lohkoja tarvitsee tuoda esiin koodillisesti (esimerkiksi enumeja käyttämällä), vaan ne on parempi dokumentoida ja mahdollisesti tuoda esiin käyttöliittymässä. Jos lohkoista halutaan kuitenkin alkaa keräämään dataa laajemmin, niin niille voisi myös luoda oman taulun tietokantaan. Vaatimusmäärittelyssä ei kuitenkaan tällä erää ollut mainittu lohkoihin liittyvästä tiedon keräämisestä, joten tauluun olisi tullut lähinnä sarakkeet ID ja ...niin, eipä siihen olisi tullutkaan muuta.

##Pohdinta

Ymmärsin tätä työtä tehdessä, mitä ovat mallit fastAPI:ssa ja miten niitä käytetään eri paikoissa, kuten 'response_modelina'. Tämä työ on tuntunut myös paljon realistisemmalta, kuin muut koulutyöt. Suurimpana tekijänä tähän on varmaankin se, että tehtävänanto on lähempänä oikeaa "epämääräistä" määrittelyä, joita työelämässä kohtaa useimmin. Toinen tekijä on varmasti myös se, että kurssi on vaativampi ja aihe laajempi.
Olen huomannut backendin aiheena kiinnostavan minua, vaikka en kurssille ilmoittautuessa ollut asiasta vielä täysin varma. Se on saanut minut myös hieman lämpenemään frontendille, vaikka web-sivut eivät vieläkään ole suurin intohimoni.
