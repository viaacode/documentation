---
layout: default
title: IIIF 3.0 Image API
parent: Een integratie ontwikkelen
has_children: false
nav_order: 3
last_modified_date: 2022-03-14T11:40:08+0100
---

<details markdown="block">
  <summary>
    Inhoudstafel
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

# Over IIIF 

Het [Image Interoperability Framework](https://iiif.io) (IIIF) is een set van open standaarden om gedigitaliseerde archieven online beschikbaar te stellen. Het zorgt voor een gebruiksvriendelijke toegang tot de objecten uit een archief.  
Het IIIF-protocol maakt gebruik van een stabiel manifest, en voorziet een duurzame URL voor elk object in het archief. Hierdoor kunnen er later eventueel andere versies van eenzelfde object worden toegevoegd aan een collectie (bijvoorbeeld in een hogere resolutie) zonder dat de URL van dit object wijzigt. 

Het IIIF-protocol bestaat uit 6 API's, die onafhankelijk van elkaar gebruikt kunnen worden. Momenteel wordt enkel de Image API benut. Dit stelt de gebruiker in staat om op een performante manier (delen van) afbeeldingen te bekijken, te herschalen, te roteren,... 

## Authenticatie

De door meemoo voorziene IIIF-endpoints zijn publiek beschikbaar, er is dus geen authenticatie vereist. 

## Endpoint

Er wordt gebruik gemaakt van de Image API versie 3.0. 
Het meemoo-Image-API-endpoint voldoet aan het hoogste IIIF-compliance level, namelijk level 2. 
Meer info over IIIF en de Image API kan je terugvinden op de [iiif.io website](https://iiif.io/api/image/3.0/). 

### Omgevingen

Het endpoint is beschikbaar op 3 omgevingen: TST, QAS en PRD.  
Let op: de afbeeldingen kunnen verschillen van omgeving tot omgeving, afhankelijk van de beschikbaarheid in het meemoo-archiefsysteem. 

### Opbouw URL

Om een afbeelding op te halen via een URL, wordt de URL als volgt opgebouwd: 

```shell
https://{DOMEIN}/iiif/{IDENTIFIER}.jp2/{REGIO}/{GROOTTE}/{ROTATIE}/{KWALITEIT}.{FORMAAT}
```

Hieronder volgt een beknopte samenvatting van de mogelijkheden van het endpoint, waarbij elke parameter afzonderlijk wordt toegelicht.  
Voor een uitgebreide beschrijving van de URL-samenstelling, zie de [iiif.io documentatie](https://iiif.io/api/image/3.0/#21-image-request-uri-syntax).

#### Domein

Het domein geeft aan vanuit welke omgeving het object wordt opgevraagd. Er zijn 3 omgevingen beschikbaar: TST, QAS en PRD.  

| Omgeving | Domein                                               |
|----------|------------------------------------------------------|
| TST      | [images-tst.meemoo.be](https://images-tst.meemoo.be) |
| QAS      | [images-qas.meemoo.be](https://images-qas.meemoo.be) |
| PRD      | [images.meemoo.be](https://images.meemoo.be)         |


#### Identifier

De identifier van het op te halen object moet overeenkomen met de `OriginalFilename` van het object. Dit vind je terug in de metadata van het gewenste object.  
Een lijst van beschikbare identifiers is te raadplegen via de [inventaris](https://images.meemoo.be/inventory).

#### Regio

De parameter `REGIO` bepaalt welk rechthoekig vlak uit de afbeelding teruggegeven wordt. Een regio kan uitgedrukt worden in pixelcoördinaten, percentages of door de waarde `full`. Deze laatste optie zorgt ervoor dat de volledige afbeelding teruggegeven wordt. 

#### Grootte

De parameter `GROOTTE` geeft aan tot welke grootte de gekozen regio geschaald moet worden. Je kan hier `max` invullen om de afbeeldingen maximaal te laten schalen. Opschaling is hier niet van toepassing. 

Alle afbeeldingen die beschikbaar zijn via het meemoo-IIIF-endpoint hebben een maximale lengte of breedte van 5000 pixels. Afbeeldingen die auteursrechtelijk beschermd zijn, worden ontsloten in 640x480 pixelformaat. 

#### Rotatie

De afbeelding kan ook geroteerd worden getoond, hiervoor kan je een getal tussen 0 en 360 meegeven in de URL. Dit getal geeft het aantal graden draaiing met de klok mee aan. 

#### Kwaliteit

Om de kwaliteit van de afbeelding te bepalen, kan je kiezen uit de volgende waardes: 
- `color`
- `gray`
- `bitonal`
- `default` 

Deze waarde zal bepalen of de afbeelding getoond wordt in kleur, grijswaarden of zwart-wit. 

#### Formaat

Als formaat kan je kiezen tussen `jpg` en `png`, afhankelijk van het gewenste afbeeldingsformaat. 

### Inventaris

Een inventaris van de beschikbare beelden is terug te vinden op [https://images.meemoo.be/inventory](https://images.meemoo.be/inventory). 

# Use case 

## Algemeen

Deze paragraaf beschrijft een use case waarbij een object wordt opgehaald via het IIIF-endpoint en getoond wordt in de browser. 
Volgende transformaties worden toegepast op het object: 
- een bepaalde regio selecteren
- schaling van de gekozen regio
- rotatie van de gekozen regio
- de gekozen regio in grijswaarden tonen
- formaatkeuze van de afbeelding

In deze use case wordt slechts een subset van de mogelijkheden van een IIIF-endpoint gebruikt. Voor de volledige waaier aan mogelijkheden, zie de Image API-[documentatie](https://iiif.io/api/image/3.0/#21-image-request-uri-syntax). 

## Stap 1: Bepalen van de identifier

Stel dat het object 'De bespotting van Christus (Ecce Homo)' van James Ensor getoond moet worden. De [inventaris](https://images.meemoo.be/inventory) geeft aan dat de originele bestandsnaam van dit werk `h12v432j8x` is (zie kolom `Descriptive.OriginalFilename`). 

## Stap 2: De URL opbouwen

### Identifier

Indien de identifier wordt ingevuld, is de URL als volgt: 

```shell 
https://images.meemoo.be/iiif/h12v432j8x.jp2/full/max/0/default.jpg
```

Wanneer je naar deze URL surft, wordt de volledige afbeelding teruggegeven, zonder enige toegepaste transformaties.  

### Regio

Stel dat een regio met volgende eigenschappen gecapteerd moet worden: 
- 1700 pixels offset links
- 1300 pixels offset boven
- 1100 pixels breedte
- 1750 pixels hoogte

In dit geval wordt de URL als volgt opgebouwd: 

```shell
https://images.meemoo.be/iiif/h12v432j8x.jp2/1700,1300,1100,1750/full/0/default.jpg
```

De getoonde afbeelding is bijgesneden naargelang de gekozen waardes. 

### Grootte

Om de gekozen regio te schalen tot een maximum breedte van 300px en een maximum hoogte van 400px zonder de beeldverhouding te verliezen, kan de parameter `GROOTTE` als volgt worden ingevuld:

```shell
https://images.meemoo.be/iiif/h12v432j8x.jp2/1700,1300,1100,1750/!300,400/0/default.jpg
```

In dit geval wordt de eerder gekozen regio van de afbeelding teruggegeven met een breedte van 251px en een hoogte van 400px. 

### Rotatie

Indien de geschaalde regio 90 graden met de klok mee geroteerd moet worden, kan de URL als volgt worden aangepast: 

```shell
https://images.meemoo.be/iiif/h12v432j8x.jp2/1700,1300,1100,1750/!300,400/90/default.jpg
```

### Kwaliteit

Om de afbeelding in grijswaarden weer te geven, kan je `gray` invullen bij de parameter `KWALITEIT`. 

```shell
https://images.meemoo.be/iiif/h12v432j8x.jp2/1700,1300,1100,1750/!300,400/90/gray.jpg
```

### Formaat

Om de afbeelding in PNG-formaat te verkrijgen, wordt `jpg` in de URL simpelweg vervangen door `png`. 

``` shell
https://images.meemoo.be/iiif/h12v432j8x.jp2/1700,1300,1100,1750/!300,400/90/default.png
```

