# Testausdokumentti

Ohjelmaa on testattu sekä automatisoiduin yksikkö- ja integraatiotestein unittest-kirjastolla että manuaalisesti järjestelmätasolla.

## Yksikkö- ja integraatiotestaus

### Sovelluslogiikka

Sovelluslogiikasta vastaavaa `LevelLogic`-luokkaa testataan `level_logic_test.py`-tiedostossa sijaitsevalla `TestLevelLogic`-testiluokalla.

### Repositorio-luokat

`HowToPlayRepository` ja `LevelRepository`-luokkia testataan testeihin kovakoodatuilla arvoilla.

### Testauskattavuus

Käyttöliittymäkerrosta ja tietokantaa lukuunottamatta sovelluksen testauksen haarautumakattavuus on 77%.

## Järjestelmätestaus

Sovelluksen järjestelmätestaus on suoritettu manuaalisesti.

### Asennus ja konfigurointi

Sovellus on on testattu [käyttöohjeen](./kayttoohje.md) kuvaamalla tavalla Linux-ympäristöön.

### Toiminnallisuudet

Kaikki käyttöohjeen listaamat toiminnallisuudet on käyty läpi. Pelissä ei ole tällä hetkellä tiedossa mitään bugeja.
