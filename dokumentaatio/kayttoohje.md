# Käyttöohje

Lataa projektin viimeisimmän [releasen](https://github.com/ilkkj/ot-harjoitustyo/releases/tag/loppupalautus) lähdekoodi valitsemalla _Assets_-osion alta _Source code_.

## Pelin käynnistäminen

Asenna riippuvuudet komennolla:

```bash
poetry install
```

Sen jälkeen suorita alustus komennolla:

```bash
poetry run invoke build
```

Nyt pelin voi käynnistää komennolla:

```bash
poetry run invoke start
```

## Pelaaminen

- Pelissä voi liikkua vasemmalle ja oikealle painamalla nuolinäppäimiä (&larr;), (&rarr;) tai vaihtoehtoisesti painamalla (A), (D).
![](kuvat/game.png)
- Välilyöntiä painamalla pelaaja voi ampua laserin. Laserilla voi tuhota ruskeita laatikoita. 
- Harmaat laatikot ovat tuhoutumattomia. 
- Pelaaja saa pisteitä tuhoamalla ruskeita laatikoita.
![](kuvat/laser.png)

- Pelaajan tulee väistää ylhäältä putoavia laatikoita.
- Peli alkaa alusta jos pelaajaan osuu putoava laatikko.
![](kuvat/falling-box.png)

- Pelin voi aloittaa alusta painamalla (R).
- Päävalikkoon voi poistua painamalla (Q), (ESC).

## High scores taulun tyhjääminen

Sammuta peli. High scores taulun voi nyt tyhjätä komennolla:

```bash
poetry run invoke build
```

Tämän jälkeen pelin voi taas käynnistää normaalisti komennolla:

```bash
poetry run invoke start
```

## Omien pelitasojen käyttäminen

Peli tukee omien pelitasojen käyttämistä. Pelitasojen data löytyy kansiosta `src/data/`. Pelitasojen data tulee olla `level_data.yaml`

Datan tulee olla muodossa:

```yaml
- - [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
  - [3,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,3]
  - [3,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,3]
  - [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3]
  - [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3]
  - [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3]
  - [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3]
  - [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3]
  - [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3]
  - [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3]
  - [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3]
  - [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
```
Matriisin tulee olla settings.py määriteltyjen mittojen mukainen. Vakiona peli tukee 12x17 matriiseja. Ympärillä tulee olla (3) seinät. (1) on tuhottava laatikko. (2) on tuhoutumaton laatikko. 