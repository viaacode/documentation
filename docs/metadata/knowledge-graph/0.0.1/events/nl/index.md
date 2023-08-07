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
[Milan Valadou](mailto:milan.valadou@meemoo.be)
, [Lennert Van de Velde](mailto:lennert.vandevelde@meemoo.be)
, [Miel Vander Sande](mailto:miel.vandersande@meemoo.be)


Datamodel voor het beschrijven van gebeurtenissen.

<div class="wrap">
  <div class="zoom">
  <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" contentStyleType="text/css" preserveAspectRatio="none" version="1.1" viewBox="0 0 2025 559" zoomAndPan="magnify"><defs/><g><a href="#schema%3ABrand" target="_top" title="#schema%3ABrand" xlink:actuate="onRequest" xlink:href="#schema%3ABrand" xlink:show="new" xlink:title="#schema%3ABrand" xlink:type="simple"><g id="elem_schema_Brand"><rect codeLine="15" fill="#F1F1F1" height="50.5938" id="schema_Brand" rx="3.5" ry="3.5" style="stroke:#181818;stroke-width:0.5;" width="204" x="354" y="502"/><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="48" x="374" y="519.9951">Brand</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="422" y="519.9951"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="112" x="426" y="519.9951">(schema:Brand)</text><line style="stroke:#181818;stroke-width:0.5;" x1="355" x2="557" y1="528.2969" y2="528.2969"/><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="39" x="360" y="545.292">naam</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="399" y="545.292"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="5" x="403" y="545.292">:</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="408" y="545.292"> </text><text fill="#000000" font-family="sans-serif" font-size="14" font-style="italic" lengthAdjust="spacing" textLength="98" x="412" y="545.292">rdf:langString</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="510" y="545.292"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="38" x="514" y="545.292">[1..1]</text></g></a><a href="#prov%3AActivity" target="_top" title="#prov%3AActivity" xlink:actuate="onRequest" xlink:href="#prov%3AActivity" xlink:show="new" xlink:title="#prov%3AActivity" xlink:type="simple"><g id="elem_prov_Activity"><rect codeLine="18" fill="#F1F1F1" height="83.1875" id="prov_Activity" rx="3.5" ry="3.5" style="stroke:#181818;stroke-width:0.5;" width="289" x="467.5" y="166"/><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="76" x="520" y="183.9951">activiteit</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="596" y="183.9951"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="104" x="600" y="183.9951">(prov:Activity)</text><line style="stroke:#181818;stroke-width:0.5;" x1="468.5" x2="755.5" y1="192.2969" y2="192.2969"/><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="40" x="473.5" y="209.292">heeft</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="513.5" y="209.292"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="77" x="517.5" y="209.292">einddatum</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="594.5" y="209.292"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="5" x="598.5" y="209.292">:</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="603.5" y="209.292"> </text><text fill="#000000" font-family="sans-serif" font-size="14" font-style="italic" lengthAdjust="spacing" textLength="97" x="607.5" y="209.292">xsd:dateTime</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="704.5" y="209.292"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="38" x="708.5" y="209.292">[1..1]</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="40" x="473.5" y="225.5889">heeft</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="513.5" y="225.5889"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="93" x="517.5" y="225.5889">gegenereerd</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="610.5" y="225.5889"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="5" x="614.5" y="225.5889">:</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="619.5" y="225.5889"> </text><text fill="#000000" font-family="sans-serif" font-size="14" font-style="italic" lengthAdjust="spacing" textLength="18" x="623.5" y="225.5889">IRI</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="641.5" y="225.5889"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="38" x="645.5" y="225.5889">[0..1]</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="40" x="473.5" y="241.8857">heeft</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="513.5" y="241.8857"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="81" x="517.5" y="241.8857">startdatum</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="598.5" y="241.8857"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="5" x="602.5" y="241.8857">:</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="607.5" y="241.8857"> </text><text fill="#000000" font-family="sans-serif" font-size="14" font-style="italic" lengthAdjust="spacing" textLength="97" x="611.5" y="241.8857">xsd:dateTime</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="708.5" y="241.8857"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="38" x="712.5" y="241.8857">[1..1]</text></g></a><a href="#premis%3AEvent" target="_top" title="#premis%3AEvent" xlink:actuate="onRequest" xlink:href="#premis%3AEvent" xlink:show="new" xlink:title="#premis%3AEvent" xlink:type="simple"><g id="elem_premis_Event"><rect codeLine="17" fill="#F1F1F1" height="66.8906" id="premis_Event" rx="3.5" ry="3.5" style="stroke:#181818;stroke-width:0.5;" width="324" x="1096" y="7"/><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="96" x="1154.5" y="24.9951">gebeurtenis</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="1250.5" y="24.9951"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="107" x="1254.5" y="24.9951">(premis:Event)</text><line style="stroke:#181818;stroke-width:0.5;" x1="1097" x2="1419" y1="33.2969" y2="33.2969"/><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="40" x="1102" y="50.292">heeft</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="1142" y="50.292"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="79" x="1146" y="50.292">opmerking</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="1225" y="50.292"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="5" x="1229" y="50.292">:</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="1234" y="50.292"> </text><text fill="#000000" font-family="sans-serif" font-size="14" font-style="italic" lengthAdjust="spacing" textLength="69" x="1238" y="50.292">xsd:string</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="1307" y="50.292"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="38" x="1311" y="50.292">[0..1]</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="40" x="1102" y="66.5889">heeft</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="1142" y="66.5889"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="144" x="1146" y="66.5889">uitkomstopmerking</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="1290" y="66.5889"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="5" x="1294" y="66.5889">:</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="1299" y="66.5889"> </text><text fill="#000000" font-family="sans-serif" font-size="14" font-style="italic" lengthAdjust="spacing" textLength="69" x="1303" y="66.5889">xsd:string</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="1372" y="66.5889"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="38" x="1376" y="66.5889">[0..1]</text></g></a><a href="#premis%3AHardwareAgent" target="_top" title="#premis%3AHardwareAgent" xlink:actuate="onRequest" xlink:href="#premis%3AHardwareAgent" xlink:show="new" xlink:title="#premis%3AHardwareAgent" xlink:type="simple"><g id="elem_premis_HardwareAgent"><rect codeLine="19" fill="#F1F1F1" height="99.4844" id="premis_HardwareAgent" rx="3.5" ry="3.5" style="stroke:#181818;stroke-width:0.5;" width="314" x="236" y="326"/><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="76" x="239" y="343.9951">hardware</text><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="5" x="315" y="343.9951"> </text><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="47" x="320" y="343.9951">agent</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="367" y="343.9951"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="176" x="371" y="343.9951">(premis:HardwareAgent)</text><line style="stroke:#181818;stroke-width:0.5;" x1="237" x2="549" y1="352.2969" y2="352.2969"/><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="45" x="242" y="369.292">model</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="287" y="369.292"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="5" x="291" y="369.292">:</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="296" y="369.292"> </text><text fill="#000000" font-family="sans-serif" font-size="14" font-style="italic" lengthAdjust="spacing" textLength="69" x="300" y="369.292">xsd:string</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="369" y="369.292"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="38" x="373" y="369.292">[0..1]</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="39" x="242" y="385.5889">naam</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="281" y="385.5889"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="5" x="285" y="385.5889">:</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="290" y="385.5889"> </text><text fill="#000000" font-family="sans-serif" font-size="14" font-style="italic" lengthAdjust="spacing" textLength="98" x="294" y="385.5889">rdf:langString</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="392" y="385.5889"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="38" x="396" y="385.5889">[1..1]</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="95" x="242" y="401.8857">serienummer</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="337" y="401.8857"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="5" x="341" y="401.8857">:</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="346" y="401.8857"> </text><text fill="#000000" font-family="sans-serif" font-size="14" font-style="italic" lengthAdjust="spacing" textLength="69" x="350" y="401.8857">xsd:string</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="419" y="401.8857"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="38" x="423" y="401.8857">[0..1]</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="43" x="242" y="418.1826">versie</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="285" y="418.1826"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="5" x="289" y="418.1826">:</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="294" y="418.1826"> </text><text fill="#000000" font-family="sans-serif" font-size="14" font-style="italic" lengthAdjust="spacing" textLength="69" x="298" y="418.1826">xsd:string</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="367" y="418.1826"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="38" x="371" y="418.1826">[0..1]</text></g></a><a href="#premis%3AAgent" target="_top" title="#premis%3AAgent" xlink:actuate="onRequest" xlink:href="#premis%3AAgent" xlink:show="new" xlink:title="#premis%3AAgent" xlink:type="simple"><g id="elem_premis_Agent"><rect codeLine="27" fill="#F1F1F1" height="26.2969" id="premis_Agent" rx="3.5" ry="3.5" style="stroke:#181818;stroke-width:0.5;" width="166" x="622" y="514.5"/><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="47" x="625" y="532.4951">agent</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="672" y="532.4951"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="109" x="676" y="532.4951">(premis:Agent)</text></g></a><a href="#premis%3AObject" target="_top" title="#premis%3AObject" xlink:actuate="onRequest" xlink:href="#premis%3AObject" xlink:show="new" xlink:title="#premis%3AObject" xlink:type="simple"><g id="elem_premis_Object"><rect codeLine="21" fill="#F1F1F1" height="26.2969" id="premis_Object" rx="3.5" ry="3.5" style="stroke:#181818;stroke-width:0.5;" width="175" x="1493.5" y="194.5"/><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="51" x="1496.5" y="212.4951">object</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="1547.5" y="212.4951"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="114" x="1551.5" y="212.4951">(premis:Object)</text></g></a><a href="#prov%3AEntity" target="_top" title="#prov%3AEntity" xlink:actuate="onRequest" xlink:href="#prov%3AEntity" xlink:show="new" xlink:title="#prov%3AEntity" xlink:type="simple"><g id="elem_prov_Entity"><rect codeLine="22" fill="#F1F1F1" height="26.2969" id="prov_Entity" rx="3.5" ry="3.5" style="stroke:#181818;stroke-width:0.5;" width="164" x="1499" y="362.5"/><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="62" x="1502" y="380.4951">entiteit</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="1564" y="380.4951"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="92" x="1568" y="380.4951">(prov:Entity)</text></g></a><a href="../../organization/nl#org%3AOrganization" target="_top" title="../../organization/nl#org%3AOrganization" xlink:actuate="onRequest" xlink:href="../../organization/nl#org%3AOrganization" xlink:show="new" xlink:title="../../organization/nl#org%3AOrganization" xlink:type="simple"><g id="elem_org_Organization"><rect codeLine="23" fill="#F1F1F1" height="26.2969" id="org_Organization" rx="3.5" ry="3.5" style="stroke:#181818;stroke-width:0.5;" width="234" x="1036" y="362.5"/><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="93" x="1039" y="380.4951">organisatie</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="1132" y="380.4951"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="131" x="1136" y="380.4951">(org:Organization)</text></g></a><a href="../../organization/nl#schema%3APerson" target="_top" title="../../organization/nl#schema%3APerson" xlink:actuate="onRequest" xlink:href="../../organization/nl#schema%3APerson" xlink:show="new" xlink:title="../../organization/nl#schema%3APerson" xlink:type="simple"><g id="elem_schema_Person"><rect codeLine="24" fill="#F1F1F1" height="26.2969" id="schema_Person" rx="3.5" ry="3.5" style="stroke:#181818;stroke-width:0.5;" width="194" x="7" y="362.5"/><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="65" x="10" y="380.4951">persoon</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="75" y="380.4951"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="119" x="79" y="380.4951">(schema:Person)</text></g></a><a href="#schema%3AThing" target="_top" title="#schema%3AThing" xlink:actuate="onRequest" xlink:href="#schema%3AThing" xlink:show="new" xlink:title="#schema%3AThing" xlink:type="simple"><g id="elem_schema_Thing"><rect codeLine="25" fill="#F1F1F1" height="26.2969" id="schema_Thing" rx="3.5" ry="3.5" style="stroke:#181818;stroke-width:0.5;" width="156" x="26" y="514.5"/><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="36" x="29" y="532.4951">Ding</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="65" y="532.4951"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="110" x="69" y="532.4951">(schema:Thing)</text></g></a><a href="#premis%3ASoftwareAgent" target="_top" title="#premis%3ASoftwareAgent" xlink:actuate="onRequest" xlink:href="#premis%3ASoftwareAgent" xlink:show="new" xlink:title="#premis%3ASoftwareAgent" xlink:type="simple"><g id="elem_premis_SoftwareAgent"><rect codeLine="26" fill="#F1F1F1" height="99.4844" id="premis_SoftwareAgent" rx="3.5" ry="3.5" style="stroke:#181818;stroke-width:0.5;" width="309" x="585.5" y="326"/><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="73" x="588.5" y="343.9951">software</text><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="5" x="661.5" y="343.9951"> </text><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="47" x="666.5" y="343.9951">agent</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="713.5" y="343.9951"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="174" x="717.5" y="343.9951">(premis:SoftwareAgent)</text><line style="stroke:#181818;stroke-width:0.5;" x1="586.5" x2="893.5" y1="352.2969" y2="352.2969"/><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="45" x="591.5" y="369.292">model</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="636.5" y="369.292"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="5" x="640.5" y="369.292">:</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="645.5" y="369.292"> </text><text fill="#000000" font-family="sans-serif" font-size="14" font-style="italic" lengthAdjust="spacing" textLength="69" x="649.5" y="369.292">xsd:string</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="718.5" y="369.292"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="38" x="722.5" y="369.292">[0..1]</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="39" x="591.5" y="385.5889">naam</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="630.5" y="385.5889"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="5" x="634.5" y="385.5889">:</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="639.5" y="385.5889"> </text><text fill="#000000" font-family="sans-serif" font-size="14" font-style="italic" lengthAdjust="spacing" textLength="98" x="643.5" y="385.5889">rdf:langString</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="741.5" y="385.5889"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="38" x="745.5" y="385.5889">[1..1]</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="95" x="591.5" y="401.8857">serienummer</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="686.5" y="401.8857"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="5" x="690.5" y="401.8857">:</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="695.5" y="401.8857"> </text><text fill="#000000" font-family="sans-serif" font-size="14" font-style="italic" lengthAdjust="spacing" textLength="69" x="699.5" y="401.8857">xsd:string</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="768.5" y="401.8857"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="38" x="772.5" y="401.8857">[0..1]</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="43" x="591.5" y="418.1826">versie</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="634.5" y="418.1826"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="5" x="638.5" y="418.1826">:</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="643.5" y="418.1826"> </text><text fill="#000000" font-family="sans-serif" font-size="14" font-style="italic" lengthAdjust="spacing" textLength="69" x="647.5" y="418.1826">xsd:string</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="716.5" y="418.1826"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="38" x="720.5" y="418.1826">[0..1]</text></g></a><a href="#premis%3AOutcomeStatus" target="_top" title="#premis%3AOutcomeStatus" xlink:actuate="onRequest" xlink:href="#premis%3AOutcomeStatus" xlink:show="new" xlink:title="#premis%3AOutcomeStatus" xlink:type="simple"><g id="elem_premis_OutcomeStatus"><rect codeLine="28" fill="#F1F1F1" height="26.2969" id="premis_OutcomeStatus" rx="3.5" ry="3.5" style="stroke:#181818;stroke-width:0.5;" width="315" x="1703.5" y="194.5"/><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="128" x="1706.5" y="212.4951">uitkomststatus</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="1834.5" y="212.4951"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="177" x="1838.5" y="212.4951">(premis:OutcomeStatus)</text></g></a><g id="link_prov_Activity_org_Organization"><path codeLine="39" d="M743.997,249.002 C865.205,286.193 1031.4839,337.214 1107.9739,360.684 " fill="none" id="prov_Activity-to-org_Organization" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#454645" points="1113.71,362.444,1106.2793,355.9799,1108.93,360.9773,1103.9326,363.628,1113.71,362.444" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#000000" points="892.78,289.0331,884.995,283.5702,883.2708,289.1895,892.78,289.0331" style="stroke:#000000;stroke-width:1.0;"/><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="26" x="897" y="292.0669">was</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="923" y="292.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="68" x="927" y="292.0669">toegekend</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="995" y="292.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="24" x="999" y="292.0669">aan</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="1023" y="292.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="34" x="1027" y="292.0669">[1..1]</text></g><g id="link_prov_Activity_premis_HardwareAgent"><path codeLine="40" d="M467.131,242.232 C448.365,251.631 430.881,263.645 417,279 C405.421,291.808 400.3929,303.4862 397.1559,320.0632 " fill="none" id="prov_Activity-to-premis_HardwareAgent" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#454645" points="396.006,325.952,401.6567,317.8854,396.9643,321.0447,393.805,316.3522,396.006,325.952" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#000000" points="418.6571,291.2846,426.89,286.5232,422.519,282.5934,418.6571,291.2846" style="stroke:#000000;stroke-width:1.0;"/><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="26" x="431" y="292.0669">was</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="457" y="292.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="68" x="461" y="292.0669">toegekend</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="529" y="292.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="24" x="533" y="292.0669">aan</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="557" y="292.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="34" x="561" y="292.0669">[1..1]</text></g><g id="link_prov_Activity_premis_SoftwareAgent"><path codeLine="41" d="M601.889,249.422 C600.224,264.899 601.133,282.114 609,296 C615.47,307.419 619.7687,313.4648 629.8617,322.0678 " fill="none" id="prov_Activity-to-premis_SoftwareAgent" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#454645" points="634.428,325.96,630.1734,317.0775,630.6228,322.7165,624.9838,323.1659,634.428,325.96" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#000000" points="615.7967,292.2324,615.2891,282.7354,609.8038,284.8476,615.7967,292.2324" style="stroke:#000000;stroke-width:1.0;"/><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="26" x="623" y="292.0669">was</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="649" y="292.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="68" x="653" y="292.0669">toegekend</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="721" y="292.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="24" x="725" y="292.0669">aan</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="749" y="292.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="34" x="753" y="292.0669">[1..1]</text></g><g id="link_prov_Activity_schema_Person"><path codeLine="42" d="M467.49,216.842 C391.078,225.543 297.346,243.213 220,279 C175.492,299.593 137.846,337.0171 118.835,357.7971 " fill="none" id="prov_Activity-to-schema_Person" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#454645" points="114.785,362.224,123.8113,358.2837,118.16,358.5349,117.9088,352.8837,114.785,362.224" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#000000" points="220.3645,289.4405,229.8517,288.7749,227.6487,283.3256,220.3645,289.4405" style="stroke:#000000;stroke-width:1.0;"/><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="26" x="234" y="292.0669">was</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="260" y="292.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="68" x="264" y="292.0669">toegekend</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="332" y="292.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="24" x="336" y="292.0669">aan</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="360" y="292.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="34" x="364" y="292.0669">[1..1]</text></g><g id="link_premis_Event_prov_Activity"><path codeLine="45" d="M1126.37,74.018 C1087.87,83.597 1045.73,94.152 1007,104 C924.089,125.079 848.9305,144.536 774.2525,164.01 " fill="none" id="premis_Event-to-prov_Activity" style="stroke:#0000FF;stroke-width:1.0;stroke-dasharray:1.0,3.0;"/><polygon fill="none" points="756.835,168.552,775.7665,169.8158,772.7385,158.2041,756.835,168.552" style="stroke:#0000FF;stroke-width:1.0;"/></g><g id="link_premis_Event_org_Organization"><path codeLine="49" d="M1248.63,74.328 C1236.82,115.34 1215.68,187.597 1196,249 C1182.57,290.891 1167.2499,334.4797 1159.3199,356.7847 " fill="none" id="premis_Event-to-org_Organization" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#454645" points="1157.31,362.438,1164.0938,355.2979,1158.9849,357.7269,1156.556,352.618,1157.31,362.438" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#000000" points="1224.4926,212.3338,1230.0217,204.5956,1224.4173,202.8235,1224.4926,212.3338" style="stroke:#000000;stroke-width:1.0;"/><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="114" x="1235" y="212.0669">geimplementeerd</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="1349" y="212.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="29" x="1353" y="212.0669">door</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="1382" y="212.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="34" x="1386" y="212.0669">[1..1]</text></g><g id="link_premis_Event_premis_HardwareAgent"><path codeLine="50" d="M1095.53,52.91 C866.858,70.72 462.893,109.093 328,166 C248.558,199.514 134.907,225.119 184,296 C191.862,307.351 205.9987,316.1569 230.3027,326.2859 " fill="none" id="premis_Event-to-premis_HardwareAgent" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#454645" points="235.841,328.594,229.0724,321.4396,231.2258,326.6705,225.9948,328.824,235.841,328.594" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#000000" points="328.2323,209.0728,337.7426,209.1501,335.9717,203.5453,328.2323,209.0728" style="stroke:#000000;stroke-width:1.0;"/><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="70" x="342" y="212.0669">instrument</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="412" y="212.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="33" x="416" y="212.0669">[0..*]</text></g><g id="link_premis_Event_premis_Object"><path codeLine="51" d="M1420.12,60.343 C1454.3,69.67 1488.58,83.507 1517,104 C1549.33,127.313 1566.8694,166.8469 1574.8194,188.5879 " fill="none" id="premis_Event-to-premis_Object" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#454645" points="1576.88,194.223,1577.5459,184.3967,1575.1629,189.5271,1570.0324,187.1441,1576.88,194.223" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#000000" points="1554.8493,123.3239,1549.7615,115.2886,1546.0102,119.8138,1554.8493,123.3239" style="stroke:#000000;stroke-width:1.0;"/><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="34" x="1560" y="117.0669">heeft</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="1594" y="117.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="29" x="1598" y="117.0669">bron</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="1627" y="117.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="34" x="1631" y="117.0669">[0..1]</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="57" x="1560" y="132.1997">resultaat</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="1617" y="132.1997"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="34" x="1621" y="132.1997">[0..1]</text></g><g id="link_premis_Object_premis_Event"><path codeLine="68" d="M1550.1,194.425 C1527.14,185.745 1494.92,174.179 1466,166 C1405.18,148.802 1379.99,170.442 1327,136 C1303.84,120.944 1288.7711,100.4334 1276.9611,79.6204 " fill="none" id="premis_Object-to-premis_Event" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#454645" points="1274,74.402,1274.9627,84.2037,1276.4676,78.7507,1281.9206,80.2556,1274,74.402" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#000000" points="1327.3906,118.129,1334.5903,124.3431,1336.8679,118.9245,1327.3906,118.129" style="stroke:#000000;stroke-width:1.0;"/><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="10" x="1341" y="124.5669">is</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="1351" y="124.5669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="82" x="1355" y="124.5669">gegenereerd</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="1437" y="124.5669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="29" x="1441" y="124.5669">door</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="1470" y="124.5669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="34" x="1474" y="124.5669">[0..1]</text></g><g id="link_premis_Event_premis_OutcomeStatus"><path codeLine="52" d="M1420.14,52.507 C1498.38,61.161 1592.69,76.577 1674,104 C1741.01,126.597 1807.1768,169.1313 1838.9668,191.0013 " fill="none" id="premis_Event-to-premis_OutcomeStatus" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#454645" points="1843.91,194.402,1838.7623,186.0055,1839.7907,191.5681,1834.2281,192.5964,1843.91,194.402" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#000000" points="1752.7472,121.6362,1745.0821,116.0061,1743.2368,121.5868,1752.7472,121.6362" style="stroke:#000000;stroke-width:1.0;"/><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="34" x="1757" y="124.5669">heeft</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="1791" y="124.5669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="56" x="1795" y="124.5669">uitkomst</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="1851" y="124.5669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="34" x="1855" y="124.5669">[0..1]</text></g><g id="link_premis_Event_premis_SoftwareAgent"><path codeLine="53" d="M1157.75,74.062 C1112.79,93.715 1063.2,123.383 1033,166 C999.118,213.811 1050,252.265 1011,296 C981.089,329.542 943.6122,347.6038 900.3872,358.9248 " fill="none" id="premis_Event-to-premis_SoftwareAgent" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#454645" points="894.583,360.445,904.3028,362.0342,899.4199,359.1782,902.2759,354.2952,894.583,360.445" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#000000" points="1034.6481,211.2765,1042.8925,206.5351,1038.531,202.5947,1034.6481,211.2765" style="stroke:#000000;stroke-width:1.0;"/><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="69" x="1047" y="212.0669">uitgevoerd</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="1116" y="212.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="29" x="1120" y="212.0669">door</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="1149" y="212.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="34" x="1153" y="212.0669">[0..1]</text></g><g id="link_premis_HardwareAgent_premis_Agent"><path codeLine="56" d="M473.88,425.101 C501.674,440.947 533.279,458.039 563,472 C598.373,488.6161 623.3241,498.2675 652.4101,508.4889 " fill="none" id="premis_HardwareAgent-to-premis_Agent" style="stroke:#0000FF;stroke-width:1.0;stroke-dasharray:1.0,3.0;"/><polygon fill="none" points="669.392,514.4567,654.3993,502.8283,650.4208,514.1496,669.392,514.4567" style="stroke:#0000FF;stroke-width:1.0;"/></g><g id="link_premis_HardwareAgent_schema_Brand"><path codeLine="63" d="M410.389,425.458 C416.021,440.513 422.499,457.0513 429,472 C433.295,481.8768 435.7575,487.1752 440.4105,496.4242 " fill="none" id="premis_HardwareAgent-to-schema_Brand" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#454645" points="443.107,501.7841,442.6356,491.9465,440.8599,497.3175,435.489,495.5418,443.107,501.7841" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#000000" points="435.9481,468.1713,435.1307,458.6959,429.7173,460.986,435.9481,468.1713" style="stroke:#000000;stroke-width:1.0;"/><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="33" x="443" y="468.0669">merk</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="476" y="468.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="34" x="480" y="468.0669">[0..1]</text></g><g id="link_premis_Object_prov_Entity"><path codeLine="66" d="M1581,220.706 C1581,251.405 1581,313.558 1581,344.276 " fill="none" id="premis_Object-to-prov_Entity" style="stroke:#0000FF;stroke-width:1.0;stroke-dasharray:1.0,3.0;"/><polygon fill="none" points="1581,362.276,1587,344.276,1575,344.276,1581,362.276" style="stroke:#0000FF;stroke-width:1.0;"/></g><g id="link_schema_Person_schema_Thing"><path codeLine="72" d="M104,388.522 C104,416.608 104,468.2785 104,496.4212 " fill="none" id="schema_Person-to-schema_Thing" style="stroke:#0000FF;stroke-width:1.0;stroke-dasharray:1.0,3.0;"/><polygon fill="none" points="104,514.4212,110,496.4212,98,496.4212,104,514.4212" style="stroke:#0000FF;stroke-width:1.0;"/></g><g id="link_premis_SoftwareAgent_premis_Agent"><path codeLine="75" d="M728.637,425.201 C721.291,456.6813 716.3843,477.7108 711.9043,496.9099 " fill="none" id="premis_SoftwareAgent-to-premis_Agent" style="stroke:#0000FF;stroke-width:1.0;stroke-dasharray:1.0,3.0;"/><polygon fill="none" points="707.814,514.439,717.7473,498.2733,706.0613,495.5465,707.814,514.439" style="stroke:#0000FF;stroke-width:1.0;"/></g><g id="link_premis_SoftwareAgent_schema_Brand"><path codeLine="82" d="M647.793,425.201 C599.204,450.864 547.0134,478.4294 507.7304,499.1775 " fill="none" id="premis_SoftwareAgent-to-schema_Brand" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#454645" points="502.425,501.9797,512.2513,501.3134,506.8462,499.6446,508.5151,494.2395,502.425,501.9797" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#000000" points="590.5788,465.9015,599.9494,464.276,597.2043,459.0785,590.5788,465.9015" style="stroke:#000000;stroke-width:1.0;"/><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="33" x="604" y="468.0669">merk</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="637" y="468.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="34" x="641" y="468.0669">[0..1]</text></g></g></svg>
  </div>
