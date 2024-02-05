---
layout: "default"
title: "Modèle de données Description"
parent: "Knowledge Graph"
nav_order: 1
nav_exclude: True
---
<svg xmlns="http://www.w3.org/2000/svg" style="display: none;"><symbol id="svg-external-link" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-external-link"><title id="svg-external-link-title">(external link)</title><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line> </symbol></svg>

Modèle de données Description
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
[Milan Valadou](mailto:milan.valadou@meemoo.be)
, [Lennert Van de Velde](mailto:lennert.vandevelde@meemoo.be)
, [Miel Vander Sande](mailto:miel.vandersande@meemoo.be)


Modèle de données pour décrire le contenu des objets.

<div class="wrap">
  <div class="zoom">
  <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" contentStyleType="text/css" preserveAspectRatio="none" version="1.1" viewBox="0 0 886 430" zoomAndPan="magnify"><defs/><g><a href="#ebucore%3AOpenCaptions" target="_top" title="#ebucore%3AOpenCaptions" xlink:actuate="onRequest" xlink:href="#ebucore%3AOpenCaptions" xlink:show="new" xlink:title="#ebucore%3AOpenCaptions" xlink:type="simple"><g id="elem_ebucore_OpenCaptions"><rect codeLine="15" fill="#F1F1F1" height="50.5938" id="ebucore_OpenCaptions" rx="3.5" ry="3.5" style="stroke:#181818;stroke-width:0.5;" width="293" x="133.5" y="373"/><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="111" x="136.5" y="390.9951">OpenCaptions</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="247.5" y="390.9951"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="172" x="251.5" y="390.9951">(ebucore:OpenCaptions)</text><line style="stroke:#181818;stroke-width:0.5;" x1="134.5" x2="425.5" y1="399.2969" y2="399.2969"/><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="18" x="139.5" y="416.292">en</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="157.5" y="416.292"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="47" x="161.5" y="416.292">langue</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="208.5" y="416.292"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="5" x="212.5" y="416.292">:</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="217.5" y="416.292"> </text><text fill="#000000" font-family="sans-serif" font-size="14" font-style="italic" lengthAdjust="spacing" textLength="68" x="221.5" y="416.292">xsd:string</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="289.5" y="416.292"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="34" x="293.5" y="416.292">[0..*]</text></g></a><a href="#haDes%3AAudioReel" target="_top" title="#haDes%3AAudioReel" xlink:actuate="onRequest" xlink:href="#haDes%3AAudioReel" xlink:show="new" xlink:title="#haDes%3AAudioReel" xlink:type="simple"><g id="elem_haDes_AudioReel"><rect codeLine="16" fill="#F1F1F1" height="26.2969" id="haDes_AudioReel" rx="3.5" ry="3.5" style="stroke:#181818;stroke-width:0.5;" width="242" x="7" y="270"/><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="54" x="10" y="287.9951">Bobine</text><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="5" x="64" y="287.9951"> </text><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="43" x="69" y="287.9951">audio</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="112" y="287.9951"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="130" x="116" y="287.9951">(haDes:AudioReel)</text></g></a><a href="#haDes%3AImageReel" target="_top" title="#haDes%3AImageReel" xlink:actuate="onRequest" xlink:href="#haDes%3AImageReel" xlink:show="new" xlink:title="#haDes%3AImageReel" xlink:type="simple"><g id="elem_haDes_ImageReel"><rect codeLine="17" fill="#F1F1F1" height="26.2969" id="haDes_ImageReel" rx="3.5" ry="3.5" style="stroke:#181818;stroke-width:0.5;" width="263" x="284.5" y="270"/><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="54" x="287.5" y="287.9951">Bobine</text><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="5" x="341.5" y="287.9951"> </text><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="61" x="346.5" y="287.9951">d'image</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="407.5" y="287.9951"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="133" x="411.5" y="287.9951">(haDes:ImageReel)</text></g></a><a href="#haDes%3AFilm" target="_top" title="#haDes%3AFilm" xlink:actuate="onRequest" xlink:href="#haDes%3AFilm" xlink:show="new" xlink:title="#haDes%3AFilm" xlink:type="simple"><g id="elem_haDes_Film"><rect codeLine="18" fill="#F1F1F1" height="26.2969" id="haDes_Film" rx="3.5" ry="3.5" style="stroke:#181818;stroke-width:0.5;" width="128" x="352" y="7"/><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="31" x="355" y="24.9951">Film</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="386" y="24.9951"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="87" x="390" y="24.9951">(haDes:Film)</text></g></a><a href="../../terms/fr#skos%3AConcept" target="_top" title="../../terms/fr#skos%3AConcept" xlink:actuate="onRequest" xlink:href="../../terms/fr#skos%3AConcept" xlink:show="new" xlink:title="../../terms/fr#skos%3AConcept" xlink:type="simple"><g id="elem_skos_Concept"><rect codeLine="19" fill="#F1F1F1" height="26.2969" id="skos_Concept" rx="3.5" ry="3.5" style="stroke:#181818;stroke-width:0.5;" width="181" x="461.5" y="385.5"/><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="64" x="464.5" y="403.4951">concept</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="528.5" y="403.4951"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="107" x="532.5" y="403.4951">(skos:Concept)</text></g></a><a href="../../dvd/fr#haObj%3ACarrierRepresentation" target="_top" title="../../dvd/fr#haObj%3ACarrierRepresentation" xlink:actuate="onRequest" xlink:href="../../dvd/fr#haObj%3ACarrierRepresentation" xlink:show="new" xlink:title="../../dvd/fr#haObj%3ACarrierRepresentation" xlink:type="simple"><g id="elem_haObj_CarrierRepresentation"><rect codeLine="20" fill="#F1F1F1" height="83.1875" id="haObj_CarrierRepresentation" rx="3.5" ry="3.5" style="stroke:#181818;stroke-width:0.5;" width="425" x="203.5" y="110"/><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="118" x="206.5" y="127.9951">représentation</text><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="5" x="324.5" y="127.9951"> </text><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="20" x="329.5" y="127.9951">de</text><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="5" x="349.5" y="127.9951"> </text><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="60" x="354.5" y="127.9951">porteur</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="414.5" y="127.9951"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="207" x="418.5" y="127.9951">(haObj:CarrierRepresentation)</text><line style="stroke:#181818;stroke-width:0.5;" x1="204.5" x2="627.5" y1="136.2969" y2="136.2969"/><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="54" x="209.5" y="153.292">nombre</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="263.5" y="153.292"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="18" x="267.5" y="153.292">de</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="285.5" y="153.292"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="56" x="289.5" y="153.292">bobines</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="345.5" y="153.292"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="5" x="349.5" y="153.292">:</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="354.5" y="153.292"> </text><text fill="#000000" font-family="sans-serif" font-size="14" font-style="italic" lengthAdjust="spacing" textLength="82" x="358.5" y="153.292">xsd:decimal</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="440.5" y="153.292"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="36" x="444.5" y="153.292">[0..1]</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="54" x="209.5" y="169.5889">nombre</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="263.5" y="169.5889"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="18" x="267.5" y="169.5889">de</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="285.5" y="169.5889"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="56" x="289.5" y="169.5889">bobines</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="345.5" y="169.5889"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="38" x="349.5" y="169.5889">audio</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="387.5" y="169.5889"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="58" x="391.5" y="169.5889">perdues</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="449.5" y="169.5889"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="5" x="453.5" y="169.5889">:</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="458.5" y="169.5889"> </text><text fill="#000000" font-family="sans-serif" font-size="14" font-style="italic" lengthAdjust="spacing" textLength="82" x="462.5" y="169.5889">xsd:decimal</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="544.5" y="169.5889"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="36" x="548.5" y="169.5889">[0..1]</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="54" x="209.5" y="185.8857">nombre</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="263.5" y="185.8857"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="18" x="267.5" y="185.8857">de</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="285.5" y="185.8857"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="56" x="289.5" y="185.8857">bobines</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="345.5" y="185.8857"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="54" x="349.5" y="185.8857">d'image</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="403.5" y="185.8857"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="58" x="407.5" y="185.8857">perdues</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="465.5" y="185.8857"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="5" x="469.5" y="185.8857">:</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="474.5" y="185.8857"> </text><text fill="#000000" font-family="sans-serif" font-size="14" font-style="italic" lengthAdjust="spacing" textLength="82" x="478.5" y="185.8857">xsd:decimal</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="560.5" y="185.8857"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="36" x="564.5" y="185.8857">[0..1]</text></g></a><a href="#premis%3ARepresentation" target="_top" title="#premis%3ARepresentation" xlink:actuate="onRequest" xlink:href="#premis%3ARepresentation" xlink:show="new" xlink:title="#premis%3ARepresentation" xlink:type="simple"><g id="elem_premis_Representation"><rect codeLine="21" fill="#F1F1F1" height="26.2969" id="premis_Representation" rx="3.5" ry="3.5" style="stroke:#181818;stroke-width:0.5;" width="297" x="582.5" y="270"/><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="118" x="585.5" y="287.9951">représentation</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="703.5" y="287.9951"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="169" x="707.5" y="287.9951">(premis:Representation)</text></g></a><g id="link_haDes_ImageReel_ebucore_OpenCaptions"><path codeLine="30" d="M327.58,296.04 C310.74,302.36 294.98,311.84 284,326 C273.87,339.07 272.5239,351.8971 274.2039,366.9371 " fill="none" id="haDes_ImageReel-to-ebucore_OpenCaptions" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#454645" points="274.87,372.9,277.8462,363.5116,274.3149,367.9309,269.8956,364.3997,274.87,372.9" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#000000" points="285.9927,338.5609,293.7809,333.1025,289.0851,329.5671,285.9927,338.5609" style="stroke:#000000;stroke-width:1.0;"/><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="8" x="298" y="339.0669">a</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="306" y="339.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="23" x="310" y="339.0669">des</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="333" y="339.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="68" x="337" y="339.0669">sous-titres</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="405" y="339.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="62" x="409" y="339.0669">(intégrés)</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="471" y="339.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="33" x="475" y="339.0669">[0..*]</text></g><g id="link_haDes_ImageReel_skos_Concept"><path codeLine="31" d="M460.12,296.12 C478.09,302.72 498.09,312.39 513,326 C531.17,342.59 540.6727,363.9987 546.1627,379.6387 " fill="none" id="haDes_ImageReel-to-skos_Concept" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#454645" points="548.15,385.3,548.9433,375.4831,546.4939,380.5822,541.3949,378.1328,548.15,385.3" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#000000" points="536.5878,338.0489,532.1444,329.6402,528.0505,333.8578,536.5878,338.0489" style="stroke:#000000;stroke-width:1.0;"/><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="28" x="542" y="339.0669">type</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="570" y="339.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="16" x="574" y="339.0669">de</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="590" y="339.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="63" x="594" y="339.0669">coloration</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="657" y="339.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="34" x="661" y="339.0669">[0..1]</text></g><g id="link_haDes_Film_haObj_CarrierRepresentation"><path codeLine="34" d="M416,33.42 C416,50.89 416,77.55 416,103.94 " fill="none" id="haDes_Film-to-haObj_CarrierRepresentation" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#454645" points="416,109.94,420,100.94,416,104.94,412,100.94,416,109.94" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#000000" points="421,76.5664,423.9389,67.5213,418.0611,67.5213,421,76.5664" style="stroke:#000000;stroke-width:1.0;"/><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="20" x="430" y="76.0669">est</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="450" y="76.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="70" x="454" y="76.0669">représenté</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="524" y="76.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="21" x="528" y="76.0669">par</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="549" y="76.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="33" x="553" y="76.0669">[1..*]</text></g><g id="link_haObj_CarrierRepresentation_premis_Representation"><path codeLine="38" d="M514.8,193.12 C579.4,219.67 642.7115,245.707 684.9715,263.077 " fill="none" id="haObj_CarrierRepresentation-to-premis_Representation" style="stroke:#0000FF;stroke-width:1.0;stroke-dasharray:1.0,3.0;"/><polygon fill="none" points="701.62,269.92,687.2525,257.5275,682.6905,268.6265,701.62,269.92" style="stroke:#0000FF;stroke-width:1.0;"/></g><g id="link_haObj_CarrierRepresentation_haDes_AudioReel"><path codeLine="43" d="M325.67,193.12 C266.61,219.67 198.9725,250.0899 160.3325,267.4599 " fill="none" id="haObj_CarrierRepresentation-to-haDes_AudioReel" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#454645" points="154.86,269.92,164.7088,269.8782,159.4204,267.8699,161.4287,262.5816,154.86,269.92" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#000000" points="255.4398,233.6168,264.8945,232.588,262.4841,227.2272,255.4398,233.6168" style="stroke:#000000;stroke-width:1.0;"/><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="42" x="269" y="236.0669">stocké</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="311" y="236.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="8" x="315" y="236.0669">à</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="323" y="236.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="33" x="327" y="236.0669">[1..*]</text></g><g id="link_haObj_CarrierRepresentation_haDes_ImageReel"><path codeLine="44" d="M416,193.12 C416,219.67 416,246.55 416,263.92 " fill="none" id="haObj_CarrierRepresentation-to-haDes_ImageReel" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#454645" points="416,269.92,420,260.92,416,264.92,412,260.92,416,269.92" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#000000" points="421,236.5664,423.9389,227.5213,418.0611,227.5213,421,236.5664" style="stroke:#000000;stroke-width:1.0;"/><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="42" x="430" y="236.0669">stocké</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="472" y="236.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="8" x="476" y="236.0669">à</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="484" y="236.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="33" x="488" y="236.0669">[1..*]</text></g></g></svg>
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
 [OpenCaptions](#ebucore%3AOpenCaptions) |  [Bobine audio](#haDes%3AAudioReel) |  [Bobine d'image](#haDes%3AImageReel) |  [Film](#haDes%3AFilm) |  [concept <svg class="svg-external-link" viewBox="0 0 24 24" aria-labelledby="svg-external-link-title"><use xlink:href="#svg-external-link"></use></svg>](../../terms/fr#skos%3AConcept){:target="_blank"} |  [représentation de porteur <svg class="svg-external-link" viewBox="0 0 24 24" aria-labelledby="svg-external-link-title"><use xlink:href="#svg-external-link"></use></svg>](../../dvd/fr#haObj%3ACarrierRepresentation){:target="_blank"}
## <a id="ebucore%3AOpenCaptions"></a>OpenCaptions <small>[(ebucore:OpenCaptions)](http://www.ebu.ch/metadata/ontologies/ebucore/ebucore#OpenCaptions)</small>




| Propriété | Description | Cardinalité | Type de données |
| :------ | :---------- | :---------- | :------- |
| <a id='schema%3AinLanguage'></a>en langue <br> <small>[(schema:inLanguage)](https://schema.org/inLanguage)</small> | Indique la langue des sous-titres intégrés. | `0..*` | [`xsd:string`](http://www.w3.org/2001/XMLSchema#string)  |

## <a id="haDes%3AImageReel"></a>Bobine d'image <small>[(haDes:ImageReel)](https://data.hetarchief.be/ns/description/ImageReel)</small>


Une bobine d'un porte-film analogique qui contient une vidéo.

| Propriété | Description | Cardinalité | Type de données |
| :------ | :---------- | :---------- | :------- |
| <a id='ebucore%3AhasCaptioning'></a>a des sous-titres (intégrés) <br> <small>[(ebucore:hasCaptioning)](http://www.ebu.ch/metadata/ontologies/ebucore/ebucore#hasCaptioning)</small> | Indique les sous-titres (intégrés) d'une bobine d'image. | `0..*` | [OpenCaptions](#ebucore%3AOpenCaptions)  |
| <a id='haDes%3AcoloringType'></a>type de coloration <br> <small>[(haDes:coloringType)](https://data.hetarchief.be/ns/description/coloringType)</small> | Indication de la coloration de la bobine d'image. | `0..1` | [concept <svg class="svg-external-link" viewBox="0 0 24 24" aria-labelledby="svg-external-link-title"><use xlink:href="#svg-external-link"></use></svg>](../../terms/fr#skos%3AConcept){:target="_blank"} <br>_Valeurs possibles: [`haCt:BandW`](https://data.hetarchief.be/id/color-type/BandW), [`haCt:Color`](https://data.hetarchief.be/id/color-type/Color), [`haCt:Colorized`](https://data.hetarchief.be/id/color-type/Colorized), [`haCt:Composite`](https://data.hetarchief.be/id/color-type/Composite), [`haCt:UnknownColorType`](https://data.hetarchief.be/id/color-type/UnknownColorType)_ |

## <a id="haDes%3AFilm"></a>Film <small>[(haDes:Film)](https://data.hetarchief.be/ns/description/Film)</small>


Cette classe s'applique aux médias dans les archives de meemoo qui proviennent à l'origine d'un support analogue du type film.

| Propriété | Description | Cardinalité | Type de données |
| :------ | :---------- | :---------- | :------- |
| <a id='rel%3Aisr'></a>est représenté par <br> <small>[(rel:isr)](http://id.loc.gov/vocabulary/preservation/relationshipSubType/isr)</small> | Une représentation de l'entité intellectuelle. | `1..*` | [représentation de porteur <svg class="svg-external-link" viewBox="0 0 24 24" aria-labelledby="svg-external-link-title"><use xlink:href="#svg-external-link"></use></svg>](../../dvd/fr#haObj%3ACarrierRepresentation){:target="_blank"}  |

## <a id="haObj%3ACarrierRepresentation"></a>représentation de porteur <small>[(haObj:CarrierRepresentation)](https://data.hetarchief.be/ns/object/CarrierRepresentation)</small>


**Sous-classe de:** 
[représentation](#premis%3ARepresentation)

Une représentation physique ou numérique d'une entité intellectuelle (Intellectual Entity) archivée qui est stockée sur un porteur physique tel qu'une bande vidéo, une bobine de film, du papier ou une toile.

| Propriété | Description | Cardinalité | Type de données |
| :------ | :---------- | :---------- | :------- |
| <a id='haDes%3AnumberOfReels'></a>nombre de bobines <br> <small>[(haDes:numberOfReels)](https://data.hetarchief.be/ns/description/numberOfReels)</small> | Indique le nombre de bobines (quel que soit le type) qui composent le film. | `0..1` | [`xsd:decimal`](http://www.w3.org/2001/XMLSchema#decimal)  |
| <a id='haDes%3AnumberOfMissingAudioReels'></a>nombre de bobines audio perdues <br> <small>[(haDes:numberOfMissingAudioReels)](https://data.hetarchief.be/ns/description/numberOfMissingAudioReels)</small> | Indique si et combien de bobines audio ont été perdues (avant tout processus de numérisation). | `0..1` | [`xsd:decimal`](http://www.w3.org/2001/XMLSchema#decimal)  |
| <a id='haDes%3AnumberOfMissingImageReels'></a>nombre de bobines d'image perdues <br> <small>[(haDes:numberOfMissingImageReels)](https://data.hetarchief.be/ns/description/numberOfMissingImageReels)</small> | Indique si et combien de bobines d'image ont été perdues (avant tout processus de numérisation). | `0..1` | [`xsd:decimal`](http://www.w3.org/2001/XMLSchema#decimal)  |
| <a id='premis%3AstoredAt'></a>stocké à <br> <small>[(premis:storedAt)](http://www.loc.gov/premis/rdf/v3/storedAt)</small> | Le porteur physique où la représentation est stocké. | `1..*` | [Bobine d'image](#haDes%3AImageReel) _ou_ [Bobine audio](#haDes%3AAudioReel)  |



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