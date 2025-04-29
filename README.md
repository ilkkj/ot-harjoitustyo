# Ohjelmistotekniikka, harjoitustyö

Pelissä pelaajan tulee tuhota yläpuoleltaan laattoja, jotka putoavat muuten pelaajan päälle.

#### Pelin nykytila:
Pelissä voi liikkua vasemmalle ja oikealle. Pelaaja voi ampua lasereita painamalla välilyöntiä. Jos laser osuu tuhottavaan laatikkoon, laatikko tuhoutuu. Laatikot putoavat tietyn ajan kuluttua alas. Peli alkaa alusta jos pelaajaan osuu laatikko.

## Release
 [Viikko 6 release](https://github.com/ilkkj/ot-harjoitustyo/releases/tag/viikko6)

## Dokumentaatio

- [Käyttöohje](/dokumentaatio/kayttoohje.md)
- [Vaatimusmäärittely](/dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](/dokumentaatio/tuntikirjanpito.md)
- [Changelog](/dokumentaatio/changelog.md)
- [Arkkitehtuurikuvaus](/dokumentaatio/arkkitehtuuri.md)


## Käynnistys

1. Asenna riippuvuudet komennolla:

```bash
poetry install
```

2. Käynnistä sovellus komennolla:

```bash
poetry run invoke start
```


### Testaus

Testit voi suorittaa komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin voi generoida komennolla (avaa raportin selaimeen):

```bash
poetry run invoke coverage-report
```

### Pylint

Pylintin voi suorittaa komennolla:

```bash
poetry run invoke lint
```