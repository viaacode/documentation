---
layout: "default"
title: "Modèle de données Film"
parent: "Modèle de données Description"
nav_order: 1
nav_exclude: True
---
<svg xmlns="http://www.w3.org/2000/svg" style="display: none;"><symbol id="svg-external-link" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-external-link"><title id="svg-external-link-title">(external link)</title><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line> </symbol></svg>

Modèle de données Film
====================

**Version:** 0.0.1

**Version précédente:** 

**Créé:** 2022-01-07

**Dernière mise à jour:** 2024-01-17

**Fichier SHACL:** [film.shacl.ttl](film.shacl.ttl)

**Autres langues:**
[en](../en)
, [nl](../nl)

**Auteurs:**
[Miel Vander Sande](mailto:miel.vandersande@meemoo.be)
, [Lennert Van de Velde](mailto:lennert.vandevelde@meemoo.be)
, [Milan Valadou](mailto:milan.valadou@meemoo.be)


Modèle de données pour fournir une description détaillée des objets Film et leurs composants.

<div class="wrap">
  <div class="zoom">
  <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" contentStyleType="text/css" preserveAspectRatio="none" version="1.1" viewBox="0 0 1132 550" zoomAndPan="magnify"><defs/><g><a href="#ebucore%3AOpenCaptions" target="_top" title="#ebucore%3AOpenCaptions" xlink:actuate="onRequest" xlink:href="#ebucore%3AOpenCaptions" xlink:show="new" xlink:title="#ebucore%3AOpenCaptions" xlink:type="simple"><g id="elem_ebucore_OpenCaptions"><rect codeLine="15" fill="#F1F1F1" height="50.5938" id="ebucore_OpenCaptions" rx="3.5" ry="3.5" style="stroke:#181818;stroke-width:0.5;" width="293" x="375" y="493"/><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="111" x="378" y="510.9951">OpenCaptions</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="489" y="510.9951"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="172" x="493" y="510.9951">(ebucore:OpenCaptions)</text><line style="stroke:#181818;stroke-width:0.5;" x1="376" x2="667" y1="519.2969" y2="519.2969"/><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="18" x="381" y="536.292">en</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="399" y="536.292"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="47" x="403" y="536.292">langue</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="450" y="536.292"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="5" x="454" y="536.292">:</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="459" y="536.292"> </text><text fill="#000000" font-family="sans-serif" font-size="14" font-style="italic" lengthAdjust="spacing" textLength="68" x="463" y="536.292">xsd:string</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="531" y="536.292"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="34" x="535" y="536.292">[0..*]</text></g></a><a href="#haDes%3AAudioReel" target="_top" title="#haDes%3AAudioReel" xlink:actuate="onRequest" xlink:href="#haDes%3AAudioReel" xlink:show="new" xlink:title="#haDes%3AAudioReel" xlink:type="simple"><g id="elem_haDes_AudioReel"><rect codeLine="16" fill="#F1F1F1" height="26.2969" id="haDes_AudioReel" rx="3.5" ry="3.5" style="stroke:#181818;stroke-width:0.5;" width="242" x="249.5" y="390"/><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="54" x="252.5" y="407.9951">Bobine</text><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="5" x="306.5" y="407.9951"> </text><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="43" x="311.5" y="407.9951">audio</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="354.5" y="407.9951"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="130" x="358.5" y="407.9951">(haDes:AudioReel)</text></g></a><a href="#haDes%3AImageReel" target="_top" title="#haDes%3AImageReel" xlink:actuate="onRequest" xlink:href="#haDes%3AImageReel" xlink:show="new" xlink:title="#haDes%3AImageReel" xlink:type="simple"><g id="elem_haDes_ImageReel"><rect codeLine="17" fill="#F1F1F1" height="26.2969" id="haDes_ImageReel" rx="3.5" ry="3.5" style="stroke:#181818;stroke-width:0.5;" width="263" x="527" y="390"/><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="54" x="530" y="407.9951">Bobine</text><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="5" x="584" y="407.9951"> </text><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="61" x="589" y="407.9951">d'image</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="650" y="407.9951"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="133" x="654" y="407.9951">(haDes:ImageReel)</text></g></a><a href="../../terms/fr#skos%3AConcept" target="_top" title="../../terms/fr#skos%3AConcept" xlink:actuate="onRequest" xlink:href="../../terms/fr#skos%3AConcept" xlink:show="new" xlink:title="../../terms/fr#skos%3AConcept" xlink:type="simple"><g id="elem_skos_Concept"><rect codeLine="18" fill="#F1F1F1" height="26.2969" id="skos_Concept" rx="3.5" ry="3.5" style="stroke:#181818;stroke-width:0.5;" width="183" x="703" y="505.5"/><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="66" x="706" y="523.4951">Concept</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="772" y="523.4951"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="107" x="776" y="523.4951">(skos:Concept)</text></g></a><a href="#haDes%3AFilm" target="_top" title="#haDes%3AFilm" xlink:actuate="onRequest" xlink:href="#haDes%3AFilm" xlink:show="new" xlink:title="#haDes%3AFilm" xlink:type="simple"><g id="elem_haDes_Film"><rect codeLine="24" fill="#F1F1F1" height="26.2969" id="haDes_Film" rx="3.5" ry="3.5" style="stroke:#181818;stroke-width:0.5;" width="128" x="177.5" y="94"/><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="31" x="180.5" y="111.9951">Film</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="211.5" y="111.9951"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="87" x="215.5" y="111.9951">(haDes:Film)</text></g></a><a href="#premis%3AIntellectualEntity" target="_top" title="#premis%3AIntellectualEntity" xlink:actuate="onRequest" xlink:href="#premis%3AIntellectualEntity" xlink:show="new" xlink:title="#premis%3AIntellectualEntity" xlink:type="simple"><g id="elem_premis_IntellectualEntity"><rect codeLine="20" fill="#F1F1F1" height="26.2969" id="premis_IntellectualEntity" rx="3.5" ry="3.5" style="stroke:#181818;stroke-width:0.5;" width="335" x="45" y="242"/><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="45" x="48" y="259.9951">Entité</text><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="5" x="93" y="259.9951"> </text><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="101" x="98" y="259.9951">intellectuelle</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="199" y="259.9951"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="174" x="203" y="259.9951">(premis:IntellectualEntity)</text></g></a><a href="#haDes%3ASilentFilm" target="_top" title="#haDes%3ASilentFilm" xlink:actuate="onRequest" xlink:href="#haDes%3ASilentFilm" xlink:show="new" xlink:title="#haDes%3ASilentFilm" xlink:type="simple"><g id="elem_haDes_SilentFilm"><rect codeLine="21" fill="#F1F1F1" height="26.2969" id="haDes_SilentFilm" rx="3.5" ry="3.5" style="stroke:#181818;stroke-width:0.5;" width="211" x="7" y="7"/><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="31" x="10" y="24.9951">Film</text><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="5" x="41" y="24.9951"> </text><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="40" x="46" y="24.9951">muet</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="86" y="24.9951"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="125" x="90" y="24.9951">(haDes:SilentFilm)</text></g></a><a href="#haDes%3ASoundFilm" target="_top" title="#haDes%3ASoundFilm" xlink:actuate="onRequest" xlink:href="#haDes%3ASoundFilm" xlink:show="new" xlink:title="#haDes%3ASoundFilm" xlink:type="simple"><g id="elem_haDes_SoundFilm"><rect codeLine="23" fill="#F1F1F1" height="26.2969" id="haDes_SoundFilm" rx="3.5" ry="3.5" style="stroke:#181818;stroke-width:0.5;" width="234" x="253.5" y="7"/><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="31" x="256.5" y="24.9951">Film</text><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="5" x="287.5" y="24.9951"> </text><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="56" x="292.5" y="24.9951">sonore</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="348.5" y="24.9951"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="132" x="352.5" y="24.9951">(haDes:SoundFilm)</text></g></a><a href="../../audiovisual/fr#haObj%3ACarrierRepresentation" target="_top" title="../../audiovisual/fr#haObj%3ACarrierRepresentation" xlink:actuate="onRequest" xlink:href="../../audiovisual/fr#haObj%3ACarrierRepresentation" xlink:show="new" xlink:title="../../audiovisual/fr#haObj%3ACarrierRepresentation" xlink:type="simple"><g id="elem_haObj_CarrierRepresentation"><rect codeLine="25" fill="#F1F1F1" height="115.7813" id="haObj_CarrierRepresentation" rx="3.5" ry="3.5" style="stroke:#181818;stroke-width:0.5;" width="486" x="415.5" y="197"/><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="121" x="447.5" y="214.9951">Représentation</text><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="5" x="568.5" y="214.9951"> </text><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="20" x="573.5" y="214.9951">de</text><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="5" x="593.5" y="214.9951"> </text><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="60" x="598.5" y="214.9951">porteur</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="658.5" y="214.9951"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="207" x="662.5" y="214.9951">(haObj:CarrierRepresentation)</text><line style="stroke:#181818;stroke-width:0.5;" x1="416.5" x2="900.5" y1="223.2969" y2="223.2969"/><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="56" x="421.5" y="240.292">bobines</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="477.5" y="240.292"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="38" x="481.5" y="240.292">audio</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="519.5" y="240.292"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="58" x="523.5" y="240.292">perdues</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="581.5" y="240.292"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="5" x="585.5" y="240.292">:</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="590.5" y="240.292"> </text><text fill="#000000" font-family="sans-serif" font-size="14" font-style="italic" lengthAdjust="spacing" textLength="85" x="594.5" y="240.292">xsd:boolean</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="679.5" y="240.292"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="36" x="683.5" y="240.292">[0..1]</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="56" x="421.5" y="256.5889">bobines</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="477.5" y="256.5889"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="54" x="481.5" y="256.5889">d'image</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="535.5" y="256.5889"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="58" x="539.5" y="256.5889">perdues</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="597.5" y="256.5889"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="5" x="601.5" y="256.5889">:</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="606.5" y="256.5889"> </text><text fill="#000000" font-family="sans-serif" font-size="14" font-style="italic" lengthAdjust="spacing" textLength="85" x="610.5" y="256.5889">xsd:boolean</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="695.5" y="256.5889"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="36" x="699.5" y="256.5889">[0..1]</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="54" x="421.5" y="272.8857">nombre</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="475.5" y="272.8857"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="18" x="479.5" y="272.8857">de</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="497.5" y="272.8857"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="56" x="501.5" y="272.8857">bobines</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="557.5" y="272.8857"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="5" x="561.5" y="272.8857">:</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="566.5" y="272.8857"> </text><text fill="#000000" font-family="sans-serif" font-size="14" font-style="italic" lengthAdjust="spacing" textLength="165" x="570.5" y="272.8857">xsd:nonNegativeInteger</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="735.5" y="272.8857"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="36" x="739.5" y="272.8857">[0..1]</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="54" x="421.5" y="289.1826">nombre</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="475.5" y="289.1826"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="18" x="479.5" y="289.1826">de</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="497.5" y="289.1826"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="56" x="501.5" y="289.1826">bobines</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="557.5" y="289.1826"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="38" x="561.5" y="289.1826">audio</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="599.5" y="289.1826"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="58" x="603.5" y="289.1826">perdues</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="661.5" y="289.1826"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="5" x="665.5" y="289.1826">:</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="670.5" y="289.1826"> </text><text fill="#000000" font-family="sans-serif" font-size="14" font-style="italic" lengthAdjust="spacing" textLength="165" x="674.5" y="289.1826">xsd:nonNegativeInteger</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="839.5" y="289.1826"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="36" x="843.5" y="289.1826">[0..1]</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="54" x="421.5" y="305.4795">nombre</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="475.5" y="305.4795"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="18" x="479.5" y="305.4795">de</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="497.5" y="305.4795"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="56" x="501.5" y="305.4795">bobines</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="557.5" y="305.4795"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="54" x="561.5" y="305.4795">d'image</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="615.5" y="305.4795"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="58" x="619.5" y="305.4795">perdues</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="677.5" y="305.4795"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="5" x="681.5" y="305.4795">:</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="686.5" y="305.4795"> </text><text fill="#000000" font-family="sans-serif" font-size="14" font-style="italic" lengthAdjust="spacing" textLength="165" x="690.5" y="305.4795">xsd:nonNegativeInteger</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="855.5" y="305.4795"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="36" x="859.5" y="305.4795">[0..1]</text></g></a><a href="#premis%3ARepresentation" target="_top" title="#premis%3ARepresentation" xlink:actuate="onRequest" xlink:href="#premis%3ARepresentation" xlink:show="new" xlink:title="#premis%3ARepresentation" xlink:type="simple"><g id="elem_premis_Representation"><rect codeLine="26" fill="#F1F1F1" height="26.2969" id="premis_Representation" rx="3.5" ry="3.5" style="stroke:#181818;stroke-width:0.5;" width="300" x="825.5" y="390"/><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="121" x="828.5" y="407.9951">Représentation</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="949.5" y="407.9951"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="169" x="953.5" y="407.9951">(premis:Representation)</text></g></a><g id="link_haDes_ImageReel_ebucore_OpenCaptions"><path codeLine="35" d="M563.02,416.12 C546.79,422.51 531.85,432 521.5,446 C511.76,459.18 511.0383,471.8576 513.6183,486.7876 " fill="none" id="haDes_ImageReel-to-ebucore_OpenCaptions" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#454645" points="514.64,492.7,517.049,483.1503,513.7886,487.773,509.1659,484.5126,514.64,492.7" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#000000" points="523.6352,458.6644,531.2263,452.935,526.4089,449.5672,523.6352,458.6644" style="stroke:#000000;stroke-width:1.0;"/><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="8" x="535.5" y="459.0669">a</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="543.5" y="459.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="23" x="547.5" y="459.0669">des</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="570.5" y="459.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="68" x="574.5" y="459.0669">sous-titres</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="642.5" y="459.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="62" x="646.5" y="459.0669">(intégrés)</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="708.5" y="459.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="33" x="712.5" y="459.0669">[0..*]</text></g><g id="link_haDes_ImageReel_skos_Concept"><path codeLine="36" d="M701.61,416.1 C719.51,422.74 739.54,432.44 754.5,446 C772.83,462.63 782.6516,484.0478 788.3916,499.6778 " fill="none" id="haDes_ImageReel-to-skos_Concept" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#454645" points="790.46,505.31,791.1122,495.4828,788.7363,500.6165,783.6026,498.2406,790.46,505.31" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#000000" points="777.1014,458.0348,772.6251,449.6435,768.5477,453.8772,777.1014,458.0348" style="stroke:#000000;stroke-width:1.0;"/><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="28" x="782.5" y="459.0669">type</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="810.5" y="459.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="16" x="814.5" y="459.0669">de</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="830.5" y="459.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="63" x="834.5" y="459.0669">coloration</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="897.5" y="459.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="34" x="901.5" y="459.0669">[0..1]</text></g><g id="link_haDes_Film_premis_IntellectualEntity"><path codeLine="40" d="M239.08,120.2 C233.6,147.75 223.8428,196.8641 218.4028,224.2841 " fill="none" id="haDes_Film-to-premis_IntellectualEntity" style="stroke:#0000FF;stroke-width:1.0;stroke-dasharray:1.0,3.0;"/><polygon fill="none" points="214.9,241.94,224.2881,225.4517,212.5176,223.1165,214.9,241.94" style="stroke:#0000FF;stroke-width:1.0;"/></g><g id="link_haDes_Film_haObj_CarrierRepresentation"><path codeLine="42" d="M275.98,120.07 C324.08,136.91 408.8672,166.5969 489.7372,194.9169 " fill="none" id="haDes_Film-to-haObj_CarrierRepresentation" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#454645" points="495.4,196.9,488.2278,190.1502,490.681,195.2474,485.5837,197.7006,495.4,196.9" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#000000" points="409.2191,160.2188,401.6534,154.4558,399.7109,160.0034,409.2191,160.2188" style="stroke:#000000;stroke-width:1.0;"/><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="20" x="413.5" y="163.0669">est</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="433.5" y="163.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="70" x="437.5" y="163.0669">représenté</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="507.5" y="163.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="21" x="511.5" y="163.0669">par</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="532.5" y="163.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="33" x="536.5" y="163.0669">[1..*]</text></g><g id="link_haDes_SilentFilm_haDes_Film"><path codeLine="44" d="M130.98,33.18 C155.51,49.34 183.5186,67.7977 208.0186,83.9377 " fill="none" id="haDes_SilentFilm-to-haDes_Film" style="stroke:#0000FF;stroke-width:1.0;stroke-dasharray:1.0,3.0;"/><polygon fill="none" points="223.05,93.84,211.3194,78.9272,204.7178,88.9481,223.05,93.84" style="stroke:#0000FF;stroke-width:1.0;"/></g><g id="link_haDes_SoundFilm_haDes_Film"><path codeLine="47" d="M352.02,33.18 C327.49,49.34 299.4814,67.7977 274.9814,83.9377 " fill="none" id="haDes_SoundFilm-to-haDes_Film" style="stroke:#0000FF;stroke-width:1.0;stroke-dasharray:1.0,3.0;"/><polygon fill="none" points="259.95,93.84,278.2822,88.9481,271.6806,78.9272,259.95,93.84" style="stroke:#0000FF;stroke-width:1.0;"/></g><g id="link_haObj_CarrierRepresentation_premis_Representation"><path codeLine="50" d="M782.42,313.07 C843.89,341.39 896.3103,365.5308 932.9003,382.3808 " fill="none" id="haObj_CarrierRepresentation-to-premis_Representation" style="stroke:#0000FF;stroke-width:1.0;stroke-dasharray:1.0,3.0;"/><polygon fill="none" points="949.25,389.91,935.41,376.9309,930.3906,387.8307,949.25,389.91" style="stroke:#0000FF;stroke-width:1.0;"/></g><g id="link_haObj_CarrierRepresentation_haDes_AudioReel"><path codeLine="57" d="M545.91,313.07 C490.07,341.39 432.9417,370.3471 399.7017,387.1971 " fill="none" id="haObj_CarrierRepresentation-to-haDes_AudioReel" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#454645" points="394.35,389.91,404.1861,389.4085,398.8097,387.6493,400.5689,382.2729,394.35,389.91" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#000000" points="480.0404,353.8274,489.4369,352.3585,486.7789,347.1159,480.0404,353.8274" style="stroke:#000000;stroke-width:1.0;"/><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="42" x="493.5" y="356.0669">stocké</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="535.5" y="356.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="8" x="539.5" y="356.0669">à</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="547.5" y="356.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="33" x="551.5" y="356.0669">[1..*]</text></g><g id="link_haObj_CarrierRepresentation_haDes_ImageReel"><path codeLine="58" d="M658.5,313.28 C658.5,341.56 658.5,367.15 658.5,383.95 " fill="none" id="haObj_CarrierRepresentation-to-haDes_ImageReel" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#454645" points="658.5,389.95,662.5,380.95,658.5,384.95,654.5,380.95,658.5,389.95" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#000000" points="663.5,356.5664,666.4389,347.5213,660.5611,347.5213,663.5,356.5664" style="stroke:#000000;stroke-width:1.0;"/><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="42" x="672.5" y="356.0669">stocké</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="714.5" y="356.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="8" x="718.5" y="356.0669">à</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="726.5" y="356.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="33" x="730.5" y="356.0669">[1..*]</text></g></g></svg>
  </div>
