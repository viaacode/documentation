---
layout: default
title: Digitale instroom
has_children: true
has_toc: true
nav_order: 1
has_children: true
last_modified_date: 2024-01-25T11:15:40+0100
---

<details markdown="block">
  <summary>
    Inhoudstafel
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

# Digitale instroom

Deze pagina biedt contentpartners (CP's) van meemoo meer inzicht in hoe de metadata gestructureerd wordt in meemoo's MAM en hoe bijgevolg moet aangeleverd worden bij digitale intake. 

## Bestaande instroom

CP's die over born digital of gedigitaliseerd materiaal beschikken, zullen metadata over deze essence moeten aanleveren. Dit gebeurt in de vorm van een sidecar XML-bestand voor elke essence, bv. test.xml + test.mxf. Meemoo's ingestproces verwacht metadata die reeds gemapt werd naar meemoo's metadatamodel, zoals uitgelegd hieronder. Indien je vragen en/of opmerkingen zou hebben, horen we die graag via support@meemoo.be!

Je kan je gemapte metadata valideren aan de hand van onze XSD [`viaa_metadatamodel_xsd.xsd`](https://github.com/viaacode/documentation/blob/7bbe0323731bc180f0b5855b47245935ab8704c4/assets/legacy_born_digital/viaa_metadatamodel_van_cp_naar_viaa.xsd). Een eenvoudige manier om dit te doen, is met xmllint (een deel van  [libxml](http://xmlsoft.org/)). Open een terminal en voer volgend commando uit:

```bash
xmllint --noout --schema viaa_metadatamodel_voor_cp.xsd viaa_metadatamodel_voorbeeld_voor_cp.xml
```

Zie [`viaa_metadatamodel_voorbeeld_voor_cp.xml`](https://github.com/viaacode/documentation/blob/7bbe0323731bc180f0b5855b47245935ab8704c4/assets/legacy_born_digital/viaa_metadatamodel_voorbeeld_van_cp_naar_viaa.xml) voor een voorbeeld van een volledig ingevuld metadatabestand.


## Instroom via meemoo SIP

Momenteel werkt meemoo aan een uniforme meemoo SIP voor toekomstige projecten. Lees alles over de specificatie [hier]({{ site.baseurl }}{% link docs/diginstroom/sip/index.md %}).

Deze SIPs worden aan meemoo aangeleverd via S3. Je leest meer over hoe dit in zijn werk gaat op [Aanlevering van SIPs]({{ site.baseurl }}{% link docs/diginstroom/aanlevering-van-sips.md %}).

## Metadata model

Zie velden: [Algemeen]({{ site.baseurl }}{% link docs/metadata/viaa/algemeen.md %}) | [Digitalisering]({{ site.baseurl }}{% link docs/metadata/viaa/digitalisering.md %}) 
