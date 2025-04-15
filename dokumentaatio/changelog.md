# Changelog

## Viikko 3

- Käyttäjä voi liikkua pelissä vasemmalle ja oikealle.
- Pelikentän yläosaan luodaan seinät.
- Lisätty Player- ja Box-luokat, joilla luodaan pelaaja ja seinät.
- Lisätty Level-luokka, joka luo matriisin pelikenttää varten.

## Viikko 4

- Lisätty Game-luokka, joka hoitaa pelin kulkua.
- Lisätty Laser-luokka pelaajan ampumia lasereita varten.
- Koodi jaettu luokkien sisälle omiin tiedostoihin mainista.
- Luotu tiedosto yleisiä asetuksia varten
- Pelaaja voi nyt rikkoa laatikoita ampumalla lasereita (välilyönti).
- Pelaajan hahmon muoto muutettu
- Luokilla ja funktioilla on alustavat Docstring dokumentoinnit.
- Tasojen luonti testataan.
- Pelaajan liikkeiden muutosta testataan.

## Viikko 5

- Koodin rakenne muutettu. Käyttöliittymä ja sovelluslogiikka pyritty saamaan paremmin erilleen toisistaan.
- Sovelluslogiikka muutettu toimimaan suurimmaksi osaksi spritejen avulla. Edellisen version sekalaisia viritelmiä poistettu.
- Uudet luokat Clock, EventQueue, GameLoop ja Renderer koodin jakamiseksi osiin.
- Lisätty SolidBox ja Wall luokat. SolidBox on tuhoutumaton laatikko ja Wall hoitaa pelikentän reunukset.
- Laserin kokoa pienennetty ja nopeutta kasvatettu.
- Pelaaja voi sammuttaa pelin painamalla (Q) ja aloittaa pelin alusta painamalla (R).
- Peli alkaa alusta jos pelaajaan osuu laatikko.