---
layout: "default"
title: "Datamodel Events"
parent: "Knowledge Graph"
nav_order: 1
nav_exclude: True
---
<svg xmlns="http://www.w3.org/2000/svg" style="display: none;"><symbol id="svg-external-link" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-external-link"><title id="svg-external-link-title">(external link)</title><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line> </symbol></svg>

Datamodel Events
====================

**Versie:** 0.0.1

**Vorige versie:** 

**Aangemaakt op:** 2022-06-08

**Laatst gewijzigd op:** 2023-01-12

**SHACL-bestand:** [events.shacl.ttl](events.shacl.ttl)

**Andere talen:**
[en](../en)
, [fr](../fr)

**Auteurs:**
[Lennert Van de Velde](mailto:lennert.vandevelde@meemoo.be)
, [Milan Valadou](mailto:milan.valadou@meemoo.be)
, [Miel Vander Sande](mailto:miel.vandersande@meemoo.be)


Datamodel voor het beschrijven van gebeurtenissen.

<div class="wrap">
  <div class="zoom">
  <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" contentStyleType="text/css" preserveAspectRatio="none" version="1.1" viewBox="0 0 2005 559" zoomAndPan="magnify"><defs/><g><a href="#schema%3ABrand" target="_top" title="#schema%3ABrand" xlink:actuate="onRequest" xlink:href="#schema%3ABrand" xlink:show="new" xlink:title="#schema%3ABrand" xlink:type="simple"><g id="elem_schema_Brand"><rect codeLine="15" fill="#F1F1F1" height="50.5938" id="schema_Brand" rx="3.5" ry="3.5" style="stroke:#181818;stroke-width:0.5;" width="195" x="325" y="502"/><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="46" x="342" y="519.9951">Brand</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="388" y="519.9951"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="111" x="392" y="519.9951">(schema:Brand)</text><line style="stroke:#181818;stroke-width:0.5;" x1="326" x2="519" y1="528.2969" y2="528.2969"/><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="38" x="331" y="545.292">naam</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="369" y="545.292"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="5" x="373" y="545.292">:</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="378" y="545.292"> </text><text fill="#000000" font-family="sans-serif" font-size="14" font-style="italic" lengthAdjust="spacing" textLength="92" x="382" y="545.292">rdf:langString</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="474" y="545.292"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="36" x="478" y="545.292">[1..1]</text></g></a><a href="#prov%3AActivity" target="_top" title="#prov%3AActivity" xlink:actuate="onRequest" xlink:href="#prov%3AActivity" xlink:show="new" xlink:title="#prov%3AActivity" xlink:type="simple"><g id="elem_prov_Activity"><rect codeLine="18" fill="#F1F1F1" height="83.1875" id="prov_Activity" rx="3.5" ry="3.5" style="stroke:#181818;stroke-width:0.5;" width="274" x="474.5" y="166"/><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="69" x="529" y="183.9951">Activiteit</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="598" y="183.9951"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="92" x="602" y="183.9951">(prov:Activity)</text><line style="stroke:#181818;stroke-width:0.5;" x1="475.5" x2="747.5" y1="192.2969" y2="192.2969"/><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="36" x="480.5" y="209.292">heeft</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="516.5" y="209.292"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="74" x="520.5" y="209.292">einddatum</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="594.5" y="209.292"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="5" x="598.5" y="209.292">:</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="603.5" y="209.292"> </text><text fill="#000000" font-family="sans-serif" font-size="14" font-style="italic" lengthAdjust="spacing" textLength="94" x="607.5" y="209.292">xsd:dateTime</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="701.5" y="209.292"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="36" x="705.5" y="209.292">[1..1]</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="36" x="480.5" y="225.5889">heeft</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="516.5" y="225.5889"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="91" x="520.5" y="225.5889">gegenereerd</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="611.5" y="225.5889"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="5" x="615.5" y="225.5889">:</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="620.5" y="225.5889"> </text><text fill="#000000" font-family="sans-serif" font-size="14" font-style="italic" lengthAdjust="spacing" textLength="16" x="624.5" y="225.5889">IRI</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="640.5" y="225.5889"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="36" x="644.5" y="225.5889">[0..1]</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="36" x="480.5" y="241.8857">heeft</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="516.5" y="241.8857"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="75" x="520.5" y="241.8857">startdatum</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="595.5" y="241.8857"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="5" x="599.5" y="241.8857">:</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="604.5" y="241.8857"> </text><text fill="#000000" font-family="sans-serif" font-size="14" font-style="italic" lengthAdjust="spacing" textLength="94" x="608.5" y="241.8857">xsd:dateTime</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="702.5" y="241.8857"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="36" x="706.5" y="241.8857">[1..1]</text></g></a><a href="#premis%3AEvent" target="_top" title="#premis%3AEvent" xlink:actuate="onRequest" xlink:href="#premis%3AEvent" xlink:show="new" xlink:title="#premis%3AEvent" xlink:type="simple"><g id="elem_premis_Event"><rect codeLine="17" fill="#F1F1F1" height="66.8906" id="premis_Event" rx="3.5" ry="3.5" style="stroke:#181818;stroke-width:0.5;" width="307" x="1109" y="7"/><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="98" x="1161" y="24.9951">Gebeurtenis</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="1259" y="24.9951"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="101" x="1263" y="24.9951">(premis:Event)</text><line style="stroke:#181818;stroke-width:0.5;" x1="1110" x2="1415" y1="33.2969" y2="33.2969"/><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="36" x="1115" y="50.292">heeft</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="1151" y="50.292"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="74" x="1155" y="50.292">opmerking</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="1229" y="50.292"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="5" x="1233" y="50.292">:</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="1238" y="50.292"> </text><text fill="#000000" font-family="sans-serif" font-size="14" font-style="italic" lengthAdjust="spacing" textLength="68" x="1242" y="50.292">xsd:string</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="1310" y="50.292"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="36" x="1314" y="50.292">[0..1]</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="36" x="1115" y="66.5889">heeft</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="1151" y="66.5889"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="134" x="1155" y="66.5889">uitkomstopmerking</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="1289" y="66.5889"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="5" x="1293" y="66.5889">:</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="1298" y="66.5889"> </text><text fill="#000000" font-family="sans-serif" font-size="14" font-style="italic" lengthAdjust="spacing" textLength="68" x="1302" y="66.5889">xsd:string</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="1370" y="66.5889"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="36" x="1374" y="66.5889">[0..1]</text></g></a><a href="#premis%3AHardwareAgent" target="_top" title="#premis%3AHardwareAgent" xlink:actuate="onRequest" xlink:href="#premis%3AHardwareAgent" xlink:show="new" xlink:title="#premis%3AHardwareAgent" xlink:type="simple"><g id="elem_premis_HardwareAgent"><rect codeLine="19" fill="#F1F1F1" height="99.4844" id="premis_HardwareAgent" rx="3.5" ry="3.5" style="stroke:#181818;stroke-width:0.5;" width="305" x="237" y="326"/><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="77" x="240" y="343.9951">Hardware</text><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="5" x="317" y="343.9951"> </text><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="45" x="322" y="343.9951">agent</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="367" y="343.9951"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="168" x="371" y="343.9951">(premis:HardwareAgent)</text><line style="stroke:#181818;stroke-width:0.5;" x1="238" x2="541" y1="352.2969" y2="352.2969"/><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="43" x="243" y="369.292">model</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="286" y="369.292"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="5" x="290" y="369.292">:</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="295" y="369.292"> </text><text fill="#000000" font-family="sans-serif" font-size="14" font-style="italic" lengthAdjust="spacing" textLength="68" x="299" y="369.292">xsd:string</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="367" y="369.292"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="36" x="371" y="369.292">[0..1]</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="38" x="243" y="385.5889">naam</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="281" y="385.5889"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="5" x="285" y="385.5889">:</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="290" y="385.5889"> </text><text fill="#000000" font-family="sans-serif" font-size="14" font-style="italic" lengthAdjust="spacing" textLength="92" x="294" y="385.5889">rdf:langString</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="386" y="385.5889"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="36" x="390" y="385.5889">[1..1]</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="92" x="243" y="401.8857">serienummer</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="335" y="401.8857"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="5" x="339" y="401.8857">:</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="344" y="401.8857"> </text><text fill="#000000" font-family="sans-serif" font-size="14" font-style="italic" lengthAdjust="spacing" textLength="68" x="348" y="401.8857">xsd:string</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="416" y="401.8857"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="36" x="420" y="401.8857">[0..1]</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="41" x="243" y="418.1826">versie</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="284" y="418.1826"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="5" x="288" y="418.1826">:</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="293" y="418.1826"> </text><text fill="#000000" font-family="sans-serif" font-size="14" font-style="italic" lengthAdjust="spacing" textLength="68" x="297" y="418.1826">xsd:string</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="365" y="418.1826"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="36" x="369" y="418.1826">[0..1]</text></g></a><a href="#premis%3AAgent" target="_top" title="#premis%3AAgent" xlink:actuate="onRequest" xlink:href="#premis%3AAgent" xlink:show="new" xlink:title="#premis%3AAgent" xlink:type="simple"><g id="elem_premis_Agent"><rect codeLine="27" fill="#F1F1F1" height="26.2969" id="premis_Agent" rx="3.5" ry="3.5" style="stroke:#181818;stroke-width:0.5;" width="160" x="612.5" y="514.5"/><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="47" x="615.5" y="532.4951">Agent</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="662.5" y="532.4951"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="103" x="666.5" y="532.4951">(premis:Agent)</text></g></a><a href="#premis%3AObject" target="_top" title="#premis%3AObject" xlink:actuate="onRequest" xlink:href="#premis%3AObject" xlink:show="new" xlink:title="#premis%3AObject" xlink:type="simple"><g id="elem_premis_Object"><rect codeLine="21" fill="#F1F1F1" height="26.2969" id="premis_Object" rx="3.5" ry="3.5" style="stroke:#181818;stroke-width:0.5;" width="168" x="1497.5" y="194.5"/><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="51" x="1500.5" y="212.4951">Object</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="1551.5" y="212.4951"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="107" x="1555.5" y="212.4951">(premis:Object)</text></g></a><a href="#prov%3AEntity" target="_top" title="#prov%3AEntity" xlink:actuate="onRequest" xlink:href="#prov%3AEntity" xlink:show="new" xlink:title="#prov%3AEntity" xlink:type="simple"><g id="elem_prov_Entity"><rect codeLine="22" fill="#F1F1F1" height="26.2969" id="prov_Entity" rx="3.5" ry="3.5" style="stroke:#181818;stroke-width:0.5;" width="148" x="1507.5" y="362.5"/><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="55" x="1510.5" y="380.4951">Entiteit</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="1565.5" y="380.4951"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="83" x="1569.5" y="380.4951">(prov:Entity)</text></g></a><a href="../../organizations/nl#org%3AOrganization" target="_top" title="../../organizations/nl#org%3AOrganization" xlink:actuate="onRequest" xlink:href="../../organizations/nl#org%3AOrganization" xlink:show="new" xlink:title="../../organizations/nl#org%3AOrganization" xlink:type="simple"><g id="elem_org_Organization"><rect codeLine="23" fill="#F1F1F1" height="26.2969" id="org_Organization" rx="3.5" ry="3.5" style="stroke:#181818;stroke-width:0.5;" width="225" x="1029" y="362.5"/><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="90" x="1032" y="380.4951">Organisatie</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="1122" y="380.4951"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="125" x="1126" y="380.4951">(org:Organization)</text></g></a><a href="../../organizations/nl#schema%3APerson" target="_top" title="../../organizations/nl#schema%3APerson" xlink:actuate="onRequest" xlink:href="../../organizations/nl#schema%3APerson" xlink:show="new" xlink:title="../../organizations/nl#schema%3APerson" xlink:type="simple"><g id="elem_schema_Person"><rect codeLine="24" fill="#F1F1F1" height="26.2969" id="schema_Person" rx="3.5" ry="3.5" style="stroke:#181818;stroke-width:0.5;" width="195" x="7" y="362.5"/><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="66" x="10" y="380.4951">Persoon</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="76" y="380.4951"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="119" x="80" y="380.4951">(schema:Person)</text></g></a><a href="#schema%3AThing" target="_top" title="#schema%3AThing" xlink:actuate="onRequest" xlink:href="#schema%3AThing" xlink:show="new" xlink:title="#schema%3AThing" xlink:type="simple"><g id="elem_schema_Thing"><rect codeLine="25" fill="#F1F1F1" height="26.2969" id="schema_Thing" rx="3.5" ry="3.5" style="stroke:#181818;stroke-width:0.5;" width="154" x="27.5" y="514.5"/><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="35" x="30.5" y="532.4951">Ding</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="65.5" y="532.4951"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="109" x="69.5" y="532.4951">(schema:Thing)</text></g></a><a href="#premis%3ASoftwareAgent" target="_top" title="#premis%3ASoftwareAgent" xlink:actuate="onRequest" xlink:href="#premis%3ASoftwareAgent" xlink:show="new" xlink:title="#premis%3ASoftwareAgent" xlink:type="simple"><g id="elem_premis_SoftwareAgent"><rect codeLine="26" fill="#F1F1F1" height="99.4844" id="premis_SoftwareAgent" rx="3.5" ry="3.5" style="stroke:#181818;stroke-width:0.5;" width="295" x="577" y="326"/><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="72" x="580" y="343.9951">Software</text><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="5" x="652" y="343.9951"> </text><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="45" x="657" y="343.9951">agent</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="702" y="343.9951"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="163" x="706" y="343.9951">(premis:SoftwareAgent)</text><line style="stroke:#181818;stroke-width:0.5;" x1="578" x2="871" y1="352.2969" y2="352.2969"/><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="43" x="583" y="369.292">model</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="626" y="369.292"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="5" x="630" y="369.292">:</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="635" y="369.292"> </text><text fill="#000000" font-family="sans-serif" font-size="14" font-style="italic" lengthAdjust="spacing" textLength="68" x="639" y="369.292">xsd:string</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="707" y="369.292"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="36" x="711" y="369.292">[0..1]</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="38" x="583" y="385.5889">naam</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="621" y="385.5889"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="5" x="625" y="385.5889">:</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="630" y="385.5889"> </text><text fill="#000000" font-family="sans-serif" font-size="14" font-style="italic" lengthAdjust="spacing" textLength="92" x="634" y="385.5889">rdf:langString</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="726" y="385.5889"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="36" x="730" y="385.5889">[1..1]</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="92" x="583" y="401.8857">serienummer</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="675" y="401.8857"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="5" x="679" y="401.8857">:</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="684" y="401.8857"> </text><text fill="#000000" font-family="sans-serif" font-size="14" font-style="italic" lengthAdjust="spacing" textLength="68" x="688" y="401.8857">xsd:string</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="756" y="401.8857"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="36" x="760" y="401.8857">[0..1]</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="41" x="583" y="418.1826">versie</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="624" y="418.1826"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="5" x="628" y="418.1826">:</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="633" y="418.1826"> </text><text fill="#000000" font-family="sans-serif" font-size="14" font-style="italic" lengthAdjust="spacing" textLength="68" x="637" y="418.1826">xsd:string</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="705" y="418.1826"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="36" x="709" y="418.1826">[0..1]</text></g></a><a href="#premis%3AOutcomeStatus" target="_top" title="#premis%3AOutcomeStatus" xlink:actuate="onRequest" xlink:href="#premis%3AOutcomeStatus" xlink:show="new" xlink:title="#premis%3AOutcomeStatus" xlink:type="simple"><g id="elem_premis_OutcomeStatus"><rect codeLine="28" fill="#F1F1F1" height="26.2969" id="premis_OutcomeStatus" rx="3.5" ry="3.5" style="stroke:#181818;stroke-width:0.5;" width="298" x="1700.5" y="194.5"/><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="118" x="1703.5" y="212.4951">Uitkomststatus</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="1821.5" y="212.4951"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="170" x="1825.5" y="212.4951">(premis:OutcomeStatus)</text></g></a><g id="link_prov_Activity_org_Organization"><path codeLine="39" d="M740.81,249 C859.56,286.19 1022.3543,337.1766 1097.2843,360.6466 " fill="none" id="prov_Activity-to-org_Organization" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#454645" points="1103.01,362.44,1095.6171,355.9327,1098.2386,360.9455,1093.2258,363.567,1103.01,362.44" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#000000" points="886.2715,289.0608,878.5182,283.5528,876.7614,289.162,886.2715,289.0608" style="stroke:#000000;stroke-width:1.0;"/><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="10" x="890.5" y="292.0669">is</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="900.5" y="292.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="85" x="904.5" y="292.0669">geassocieerd</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="989.5" y="292.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="26" x="993.5" y="292.0669">met</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="1019.5" y="292.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="34" x="1023.5" y="292.0669">[1..1]</text></g><g id="link_prov_Activity_premis_HardwareAgent"><path codeLine="40" d="M474.48,237.23 C451.66,247.25 430.06,260.77 413.5,279 C401.89,291.78 396.8607,303.4514 393.6207,320.0314 " fill="none" id="prov_Activity-to-premis_HardwareAgent" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#454645" points="392.47,325.92,398.1218,317.8542,393.4289,321.0128,390.2704,316.3199,392.47,325.92" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#000000" points="415.0067,291.1436,423.4288,286.7257,419.2235,282.619,415.0067,291.1436" style="stroke:#000000;stroke-width:1.0;"/><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="10" x="427.5" y="292.0669">is</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="437.5" y="292.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="85" x="441.5" y="292.0669">geassocieerd</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="526.5" y="292.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="26" x="530.5" y="292.0669">met</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="556.5" y="292.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="34" x="560.5" y="292.0669">[1..1]</text></g><g id="link_prov_Activity_premis_SoftwareAgent"><path codeLine="41" d="M601.79,249.2 C600.18,264.65 601.02,281.9 608.5,296 C614.48,307.28 618.4462,313.1986 628.0362,321.8986 " fill="none" id="prov_Activity-to-premis_SoftwareAgent" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#454645" points="632.48,325.93,628.5019,316.9203,628.7768,322.5705,623.1266,322.8454,632.48,325.93" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#000000" points="615.1979,292.2693,614.8907,282.7637,609.3621,284.7597,615.1979,292.2693" style="stroke:#000000;stroke-width:1.0;"/><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="10" x="622.5" y="292.0669">is</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="632.5" y="292.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="85" x="636.5" y="292.0669">geassocieerd</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="721.5" y="292.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="26" x="725.5" y="292.0669">met</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="751.5" y="292.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="34" x="755.5" y="292.0669">[1..1]</text></g><g id="link_prov_Activity_schema_Person"><path codeLine="42" d="M474.16,214.51 C394.76,222.38 294.8,239.99 213.5,279 C170.86,299.46 135.9324,336.7869 118.3324,357.6169 " fill="none" id="prov_Activity-to-schema_Person" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#454645" points="114.46,362.2,123.324,357.907,117.687,358.3808,117.2132,352.7438,114.46,362.2" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#000000" points="213.8611,289.4321,223.3496,288.7837,221.1563,283.3304,213.8611,289.4321" style="stroke:#000000;stroke-width:1.0;"/><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="10" x="227.5" y="292.0669">is</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="237.5" y="292.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="85" x="241.5" y="292.0669">geassocieerd</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="326.5" y="292.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="26" x="330.5" y="292.0669">met</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="356.5" y="292.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="34" x="360.5" y="292.0669">[1..1]</text></g><g id="link_premis_Event_prov_Activity"><path codeLine="45" d="M1131.74,74.05 C1093.32,83.65 1051.21,94.21 1012.5,104 C924.72,126.19 843.646,146.8995 766.226,166.7495 " fill="none" id="premis_Event-to-prov_Activity" style="stroke:#0000FF;stroke-width:1.0;stroke-dasharray:1.0,3.0;"/><polygon fill="none" points="748.79,171.22,767.7162,172.5615,764.7359,160.9375,748.79,171.22" style="stroke:#0000FF;stroke-width:1.0;"/></g><g id="link_premis_Event_org_Organization"><path codeLine="49" d="M1254.31,74.35 C1243.63,115.69 1223.58,188.59 1200.5,249 C1184.18,291.73 1162.3627,334.8443 1150.7727,356.9843 " fill="none" id="premis_Event-to-org_Organization" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#454645" points="1147.99,362.3,1155.7078,356.1816,1150.3089,357.8703,1148.6202,352.4713,1147.99,362.3" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#000000" points="1230.7801,212.2613,1236.651,204.7791,1231.1318,202.7572,1230.7801,212.2613" style="stroke:#000000;stroke-width:1.0;"/><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="114" x="1241.5" y="212.0669">geimplementeerd</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="1355.5" y="212.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="29" x="1359.5" y="212.0669">door</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="1388.5" y="212.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="34" x="1392.5" y="212.0669">[1..1]</text></g><g id="link_premis_Event_premis_HardwareAgent"><path codeLine="50" d="M1108.67,52.97 C882.39,71.4 471.77,111.15 334.5,166 C250.69,199.49 127,221.89 178.5,296 C187.09,308.36 204.0199,318.175 231.2999,328.955 " fill="none" id="premis_Event-to-premis_HardwareAgent" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#454645" points="236.88,331.16,229.9798,324.1323,232.2299,329.3225,227.0398,331.5725,236.88,331.16" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#000000" points="334.7304,209.0667,344.2405,209.1561,342.4768,203.5491,334.7304,209.0667" style="stroke:#000000;stroke-width:1.0;"/><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="70" x="348.5" y="212.0669">instrument</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="418.5" y="212.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="33" x="422.5" y="212.0669">[0..*]</text></g><g id="link_premis_Event_premis_Object"><path codeLine="51" d="M1416.24,57.85 C1452.92,67.17 1490.19,81.63 1520.5,104 C1552.16,127.36 1568.5038,166.8242 1575.8238,188.5442 " fill="none" id="premis_Event-to-premis_Object" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#454645" points="1577.74,194.23,1578.6562,184.4239,1576.1432,189.4918,1571.0752,186.9788,1577.74,194.23" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#000000" points="1557.3683,123.3008,1552.2326,115.2961,1548.5084,119.8436,1557.3683,123.3008" style="stroke:#000000;stroke-width:1.0;"/><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="33" x="1562.5" y="117.0669">heeft</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="1595.5" y="117.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="29" x="1599.5" y="117.0669">bron</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="1628.5" y="117.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="33" x="1632.5" y="117.0669">[0..*]</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="57" x="1562.5" y="132.1997">resultaat</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="1619.5" y="132.1997"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="33" x="1623.5" y="132.1997">[0..*]</text></g><g id="link_premis_Object_premis_Event"><path codeLine="68" d="M1551.72,194.36 C1529.58,185.64 1498.49,174.06 1470.5,166 C1409.35,148.39 1383.76,170.82 1330.5,136 C1307.49,120.96 1292.6583,100.4724 1281.0683,79.6524 " fill="none" id="premis_Object-to-premis_Event" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#454645" points="1278.15,74.41,1279.0326,84.2192,1280.582,78.7787,1286.0225,80.3281,1278.15,74.41" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#000000" points="1330.8964,118.1153,1338.0776,124.3508,1340.3712,118.9389,1330.8964,118.1153" style="stroke:#000000;stroke-width:1.0;"/><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="10" x="1344.5" y="124.5669">is</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="1354.5" y="124.5669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="82" x="1358.5" y="124.5669">gegenereerd</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="1440.5" y="124.5669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="29" x="1444.5" y="124.5669">door</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="1473.5" y="124.5669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="34" x="1477.5" y="124.5669">[0..1]</text></g><g id="link_premis_Event_premis_OutcomeStatus"><path codeLine="52" d="M1416.05,50.89 C1495.02,59.17 1591.81,74.73 1674.5,104 C1737.9,126.44 1799.2922,168.8738 1828.8222,190.7938 " fill="none" id="premis_Event-to-premis_OutcomeStatus" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#454645" points="1833.64,194.37,1828.7975,185.7939,1829.6252,191.3898,1824.0292,192.2175,1833.64,194.37" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#000000" points="1749.2354,121.6714,1741.6124,115.9845,1739.7256,121.5513,1749.2354,121.6714" style="stroke:#000000;stroke-width:1.0;"/><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="33" x="1753.5" y="124.5669">heeft</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="1786.5" y="124.5669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="56" x="1790.5" y="124.5669">uitkomst</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="1846.5" y="124.5669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="34" x="1850.5" y="124.5669">[0..1]</text></g><g id="link_premis_Event_premis_SoftwareAgent"><path codeLine="53" d="M1162.97,74.04 C1118.14,93.72 1068.62,123.41 1038.5,166 C1004.66,213.84 1055.92,252.64 1016.5,296 C995.97,318.58 939.7471,335.5844 878.0671,348.7844 " fill="none" id="premis_Event-to-premis_SoftwareAgent" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#454645" points="872.2,350.04,881.8378,352.068,877.0893,348.9937,880.1636,344.2451,872.2,350.04" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#000000" points="1039.9009,211.0372,1048.4518,206.874,1044.3717,202.643,1039.9009,211.0372" style="stroke:#000000;stroke-width:1.0;"/><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="68" x="1052.5" y="212.0669">uitgevoerd</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="1120.5" y="212.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="29" x="1124.5" y="212.0669">door</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="1153.5" y="212.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="34" x="1157.5" y="212.0669">[0..1]</text></g><g id="link_premis_HardwareAgent_premis_Agent"><path codeLine="56" d="M467.41,425.15 C494.22,441 524.73,458.08 553.5,472 C587.92,488.65 611.8734,498.1328 640.3634,508.3328 " fill="none" id="premis_HardwareAgent-to-premis_Agent" style="stroke:#0000FF;stroke-width:1.0;stroke-dasharray:1.0,3.0;"/><polygon fill="none" points="657.31,514.4,642.3858,502.6839,638.3409,513.9816,657.31,514.4" style="stroke:#0000FF;stroke-width:1.0;"/></g><g id="link_premis_HardwareAgent_schema_Brand"><path codeLine="63" d="M400.21,425.2 C405.86,450.86 411.2495,475.3704 415.8195,496.1204 " fill="none" id="premis_HardwareAgent-to-schema_Brand" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#454645" points="417.11,501.98,419.0806,492.3303,416.0346,497.097,411.2678,494.051,417.11,501.98" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#000000" points="416.5748,468.4495,417.5007,458.9841,411.7603,460.2476,416.5748,468.4495" style="stroke:#000000;stroke-width:1.0;"/><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="33" x="424.5" y="468.0669">merk</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="457.5" y="468.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="34" x="461.5" y="468.0669">[0..1]</text></g><g id="link_premis_Object_prov_Entity"><path codeLine="66" d="M1581.5,220.71 C1581.5,251.4 1581.5,313.56 1581.5,344.28 " fill="none" id="premis_Object-to-prov_Entity" style="stroke:#0000FF;stroke-width:1.0;stroke-dasharray:1.0,3.0;"/><polygon fill="none" points="1581.5,362.28,1587.5,344.28,1575.5,344.28,1581.5,362.28" style="stroke:#0000FF;stroke-width:1.0;"/></g><g id="link_schema_Person_schema_Thing"><path codeLine="72" d="M104.5,388.52 C104.5,416.61 104.5,468.28 104.5,496.42 " fill="none" id="schema_Person-to-schema_Thing" style="stroke:#0000FF;stroke-width:1.0;stroke-dasharray:1.0,3.0;"/><polygon fill="none" points="104.5,514.42,110.5,496.42,98.5,496.42,104.5,514.42" style="stroke:#0000FF;stroke-width:1.0;"/></g><g id="link_premis_SoftwareAgent_premis_Agent"><path codeLine="75" d="M714.11,425.2 C707.39,456.68 702.929,477.6369 698.829,496.8369 " fill="none" id="premis_SoftwareAgent-to-premis_Agent" style="stroke:#0000FF;stroke-width:1.0;stroke-dasharray:1.0,3.0;"/><polygon fill="none" points="695.07,514.44,704.6967,498.0899,692.9613,495.5839,695.07,514.44" style="stroke:#0000FF;stroke-width:1.0;"/></g><g id="link_premis_SoftwareAgent_schema_Brand"><path codeLine="82" d="M626.45,425.2 C574.78,450.86 519.0135,478.5606 477.2435,499.3106 " fill="none" id="premis_SoftwareAgent-to-schema_Brand" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#454645" points="471.87,501.98,481.7098,501.5583,476.3479,499.7555,478.1507,494.3936,471.87,501.98" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#000000" points="565.022,465.7906,574.4302,464.3991,571.8154,459.1348,565.022,465.7906" style="stroke:#000000;stroke-width:1.0;"/><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="33" x="578.5" y="468.0669">merk</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="611.5" y="468.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="34" x="615.5" y="468.0669">[0..1]</text></g></g></svg>
  </div>
