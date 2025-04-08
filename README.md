# Ohjelmistotekniikka, harjoitustyö

Olen toteuttamassa *jonkin sortin* **pelin**.

#### Pelin nykytila:
Pelissä voi liikkua vasemmalle ja oikealle. Pelaaja voi ampua lasereita painamalla välilyöntiä. Jos laser osuu laatikkoon, laatikko tuhoutuu.

## Dokumentaatio

- [Vaatimusmäärittely](/dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](/dokumentaatio/tuntikirjanpito.md)
- [Changelog](/dokumentaatio/changelog.md)
- [Arkkitehtuuri](/dokumentaatio/arkkitehtuuri.md)


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