</div>

## Espaces de noms

| Prefix | URI      |
| :----- | :------- |
| dct     | [http://purl.org/dc/terms/](http://purl.org/dc/terms/) |
| ebucore     | [http://www.ebu.ch/metadata/ontologies/ebucore/ebucore#](http://www.ebu.ch/metadata/ontologies/ebucore/ebucore#) |
| haCt     | [https://data.hetarchief.be/id/color-type/](https://data.hetarchief.be/id/color-type/) |
| haDes     | [https://data.hetarchief.be/ns/description/](https://data.hetarchief.be/ns/description/) |
| haObj     | [https://data.hetarchief.be/ns/object/](https://data.hetarchief.be/ns/object/) |
| owl     | [http://www.w3.org/2002/07/owl#](http://www.w3.org/2002/07/owl#) |
| pav     | [http://purl.org/pav/](http://purl.org/pav/) |
| premis     | [http://www.loc.gov/premis/rdf/v3/](http://www.loc.gov/premis/rdf/v3/) |
| rdf     | [http://www.w3.org/1999/02/22-rdf-syntax-ns#](http://www.w3.org/1999/02/22-rdf-syntax-ns#) |
| rdfs     | [http://www.w3.org/2000/01/rdf-schema#](http://www.w3.org/2000/01/rdf-schema#) |
| rel     | [http://id.loc.gov/vocabulary/preservation/relationshipSubType/](http://id.loc.gov/vocabulary/preservation/relationshipSubType/) |
| schema     | [https://schema.org/](https://schema.org/) |
| sh     | [http://www.w3.org/ns/shacl#](http://www.w3.org/ns/shacl#) |
| skos     | [http://www.w3.org/2004/02/skos/core#](http://www.w3.org/2004/02/skos/core#) |
| vann     | [http://purl.org/vocab/vann/](http://purl.org/vocab/vann/) |
| xsd     | [http://www.w3.org/2001/XMLSchema#](http://www.w3.org/2001/XMLSchema#) |

## Classes & Propriétés

**Classes:** 
 [OpenCaptions](#ebucore%3AOpenCaptions) |  [Bobine audio](#haDes%3AAudioReel) |  [Bobine d'image](#haDes%3AImageReel) |  [Concept <svg class="svg-external-link" viewBox="0 0 24 24" aria-labelledby="svg-external-link-title"><use xlink:href="#svg-external-link"></use></svg>](../../terms/fr#skos%3AConcept){:target="_blank"} |  [Film](#haDes%3AFilm) |  [Film muet](#haDes%3ASilentFilm) |  [Film sonore](#haDes%3ASoundFilm) |  [Représentation de porteur <svg class="svg-external-link" viewBox="0 0 24 24" aria-labelledby="svg-external-link-title"><use xlink:href="#svg-external-link"></use></svg>](../../audiovisual/fr#haObj%3ACarrierRepresentation){:target="_blank"}
## <a id="ebucore%3AOpenCaptions"></a>OpenCaptions <small>[(ebucore:OpenCaptions)](http://www.ebu.ch/metadata/ontologies/ebucore/ebucore#OpenCaptions)</small>




| Propriété | Description | Cardinalité | Type de données |
| :------ | :---------- | :---------- | :------- |
| <a id='schema%3AinLanguage'></a>en langue <br> <small>[(schema:inLanguage)](https://schema.org/inLanguage)</small> | Indique la langue des sous-titres intégrés. | `0..*` | [`xsd:string`](http://www.w3.org/2001/XMLSchema#string)  |

## <a id="haDes%3AAudioReel"></a>Bobine audio <small>[(haDes:AudioReel)](https://data.hetarchief.be/ns/description/AudioReel)</small>


Une bobine d'un porte-film analogique qui contient de l'audio.


## <a id="haDes%3AImageReel"></a>Bobine d'image <small>[(haDes:ImageReel)](https://data.hetarchief.be/ns/description/ImageReel)</small>


Une bobine d'un porte-film analogique qui contient une vidéo.

| Propriété | Description | Cardinalité | Type de données |
| :------ | :---------- | :---------- | :------- |
| <a id='ebucore%3AhasCaptioning'></a>a des sous-titres (intégrés) <br> <small>[(ebucore:hasCaptioning)](http://www.ebu.ch/metadata/ontologies/ebucore/ebucore#hasCaptioning)</small> | Indique les sous-titres (intégrés) d'une bobine d'image. | `0..*` | [OpenCaptions](#ebucore%3AOpenCaptions)  |
| <a id='haDes%3AcoloringType'></a>type de coloration <br> <small>[(haDes:coloringType)](https://data.hetarchief.be/ns/description/coloringType)</small> | Indication de la coloration de la bobine d'image. | `0..1` | [Concept <svg class="svg-external-link" viewBox="0 0 24 24" aria-labelledby="svg-external-link-title"><use xlink:href="#svg-external-link"></use></svg>](../../terms/fr#skos%3AConcept){:target="_blank"} <br>_Valeurs possibles: [`haCt:BandW`](https://data.hetarchief.be/id/color-type/BandW), [`haCt:Color`](https://data.hetarchief.be/id/color-type/Color), [`haCt:Colorized`](https://data.hetarchief.be/id/color-type/Colorized), [`haCt:Composite`](https://data.hetarchief.be/id/color-type/Composite), [`haCt:UnknownColorType`](https://data.hetarchief.be/id/color-type/UnknownColorType)_ |

## <a id="haDes%3AFilm"></a>Film <small>[(haDes:Film)](https://data.hetarchief.be/ns/description/Film)</small>


**Sous-classe de:** 
[Entité intellectuelle](#premis%3AIntellectualEntity)

**Sous-classes:** 
[Film muet](#haDes%3ASilentFilm)
, [Film sonore](#haDes%3ASoundFilm)

Cette classe s'applique aux médias dans les archives de meemoo qui proviennent à l'origine d'un support analogue du type film.

| Propriété | Description | Cardinalité | Type de données |
| :------ | :---------- | :---------- | :------- |
| <a id='rel%3Aisr'></a>est représenté par <br> <small>[(rel:isr)](http://id.loc.gov/vocabulary/preservation/relationshipSubType/isr)</small> | Une représentation de l'entité intellectuelle. | `1..*` | [Représentation de porteur <svg class="svg-external-link" viewBox="0 0 24 24" aria-labelledby="svg-external-link-title"><use xlink:href="#svg-external-link"></use></svg>](../../audiovisual/fr#haObj%3ACarrierRepresentation){:target="_blank"}  |



## <a id="haDes%3ASilentFilm"></a>Film muet <small>[(haDes:SilentFilm)](https://data.hetarchief.be/ns/description/SilentFilm)</small>


**Sous-classe de:** 
[Film](#haDes%3AFilm)

Cette classe s'applique aux médias dans les archives de meemoo qui proviennent à l'origine d'un support analogue pour le film muet.


_Propriétés de [Film](#haDes%3AFilm):_  [est représenté par](#rel%3Aisr)

## <a id="haDes%3ASoundFilm"></a>Film sonore <small>[(haDes:SoundFilm)](https://data.hetarchief.be/ns/description/SoundFilm)</small>


**Sous-classe de:** 
[Film](#haDes%3AFilm)

Cette classe s'applique aux médias dans les archives de meemoo qui proviennent à l'origine d'un support analogue pour le film sonore.


_Propriétés de [Film](#haDes%3AFilm):_  [est représenté par](#rel%3Aisr)

[^1]: Étiquettes de langue uniques requises
<style>
.zoom > svg {
    width: 100%;
    height: auto;
    background-color: #fff;
}

.zoom > svg text{
   -webkit-user-select: none;
   -moz-user-select: none;
   -ms-user-select: none;
   user-select: none;
}

.wrap {
  overflow: hidden;
  border: 1px solid #E6E6E6;
}

.zoom {
  position: relative;
}

.zoom:hover {
  transform: scale(2.0); cursor: grab;
}
.svg-external-link {
  width: 16px;
  height: 16px;
}
</style>
<script>
var svg = document.querySelector('svg[zoomAndPan="magnify"]');
var zoomDiv = document.querySelector('.zoom');
zoomDiv.addEventListener('mouseleave', onMouseOutZoomDiv);
if (window.PointerEvent) {
  svg.addEventListener('pointerdown', onPointerDown);
  svg.addEventListener('pointerup', onPointerUp);
  svg.addEventListener('pointerleave', onPointerUp); 
  svg.addEventListener('pointermove', onPointerMove); 
} else {

  svg.addEventListener('mousedown', onPointerDown); 
  svg.addEventListener('mouseup', onPointerUp); 
  svg.addEventListener('mouseleave', onPointerUp); 
  svg.addEventListener('mousemove', onPointerMove); 

  svg.addEventListener('touchstart', onPointerDown);
  svg.addEventListener('touchend', onPointerUp);
  svg.addEventListener('touchmove', onPointerMove); 
}

function getPointFromEvent (event) {
  var point = {x:0, y:0};
  if (event.targetTouches) {
    point.x = event.targetTouches[0].clientX;
    point.y = event.targetTouches[0].clientY;
  } else {
    point.x = event.clientX;
    point.y = event.clientY;
  }
  
  return point;
}

var isPointerDown = false;

var pointerOrigin = {
  x: 0,
  y: 0
};

function onPointerDown(event) {
  isPointerDown = true; 
  
  var pointerPosition = getPointFromEvent(event);
  pointerOrigin.x = pointerPosition.x;
  pointerOrigin.y = pointerPosition.y;
}

var originalViewBoxString = svg.getAttribute('viewBox');
var originalViewBoxList= svg.viewBox.baseVal;

var originalViewBox = {
    x: originalViewBoxList.x,
    y: originalViewBoxList.y,
    width: originalViewBoxList.width,
    height: originalViewBoxList.height
};

var viewBox = structuredClone(originalViewBox);
console.log(viewBox);
var newViewBox = {
  x: 0,
  y: 0
};

var ratio = viewBox.width / svg.getBoundingClientRect().width;
window.addEventListener('resize', function() {
  ratio = viewBox.width / svg.getBoundingClientRect().width;
});

function onPointerMove (event) {
  if (!isPointerDown) {
    return;
  }
  event.preventDefault();

  var pointerPosition = getPointFromEvent(event);

  newViewBox.x = viewBox.x - ((pointerPosition.x - pointerOrigin.x) * ratio);
  newViewBox.y = viewBox.y - ((pointerPosition.y - pointerOrigin.y) * ratio);

  var viewBoxString = `${newViewBox.x} ${newViewBox.y} ${viewBox.width} ${viewBox.height}`;
  svg.setAttribute('viewBox', viewBoxString);
}

function onPointerUp() {
  isPointerDown = false;

  viewBox.x = newViewBox.x;
  viewBox.y = newViewBox.y;
}
function onMouseOutZoomDiv(event) {

  var viewBoxString = structuredClone(originalViewBoxString);
  viewBox.x = 0;
  viewBox.y = 0;
  svg.setAttribute('viewBox', originalViewBoxString);
}

</script>
