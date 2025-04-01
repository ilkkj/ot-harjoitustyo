# Ohjelmistotekniikka, harjoitustyö

Olen toteuttamassa *jonkin sortin* **pelin**.

#### Pelin nykytila:
Pelissä voi liikkua vasemmalle ja oikealle, mutta itse pelin toimintoja ei ole vielä toteutettu.

## Dokumentaatio

- [Vaatimusmäärittely](/dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](/dokumentaatio/tuntikirjanpito.md)
- [Changelog](/dokumentaatio/changelog.md)


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