</div>

## Naamruimten

| Prefix | URI      |
| :----- | :------- |
| dct     | [http://purl.org/dc/terms/](http://purl.org/dc/terms/) |
| evtAgRole     | [http://id.loc.gov/vocabulary/preservation/eventRelatedAgentRole/](http://id.loc.gov/vocabulary/preservation/eventRelatedAgentRole/) |
| evtObjRole     | [http://id.loc.gov/vocabulary/preservation/eventRelatedObjectRole/](http://id.loc.gov/vocabulary/preservation/eventRelatedObjectRole/) |
| evtOutcome     | [http://id.loc.gov/vocabulary/preservation/eventOutcome/](http://id.loc.gov/vocabulary/preservation/eventOutcome/) |
| haEvt     | [https://data.hetarchief.be/ns/event/](https://data.hetarchief.be/ns/event/) |
| org     | [http://www.w3.org/ns/org#](http://www.w3.org/ns/org#) |
| owl     | [http://www.w3.org/2002/07/owl#](http://www.w3.org/2002/07/owl#) |
| pav     | [http://purl.org/pav/](http://purl.org/pav/) |
| premis     | [http://www.loc.gov/premis/rdf/v3/](http://www.loc.gov/premis/rdf/v3/) |
| prov     | [http://www.w3.org/ns/prov#](http://www.w3.org/ns/prov#) |
| rdf     | [http://www.w3.org/1999/02/22-rdf-syntax-ns#](http://www.w3.org/1999/02/22-rdf-syntax-ns#) |
| rdfs     | [http://www.w3.org/2000/01/rdf-schema#](http://www.w3.org/2000/01/rdf-schema#) |
| schema     | [https://schema.org/](https://schema.org/) |
| sh     | [http://www.w3.org/ns/shacl#](http://www.w3.org/ns/shacl#) |
| skos     | [http://www.w3.org/2004/02/skos/core#](http://www.w3.org/2004/02/skos/core#) |
| vann     | [http://purl.org/vocab/vann/](http://purl.org/vocab/vann/) |
| xsd     | [http://www.w3.org/2001/XMLSchema#](http://www.w3.org/2001/XMLSchema#) |

## Klassen & Eigenschappen

**Klassen:** 
 [Brand](#schema%3ABrand) |  [Activiteit](#prov%3AActivity) |  [Gebeurtenis](#premis%3AEvent) |  [Hardware agent](#premis%3AHardwareAgent) |  [Object](#premis%3AObject) |  [Organisatie <svg class="svg-external-link" viewBox="0 0 24 24" aria-labelledby="svg-external-link-title"><use xlink:href="#svg-external-link"></use></svg>](../../organizations/nl#org%3AOrganization){:target="_blank"} |  [Persoon <svg class="svg-external-link" viewBox="0 0 24 24" aria-labelledby="svg-external-link-title"><use xlink:href="#svg-external-link"></use></svg>](../../organizations/nl#schema%3APerson){:target="_blank"} |  [Software agent](#premis%3ASoftwareAgent) |  [Uitkomststatus](#premis%3AOutcomeStatus)
## <a id="schema%3ABrand"></a>Brand <small>[(schema:Brand)](https://schema.org/Brand)</small>




| Eigenschap | Beschrijving | Kardinaliteit | Datatype |
| :------ | :---------- | :---------- | :------- |
| <a id='schema%3Aname'></a>naam <br> <small>[(schema:name)](https://schema.org/name)</small> | De naam van het item. | `1..1` | [`rdf:langString`](http://www.w3.org/1999/02/22-rdf-syntax-ns#langString)  |

## <a id="prov%3AActivity"></a>Activiteit <small>[(prov:Activity)](http://www.w3.org/ns/prov#Activity)</small>


**Subklassen:** 
[Gebeurtenis](#premis%3AEvent)

Een activiteit is iets dat zich gedurende een bepaalde periode voordoet en op/met entiteiten handelt. Het kan onder meer volgende zaken inhouden: consumeren, verwerken, transformeren, wijzigen, verplaatsen, gebruiken of genereren van entiteiten.

| Eigenschap | Beschrijving | Kardinaliteit | Datatype |
| :------ | :---------- | :---------- | :------- |
| <a id='prov%3AendedAtTime'></a>heeft einddatum <br> <small>[(prov:endedAtTime)](http://www.w3.org/ns/prov#endedAtTime)</small> | De einddatum van de activiteit. | `1..1` | [`xsd:dateTime`](http://www.w3.org/2001/XMLSchema#dateTime)  |
| <a id='prov%3Agenerated'></a>heeft gegenereerd <br> <small>[(prov:generated)](http://www.w3.org/ns/prov#generated)</small> | Het gegenereerde object. | `0..1` | [`IRI`](https://www.rfc-editor.org/rfc/rfc3987.txt)  |
| <a id='prov%3AstartedAtTime'></a>heeft startdatum <br> <small>[(prov:startedAtTime)](http://www.w3.org/ns/prov#startedAtTime)</small> | De startdatum van de activiteit. | `1..1` | [`xsd:dateTime`](http://www.w3.org/2001/XMLSchema#dateTime)  |
| <a id='prov%3AwasAssociatedWith'></a>is geassocieerd met <br> <small>[(prov:wasAssociatedWith)](http://www.w3.org/ns/prov#wasAssociatedWith)</small> | Een `prov:Agent` die enige (niet-gespecificeerde) verantwoordelijkheid had voor het optreden van deze `prov:Activity`. | `1..1` | [Persoon <svg class="svg-external-link" viewBox="0 0 24 24" aria-labelledby="svg-external-link-title"><use xlink:href="#svg-external-link"></use></svg>](../../organizations/nl#schema%3APerson){:target="_blank"} _of_ [Organisatie <svg class="svg-external-link" viewBox="0 0 24 24" aria-labelledby="svg-external-link-title"><use xlink:href="#svg-external-link"></use></svg>](../../organizations/nl#org%3AOrganization){:target="_blank"} _of_ [Software agent](#premis%3ASoftwareAgent) _of_ [Hardware agent](#premis%3AHardwareAgent)  |

## <a id="premis%3AEvent"></a>Gebeurtenis <small>[(premis:Event)](http://www.loc.gov/premis/rdf/v3/Event)</small>


**Subklasse van:** 
[Activiteit](#prov%3AActivity)

Handeling uitgevoerd binnen of buiten het archief die het vermogen beïnvloedt om objecten op lange termijn te bewaren.

| Eigenschap | Beschrijving | Kardinaliteit | Datatype |
| :------ | :---------- | :---------- | :------- |
| <a id='evtAgRole%3Aimp'></a>geimplementeerd door <br> <small>[(evtAgRole:imp)](http://id.loc.gov/vocabulary/preservation/eventRelatedAgentRole/imp)</small> | De organisatie die de gebeurtenis (Event) heeft geimplementeerd. | `1..1` | [Organisatie <svg class="svg-external-link" viewBox="0 0 24 24" aria-labelledby="svg-external-link-title"><use xlink:href="#svg-external-link"></use></svg>](../../organizations/nl#org%3AOrganization){:target="_blank"}  |
| <a id='evtObjRole%3Asou'></a>heeft bron <br> <small>[(evtObjRole:sou)](http://id.loc.gov/vocabulary/preservation/eventRelatedObjectRole/sou)</small> | Het object dat als bron gebruikt is voor de gebeurtenis (Event). | `0..*` | [Object](#premis%3AObject)  |
| <a id='premis%3Anote'></a>heeft opmerking <br> <small>[(premis:note)](http://www.loc.gov/premis/rdf/v3/note)</small> | Een opmerking over de gebeurtenis (Event). | `0..1` | [`xsd:string`](http://www.w3.org/2001/XMLSchema#string)  |
| <a id='premis%3Aoutcome'></a>heeft uitkomst <br> <small>[(premis:outcome)](http://www.loc.gov/premis/rdf/v3/outcome)</small> | De uitkomststatus van de gebeurtenis (Event). | `0..1` | [Uitkomststatus](#premis%3AOutcomeStatus) <br>_Mogelijke waarden: [`evtOutcome:fai`](http://id.loc.gov/vocabulary/preservation/eventOutcome/fai), [`evtOutcome:suc`](http://id.loc.gov/vocabulary/preservation/eventOutcome/suc), [`evtOutcome:war`](http://id.loc.gov/vocabulary/preservation/eventOutcome/war)_ |
| <a id='premis%3AoutcomeNote'></a>heeft uitkomstopmerking <br> <small>[(premis:outcomeNote)](http://www.loc.gov/premis/rdf/v3/outcomeNote)</small> | Een opmerking over de uitkomst van de gebeurtenis (Event). | `0..1` | [`xsd:string`](http://www.w3.org/2001/XMLSchema#string)  |
| <a id='schema%3Ainstrument'></a>instrument <br> <small>[(schema:instrument)](https://schema.org/instrument)</small> | De hardware die gebruikt is voor het uitvoeren van de gebeurtenis (Event). | `0..*` | [Hardware agent](#premis%3AHardwareAgent)  |
| <a id='evtObjRole%3Aout'></a>resultaat <br> <small>[(evtObjRole:out)](http://id.loc.gov/vocabulary/preservation/eventRelatedObjectRole/out)</small> | Het object dat door de gebeurtenis (Event) gegenereerd is. | `0..*` | [Object](#premis%3AObject)  |
| <a id='evtAgRole%3Aexe'></a>uitgevoerd door <br> <small>[(evtAgRole:exe)](http://id.loc.gov/vocabulary/preservation/eventRelatedAgentRole/exe)</small> | De software die de gebeurtenis (Event) heeft uitgevoerd. | `0..1` | [Software agent](#premis%3ASoftwareAgent)  |

_Eigenschappen van [Activiteit](#prov%3AActivity):_  [heeft einddatum](#prov%3AendedAtTime),  [heeft gegenereerd](#prov%3Agenerated),  [heeft startdatum](#prov%3AstartedAtTime),  [is geassocieerd met](#prov%3AwasAssociatedWith)

## <a id="premis%3AHardwareAgent"></a>Hardware agent <small>[(premis:HardwareAgent)](http://www.loc.gov/premis/rdf/v3/HardwareAgent)</small>


**Subklasse van:** 
[Agent](#premis%3AAgent)

Hardwareagent (bv. een computer) die gekoppeld is aan één of meer gebeurtenissen (Events) en/of rechtenuitdrukking(en) geassocieerd met een digitaal object.

| Eigenschap | Beschrijving | Kardinaliteit | Datatype |
| :------ | :---------- | :---------- | :------- |
| <a id='schema%3Abrand'></a>merk <br> <small>[(schema:brand)](https://schema.org/brand)</small> | Het specifieke merk van de agent. | `0..1` | [Brand](#schema%3ABrand)  |
| <a id='schema%3Amodel'></a>model <br> <small>[(schema:model)](https://schema.org/model)</small> | Het specifieke model van de agent. | `0..1` | [`xsd:string`](http://www.w3.org/2001/XMLSchema#string)  |
| <a id='schema%3Aname'></a>naam <br> <small>[(schema:name)](https://schema.org/name)</small> | De naam van het item. | `1..1` | [`rdf:langString`](http://www.w3.org/1999/02/22-rdf-syntax-ns#langString)  |
| <a id='schema%3AserialNumber'></a>serienummer <br> <small>[(schema:serialNumber)](https://schema.org/serialNumber)</small> | Het serienummer of een alfanumerieke identificatie van een bepaald middel. | `0..1` | [`xsd:string`](http://www.w3.org/2001/XMLSchema#string)  |
| <a id='schema%3Aversion'></a>versie <br> <small>[(schema:version)](https://schema.org/version)</small> | Het versienummer of versienaam van de agent. | `0..1` | [`xsd:string`](http://www.w3.org/2001/XMLSchema#string)  |



## <a id="premis%3AObject"></a>Object <small>[(premis:Object)](http://www.loc.gov/premis/rdf/v3/Object)</small>


**Subklasse van:** 
[Entiteit](#prov%3AEntity)

**Subklassen:** 
[Bestand](#premis%3AFile)
, [Intellectuele entiteit](#premis%3AIntellectualEntity)
, [Representatie](#premis%3ARepresentation)

Discrete eenheid van informatie die digitaal moet worden bewaard. Subklassen van Object zijn Intellectual Entity (intellectuele entiteit), Representation (voorstelling/weergave), File (bestand) en Bitstream (bitstream).

| Eigenschap | Beschrijving | Kardinaliteit | Datatype |
| :------ | :---------- | :---------- | :------- |
| <a id='prov%3AwasGeneratedBy'></a>is gegenereerd door <br> <small>[(prov:wasGeneratedBy)](http://www.w3.org/ns/prov#wasGeneratedBy)</small> | De tijd waarop het object volledig is aangemaakt en beschikbaar is voor gebruik. | `0..1` | [Gebeurtenis](#premis%3AEvent)  |



## <a id="premis%3ASoftwareAgent"></a>Software agent <small>[(premis:SoftwareAgent)](http://www.loc.gov/premis/rdf/v3/SoftwareAgent)</small>


**Subklasse van:** 
[Agent](#premis%3AAgent)

Softwareagent (bv. een computerprogramma) die gekoppeld is aan één of meer gebeurtenissen (Events) en/of rechtenuitdrukking(en) geassocieerd met een digitaal object.

| Eigenschap | Beschrijving | Kardinaliteit | Datatype |
| :------ | :---------- | :---------- | :------- |
| <a id='schema%3Abrand'></a>merk <br> <small>[(schema:brand)](https://schema.org/brand)</small> | Het specifieke merk van de agent. | `0..1` | [Brand](#schema%3ABrand)  |
| <a id='schema%3Amodel'></a>model <br> <small>[(schema:model)](https://schema.org/model)</small> | Het specifieke model van de agent. | `0..1` | [`xsd:string`](http://www.w3.org/2001/XMLSchema#string)  |
| <a id='schema%3Aname'></a>naam <br> <small>[(schema:name)](https://schema.org/name)</small> | De naam van het item. | `1..1` | [`rdf:langString`](http://www.w3.org/1999/02/22-rdf-syntax-ns#langString)  |
| <a id='schema%3AserialNumber'></a>serienummer <br> <small>[(schema:serialNumber)](https://schema.org/serialNumber)</small> | Het serienummer of een alfanumerieke identificatie van een bepaald middel. | `0..1` | [`xsd:string`](http://www.w3.org/2001/XMLSchema#string)  |
| <a id='schema%3Aversion'></a>versie <br> <small>[(schema:version)](https://schema.org/version)</small> | Het versienummer of versienaam van de agent. | `0..1` | [`xsd:string`](http://www.w3.org/2001/XMLSchema#string)  |



## <a id="premis%3AOutcomeStatus"></a>Uitkomststatus <small>[(premis:OutcomeStatus)](http://www.loc.gov/premis/rdf/v3/OutcomeStatus)</small>


Algemeen resultaat van het Event in termen van succes, gedeeltelijk succes of falen.


[^1]: Unieke taallabels vereist
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