</div>

## Naamruimten

| Prefix | URI      |
| :----- | :------- |
| brick     | [https://brickschema.org/schema/Brick#](https://brickschema.org/schema/Brick#) |
| csvw     | [http://www.w3.org/ns/csvw#](http://www.w3.org/ns/csvw#) |
| dc     | [http://purl.org/dc/elements/1.1/](http://purl.org/dc/elements/1.1/) |
| dcam     | [http://purl.org/dc/dcam/](http://purl.org/dc/dcam/) |
| dcat     | [http://www.w3.org/ns/dcat#](http://www.w3.org/ns/dcat#) |
| dcmitype     | [http://purl.org/dc/dcmitype/](http://purl.org/dc/dcmitype/) |
| dct     | [http://purl.org/dc/terms/](http://purl.org/dc/terms/) |
| doap     | [http://usefulinc.com/ns/doap#](http://usefulinc.com/ns/doap#) |
| evtAgRole     | [http://id.loc.gov/vocabulary/preservation/eventRelatedAgentRole/](http://id.loc.gov/vocabulary/preservation/eventRelatedAgentRole/) |
| evtObjRole     | [http://id.loc.gov/vocabulary/preservation/eventRelatedObjectRole/](http://id.loc.gov/vocabulary/preservation/eventRelatedObjectRole/) |
| evtOutcome     | [http://id.loc.gov/vocabulary/preservation/eventOutcome/](http://id.loc.gov/vocabulary/preservation/eventOutcome/) |
| foaf     | [http://xmlns.com/foaf/0.1/](http://xmlns.com/foaf/0.1/) |
| geo     | [http://www.opengis.net/ont/geosparql#](http://www.opengis.net/ont/geosparql#) |
| haEvt     | [https://data.hetarchief.be/ns/event/](https://data.hetarchief.be/ns/event/) |
| odrl     | [http://www.w3.org/ns/odrl/2/](http://www.w3.org/ns/odrl/2/) |
| org     | [http://www.w3.org/ns/org#](http://www.w3.org/ns/org#) |
| owl     | [http://www.w3.org/2002/07/owl#](http://www.w3.org/2002/07/owl#) |
| pav     | [http://purl.org/pav/](http://purl.org/pav/) |
| premis     | [http://www.loc.gov/premis/rdf/v3/](http://www.loc.gov/premis/rdf/v3/) |
| prof     | [http://www.w3.org/ns/dx/prof/](http://www.w3.org/ns/dx/prof/) |
| prov     | [http://www.w3.org/ns/prov#](http://www.w3.org/ns/prov#) |
| qb     | [http://purl.org/linked-data/cube#](http://purl.org/linked-data/cube#) |
| rdf     | [http://www.w3.org/1999/02/22-rdf-syntax-ns#](http://www.w3.org/1999/02/22-rdf-syntax-ns#) |
| rdfs     | [http://www.w3.org/2000/01/rdf-schema#](http://www.w3.org/2000/01/rdf-schema#) |
| schema     | [https://schema.org/](https://schema.org/) |
| sh     | [http://www.w3.org/ns/shacl#](http://www.w3.org/ns/shacl#) |
| skos     | [http://www.w3.org/2004/02/skos/core#](http://www.w3.org/2004/02/skos/core#) |
| sosa     | [http://www.w3.org/ns/sosa/](http://www.w3.org/ns/sosa/) |
| ssn     | [http://www.w3.org/ns/ssn/](http://www.w3.org/ns/ssn/) |
| time     | [http://www.w3.org/2006/time#](http://www.w3.org/2006/time#) |
| vann     | [http://purl.org/vocab/vann/](http://purl.org/vocab/vann/) |
| void     | [http://rdfs.org/ns/void#](http://rdfs.org/ns/void#) |
| wgs     | [https://www.w3.org/2003/01/geo/wgs84_pos#](https://www.w3.org/2003/01/geo/wgs84_pos#) |
| xml     | [http://www.w3.org/XML/1998/namespace](http://www.w3.org/XML/1998/namespace) |
| xsd     | [http://www.w3.org/2001/XMLSchema#](http://www.w3.org/2001/XMLSchema#) |

## Klassen & Eigenschappen

**Klassen:** 
 [Brand](#schema%3ABrand) |  [activiteit](#prov%3AActivity) |  [gebeurtenis](#premis%3AEvent) |  [hardware agent](#premis%3AHardwareAgent) |  [object](#premis%3AObject) |  [organisatie <svg class="svg-external-link" viewBox="0 0 24 24" aria-labelledby="svg-external-link-title"><use xlink:href="#svg-external-link"></use></svg>](../../organization/nl#org%3AOrganization){:target="_blank"} |  [persoon <svg class="svg-external-link" viewBox="0 0 24 24" aria-labelledby="svg-external-link-title"><use xlink:href="#svg-external-link"></use></svg>](../../organization/nl#schema%3APerson){:target="_blank"} |  [software agent](#premis%3ASoftwareAgent) |  [uitkomststatus](#premis%3AOutcomeStatus)
## <a id="schema%3ABrand"></a>Brand <small>[(schema:Brand)](https://schema.org/Brand)</small>




| Eigenschap | Beschrijving | Kardinaliteit | Datatype |
| :------ | :---------- | :---------- | :------- |
| <a id='schema%3Aname'></a>naam <br> <small>[(schema:name)](https://schema.org/name)</small> | De naam van het item. | `1..1` | [`rdf:langString`](http://www.w3.org/1999/02/22-rdf-syntax-ns#langString)  |

## <a id="prov%3AActivity"></a>activiteit <small>[(prov:Activity)](http://www.w3.org/ns/prov#Activity)</small>


**Subklassen:** 
[gebeurtenis](#premis%3AEvent)

Een activiteit is iets dat zich gedurende een bepaalde periode voordoet en op/met entiteiten handelt. Het kan onder meer volgende zaken inhouden: consumeren, verwerken, transformeren, wijzigen, verplaatsen, gebruiken of genereren van entiteiten.

| Eigenschap | Beschrijving | Kardinaliteit | Datatype |
| :------ | :---------- | :---------- | :------- |
| <a id='prov%3AendedAtTime'></a>heeft einddatum <br> <small>[(prov:endedAtTime)](http://www.w3.org/ns/prov#endedAtTime)</small> | De einddatum van de activiteit. | `1..1` | [`xsd:dateTime`](http://www.w3.org/2001/XMLSchema#dateTime)  |
| <a id='prov%3Agenerated'></a>heeft gegenereerd <br> <small>[(prov:generated)](http://www.w3.org/ns/prov#generated)</small> | Het gegenereerde object. | `0..1` | [`IRI`](https://www.rfc-editor.org/rfc/rfc3987.txt)  |
| <a id='prov%3AstartedAtTime'></a>heeft startdatum <br> <small>[(prov:startedAtTime)](http://www.w3.org/ns/prov#startedAtTime)</small> | De startdatum van de activiteit. | `1..1` | [`xsd:dateTime`](http://www.w3.org/2001/XMLSchema#dateTime)  |
| <a id='prov%3AwasAttributedTo'></a>was toegekend aan <br> <small>[(prov:wasAttributedTo)](http://www.w3.org/ns/prov#wasAttributedTo)</small> | De agent die toegekend is aan de activiteit. | `1..1` | [persoon <svg class="svg-external-link" viewBox="0 0 24 24" aria-labelledby="svg-external-link-title"><use xlink:href="#svg-external-link"></use></svg>](../../organization/nl#schema%3APerson){:target="_blank"} _of_ [organisatie <svg class="svg-external-link" viewBox="0 0 24 24" aria-labelledby="svg-external-link-title"><use xlink:href="#svg-external-link"></use></svg>](../../organization/nl#org%3AOrganization){:target="_blank"} _of_ [software agent](#premis%3ASoftwareAgent) _of_ [hardware agent](#premis%3AHardwareAgent)  |

## <a id="premis%3AEvent"></a>gebeurtenis <small>[(premis:Event)](http://www.loc.gov/premis/rdf/v3/Event)</small>


**Subklasse van:** 
[activiteit](#prov%3AActivity)

Handeling uitgevoerd binnen of buiten het archief die het vermogen beïnvloedt om objecten op lange termijn te bewaren.

| Eigenschap | Beschrijving | Kardinaliteit | Datatype |
| :------ | :---------- | :---------- | :------- |
| <a id='evtAgRole%3Aimp'></a>geimplementeerd door <br> <small>[(evtAgRole:imp)](http://id.loc.gov/vocabulary/preservation/eventRelatedAgentRole/imp)</small> | De organisatie die de gebeurtenis (Event) heeft geimplementeerd. | `1..1` | [organisatie <svg class="svg-external-link" viewBox="0 0 24 24" aria-labelledby="svg-external-link-title"><use xlink:href="#svg-external-link"></use></svg>](../../organization/nl#org%3AOrganization){:target="_blank"}  |
| <a id='evtObjRole%3Asou'></a>heeft bron <br> <small>[(evtObjRole:sou)](http://id.loc.gov/vocabulary/preservation/eventRelatedObjectRole/sou)</small> | Het object dat als bron gebruikt is voor de gebeurtenis (Event). | `0..1` | [object](#premis%3AObject)  |
| <a id='premis%3Anote'></a>heeft opmerking <br> <small>[(premis:note)](http://www.loc.gov/premis/rdf/v3/note)</small> | Een opmerking over de gebeurtenis (Event). | `0..1` | [`xsd:string`](http://www.w3.org/2001/XMLSchema#string)  |
| <a id='premis%3Aoutcome'></a>heeft uitkomst <br> <small>[(premis:outcome)](http://www.loc.gov/premis/rdf/v3/outcome)</small> | De uitkomststatus van de gebeurtenis (Event). | `0..1` | [uitkomststatus](#premis%3AOutcomeStatus) <br>_Mogelijke waarden: [`evtOutcome:fai`](http://id.loc.gov/vocabulary/preservation/eventOutcome/fai), [`evtOutcome:suc`](http://id.loc.gov/vocabulary/preservation/eventOutcome/suc), [`evtOutcome:war`](http://id.loc.gov/vocabulary/preservation/eventOutcome/war)_ |
| <a id='premis%3AoutcomeNote'></a>heeft uitkomstopmerking <br> <small>[(premis:outcomeNote)](http://www.loc.gov/premis/rdf/v3/outcomeNote)</small> | Een opmerking over de uitkomst van de gebeurtenis (Event). | `0..1` | [`xsd:string`](http://www.w3.org/2001/XMLSchema#string)  |
| <a id='schema%3Ainstrument'></a>instrument <br> <small>[(schema:instrument)](https://schema.org/instrument)</small> | De hardware die gebruikt is voor het uitvoeren van de gebeurtenis (Event). | `0..*` | [hardware agent](#premis%3AHardwareAgent)  |
| <a id='evtObjRole%3Aout'></a>resultaat <br> <small>[(evtObjRole:out)](http://id.loc.gov/vocabulary/preservation/eventRelatedObjectRole/out)</small> | Het object dat door de gebeurtenis (Event) gegenereerd is. | `0..1` | [object](#premis%3AObject)  |
| <a id='evtAgRole%3Aexe'></a>uitgevoerd door <br> <small>[(evtAgRole:exe)](http://id.loc.gov/vocabulary/preservation/eventRelatedAgentRole/exe)</small> | De software die de gebeurtenis (Event) heeft uitgevoerd. | `0..1` | [software agent](#premis%3ASoftwareAgent)  |

_Eigenschappen van [activiteit](#prov%3AActivity):_  [heeft einddatum](#prov%3AendedAtTime),  [heeft gegenereerd](#prov%3Agenerated),  [heeft startdatum](#prov%3AstartedAtTime),  [was toegekend aan](#prov%3AwasAttributedTo)

## <a id="premis%3AHardwareAgent"></a>hardware agent <small>[(premis:HardwareAgent)](http://www.loc.gov/premis/rdf/v3/HardwareAgent)</small>


**Subklasse van:** 
[agent](#premis%3AAgent)

Hardwareagent (bv. een computer) die gekoppeld is aan één of meer gebeurtenissen (Events) en/of rechtenuitdrukking(en) geassocieerd met een digitaal object.

| Eigenschap | Beschrijving | Kardinaliteit | Datatype |
| :------ | :---------- | :---------- | :------- |
| <a id='schema%3Abrand'></a>merk <br> <small>[(schema:brand)](https://schema.org/brand)</small> | Het specifieke merk van de agent. | `0..1` | [Brand](#schema%3ABrand)  |
| <a id='schema%3Amodel'></a>model <br> <small>[(schema:model)](https://schema.org/model)</small> | Het specifieke model van de agent. | `0..1` | [`xsd:string`](http://www.w3.org/2001/XMLSchema#string)  |
| <a id='schema%3Aname'></a>naam <br> <small>[(schema:name)](https://schema.org/name)</small> | De naam van het item. | `1..1` | [`rdf:langString`](http://www.w3.org/1999/02/22-rdf-syntax-ns#langString)  |
| <a id='schema%3AserialNumber'></a>serienummer <br> <small>[(schema:serialNumber)](https://schema.org/serialNumber)</small> | Het serienummer of een alfanumerieke identificatie van een bepaald middel. | `0..1` | [`xsd:string`](http://www.w3.org/2001/XMLSchema#string)  |
| <a id='schema%3Aversion'></a>versie <br> <small>[(schema:version)](https://schema.org/version)</small> | Het versienummer of versienaam van de agent. | `0..1` | [`xsd:string`](http://www.w3.org/2001/XMLSchema#string)  |



## <a id="premis%3AObject"></a>object <small>[(premis:Object)](http://www.loc.gov/premis/rdf/v3/Object)</small>


**Subklasse van:** 
[entiteit](#prov%3AEntity)

**Subklassen:** 
[bestand](#premis%3AFile)
, [intellectuele entiteit](#premis%3AIntellectualEntity)
, [representatie](#premis%3ARepresentation)

Discrete eenheid van informatie die digitaal moet worden bewaard. Subklassen van Object zijn Intellectual Entity (intellectuele entiteit), Representation (voorstelling/weergave), File (bestand) en Bitstream (bitstream).

| Eigenschap | Beschrijving | Kardinaliteit | Datatype |
| :------ | :---------- | :---------- | :------- |
| <a id='prov%3AwasGeneratedBy'></a>is gegenereerd door <br> <small>[(prov:wasGeneratedBy)](http://www.w3.org/ns/prov#wasGeneratedBy)</small> | De tijd waarop het object volledig is aangemaakt en beschikbaar is voor gebruik. | `0..1` | [gebeurtenis](#premis%3AEvent)  |



## <a id="premis%3ASoftwareAgent"></a>software agent <small>[(premis:SoftwareAgent)](http://www.loc.gov/premis/rdf/v3/SoftwareAgent)</small>


**Subklasse van:** 
[agent](#premis%3AAgent)

Softwareagent (bv. een computerprogramma) die gekoppeld is aan één of meer gebeurtenissen (Events) en/of rechtenuitdrukking(en) geassocieerd met een digitaal object.

| Eigenschap | Beschrijving | Kardinaliteit | Datatype |
| :------ | :---------- | :---------- | :------- |
| <a id='schema%3Abrand'></a>merk <br> <small>[(schema:brand)](https://schema.org/brand)</small> | Het specifieke merk van de agent. | `0..1` | [Brand](#schema%3ABrand)  |
| <a id='schema%3Amodel'></a>model <br> <small>[(schema:model)](https://schema.org/model)</small> | Het specifieke model van de agent. | `0..1` | [`xsd:string`](http://www.w3.org/2001/XMLSchema#string)  |
| <a id='schema%3Aname'></a>naam <br> <small>[(schema:name)](https://schema.org/name)</small> | De naam van het item. | `1..1` | [`rdf:langString`](http://www.w3.org/1999/02/22-rdf-syntax-ns#langString)  |
| <a id='schema%3AserialNumber'></a>serienummer <br> <small>[(schema:serialNumber)](https://schema.org/serialNumber)</small> | Het serienummer of een alfanumerieke identificatie van een bepaald middel. | `0..1` | [`xsd:string`](http://www.w3.org/2001/XMLSchema#string)  |
| <a id='schema%3Aversion'></a>versie <br> <small>[(schema:version)](https://schema.org/version)</small> | Het versienummer of versienaam van de agent. | `0..1` | [`xsd:string`](http://www.w3.org/2001/XMLSchema#string)  |



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
