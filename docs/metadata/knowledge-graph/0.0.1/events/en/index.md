---
layout: "default"
title: "Data model Events"
parent: "Knowledge Graph"
nav_order: 1
nav_exclude: False
---
<svg xmlns="http://www.w3.org/2000/svg" style="display: none;"><symbol id="svg-external-link" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-external-link"><title id="svg-external-link-title">(external link)</title><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line> </symbol></svg>

Data model Events
====================

**Version:** 0.0.1

**Previous version:** 

**Created:** 2022-06-08

**Last modified:** 2023-01-12

**SHACL file:** [events.shacl.ttl](events.shacl.ttl)

**Other languages:**
[nl](../nl)
, [fr](../fr)

**Authors:**
[Lennert Van de Velde](mailto:lennert.vandevelde@meemoo.be)
, [Milan Valadou](mailto:milan.valadou@meemoo.be)
, [Miel Vander Sande](mailto:miel.vandersande@meemoo.be)


Data model to describe events.

<div class="wrap">
  <div class="zoom">
  <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" contentStyleType="text/css" preserveAspectRatio="none" version="1.1" viewBox="0 0 1928 559" zoomAndPan="magnify"><defs/><g><a href="#schema%3ABrand" target="_top" title="#schema%3ABrand" xlink:actuate="onRequest" xlink:href="#schema%3ABrand" xlink:show="new" xlink:title="#schema%3ABrand" xlink:type="simple"><g id="elem_schema_Brand"><rect codeLine="15" fill="#F1F1F1" height="50.5938" id="schema_Brand" rx="3.5" ry="3.5" style="stroke:#181818;stroke-width:0.5;" width="196" x="313.5" y="502"/><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="46" x="331" y="519.9951">Brand</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="377" y="519.9951"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="111" x="381" y="519.9951">(schema:Brand)</text><line style="stroke:#181818;stroke-width:0.5;" x1="314.5" x2="508.5" y1="528.2969" y2="528.2969"/><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="39" x="319.5" y="545.292">name</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="358.5" y="545.292"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="5" x="362.5" y="545.292">:</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="367.5" y="545.292"> </text><text fill="#000000" font-family="sans-serif" font-size="14" font-style="italic" lengthAdjust="spacing" textLength="92" x="371.5" y="545.292">rdf:langString</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="463.5" y="545.292"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="36" x="467.5" y="545.292">[1..1]</text></g></a><a href="#prov%3AActivity" target="_top" title="#prov%3AActivity" xlink:actuate="onRequest" xlink:href="#prov%3AActivity" xlink:show="new" xlink:title="#prov%3AActivity" xlink:type="simple"><g id="elem_prov_Activity"><rect codeLine="18" fill="#F1F1F1" height="83.1875" id="prov_Activity" rx="3.5" ry="3.5" style="stroke:#181818;stroke-width:0.5;" width="254" x="471.5" y="166"/><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="58" x="521.5" y="183.9951">Activity</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="579.5" y="183.9951"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="92" x="583.5" y="183.9951">(prov:Activity)</text><line style="stroke:#181818;stroke-width:0.5;" x1="472.5" x2="724.5" y1="192.2969" y2="192.2969"/><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="25" x="477.5" y="209.292">has</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="502.5" y="209.292"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="27" x="506.5" y="209.292">end</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="533.5" y="209.292"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="31" x="537.5" y="209.292">date</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="568.5" y="209.292"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="5" x="572.5" y="209.292">:</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="577.5" y="209.292"> </text><text fill="#000000" font-family="sans-serif" font-size="14" font-style="italic" lengthAdjust="spacing" textLength="94" x="581.5" y="209.292">xsd:dateTime</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="675.5" y="209.292"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="36" x="679.5" y="209.292">[1..1]</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="25" x="477.5" y="225.5889">has</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="502.5" y="225.5889"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="72" x="506.5" y="225.5889">generated</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="578.5" y="225.5889"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="5" x="582.5" y="225.5889">:</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="587.5" y="225.5889"> </text><text fill="#000000" font-family="sans-serif" font-size="14" font-style="italic" lengthAdjust="spacing" textLength="16" x="591.5" y="225.5889">IRI</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="607.5" y="225.5889"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="36" x="611.5" y="225.5889">[0..1]</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="25" x="477.5" y="241.8857">has</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="502.5" y="241.8857"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="31" x="506.5" y="241.8857">start</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="537.5" y="241.8857"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="31" x="541.5" y="241.8857">date</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="572.5" y="241.8857"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="5" x="576.5" y="241.8857">:</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="581.5" y="241.8857"> </text><text fill="#000000" font-family="sans-serif" font-size="14" font-style="italic" lengthAdjust="spacing" textLength="94" x="585.5" y="241.8857">xsd:dateTime</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="679.5" y="241.8857"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="36" x="683.5" y="241.8857">[1..1]</text></g></a><a href="#premis%3AEvent" target="_top" title="#premis%3AEvent" xlink:actuate="onRequest" xlink:href="#premis%3AEvent" xlink:show="new" xlink:title="#premis%3AEvent" xlink:type="simple"><g id="elem_premis_Event"><rect codeLine="17" fill="#F1F1F1" height="66.8906" id="premis_Event" rx="3.5" ry="3.5" style="stroke:#181818;stroke-width:0.5;" width="260" x="1090.5" y="7"/><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="44" x="1146" y="24.9951">Event</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="1190" y="24.9951"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="101" x="1194" y="24.9951">(premis:Event)</text><line style="stroke:#181818;stroke-width:0.5;" x1="1091.5" x2="1349.5" y1="33.2969" y2="33.2969"/><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="25" x="1096.5" y="50.292">has</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="1121.5" y="50.292"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="32" x="1125.5" y="50.292">note</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="1157.5" y="50.292"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="5" x="1161.5" y="50.292">:</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="1166.5" y="50.292"> </text><text fill="#000000" font-family="sans-serif" font-size="14" font-style="italic" lengthAdjust="spacing" textLength="68" x="1170.5" y="50.292">xsd:string</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="1238.5" y="50.292"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="36" x="1242.5" y="50.292">[0..1]</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="25" x="1096.5" y="66.5889">has</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="1121.5" y="66.5889"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="62" x="1125.5" y="66.5889">outcome</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="1187.5" y="66.5889"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="32" x="1191.5" y="66.5889">note</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="1223.5" y="66.5889"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="5" x="1227.5" y="66.5889">:</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="1232.5" y="66.5889"> </text><text fill="#000000" font-family="sans-serif" font-size="14" font-style="italic" lengthAdjust="spacing" textLength="68" x="1236.5" y="66.5889">xsd:string</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="1304.5" y="66.5889"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="36" x="1308.5" y="66.5889">[0..1]</text></g></a><a href="#premis%3AHardwareAgent" target="_top" title="#premis%3AHardwareAgent" xlink:actuate="onRequest" xlink:href="#premis%3AHardwareAgent" xlink:show="new" xlink:title="#premis%3AHardwareAgent" xlink:type="simple"><g id="elem_premis_HardwareAgent"><rect codeLine="19" fill="#F1F1F1" height="99.4844" id="premis_HardwareAgent" rx="3.5" ry="3.5" style="stroke:#181818;stroke-width:0.5;" width="305" x="227" y="326"/><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="77" x="230" y="343.9951">Hardware</text><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="5" x="307" y="343.9951"> </text><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="45" x="312" y="343.9951">agent</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="357" y="343.9951"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="168" x="361" y="343.9951">(premis:HardwareAgent)</text><line style="stroke:#181818;stroke-width:0.5;" x1="228" x2="531" y1="352.2969" y2="352.2969"/><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="43" x="233" y="369.292">model</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="276" y="369.292"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="5" x="280" y="369.292">:</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="285" y="369.292"> </text><text fill="#000000" font-family="sans-serif" font-size="14" font-style="italic" lengthAdjust="spacing" textLength="68" x="289" y="369.292">xsd:string</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="357" y="369.292"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="36" x="361" y="369.292">[0..1]</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="39" x="233" y="385.5889">name</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="272" y="385.5889"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="5" x="276" y="385.5889">:</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="281" y="385.5889"> </text><text fill="#000000" font-family="sans-serif" font-size="14" font-style="italic" lengthAdjust="spacing" textLength="92" x="285" y="385.5889">rdf:langString</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="377" y="385.5889"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="36" x="381" y="385.5889">[1..1]</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="91" x="233" y="401.8857">serialNumber</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="324" y="401.8857"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="5" x="328" y="401.8857">:</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="333" y="401.8857"> </text><text fill="#000000" font-family="sans-serif" font-size="14" font-style="italic" lengthAdjust="spacing" textLength="68" x="337" y="401.8857">xsd:string</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="405" y="401.8857"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="36" x="409" y="401.8857">[0..1]</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="50" x="233" y="418.1826">version</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="283" y="418.1826"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="5" x="287" y="418.1826">:</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="292" y="418.1826"> </text><text fill="#000000" font-family="sans-serif" font-size="14" font-style="italic" lengthAdjust="spacing" textLength="68" x="296" y="418.1826">xsd:string</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="364" y="418.1826"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="36" x="368" y="418.1826">[0..1]</text></g></a><a href="#premis%3AAgent" target="_top" title="#premis%3AAgent" xlink:actuate="onRequest" xlink:href="#premis%3AAgent" xlink:show="new" xlink:title="#premis%3AAgent" xlink:type="simple"><g id="elem_premis_Agent"><rect codeLine="28" fill="#F1F1F1" height="26.2969" id="premis_Agent" rx="3.5" ry="3.5" style="stroke:#181818;stroke-width:0.5;" width="160" x="601.5" y="514.5"/><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="47" x="604.5" y="532.4951">Agent</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="651.5" y="532.4951"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="103" x="655.5" y="532.4951">(premis:Agent)</text></g></a><a href="#premis%3AObject" target="_top" title="#premis%3AObject" xlink:actuate="onRequest" xlink:href="#premis%3AObject" xlink:show="new" xlink:title="#premis%3AObject" xlink:type="simple"><g id="elem_premis_Object"><rect codeLine="21" fill="#F1F1F1" height="26.2969" id="premis_Object" rx="3.5" ry="3.5" style="stroke:#181818;stroke-width:0.5;" width="168" x="1412.5" y="194.5"/><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="51" x="1415.5" y="212.4951">Object</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="1466.5" y="212.4951"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="107" x="1470.5" y="212.4951">(premis:Object)</text></g></a><a href="#prov%3AEntity" target="_top" title="#prov%3AEntity" xlink:actuate="onRequest" xlink:href="#prov%3AEntity" xlink:show="new" xlink:title="#prov%3AEntity" xlink:type="simple"><g id="elem_prov_Entity"><rect codeLine="22" fill="#F1F1F1" height="26.2969" id="prov_Entity" rx="3.5" ry="3.5" style="stroke:#181818;stroke-width:0.5;" width="137" x="1428" y="362.5"/><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="44" x="1431" y="380.4951">Entity</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="1475" y="380.4951"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="83" x="1479" y="380.4951">(prov:Entity)</text></g></a><a href="../../organizations/en#org%3AOrganization" target="_top" title="../../organizations/en#org%3AOrganization" xlink:actuate="onRequest" xlink:href="../../organizations/en#org%3AOrganization" xlink:show="new" xlink:title="../../organizations/en#org%3AOrganization" xlink:type="simple"><g id="elem_org_Organization"><rect codeLine="23" fill="#F1F1F1" height="26.2969" id="org_Organization" rx="3.5" ry="3.5" style="stroke:#181818;stroke-width:0.5;" width="235" x="1000" y="362.5"/><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="100" x="1003" y="380.4951">Organization</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="1103" y="380.4951"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="125" x="1107" y="380.4951">(org:Organization)</text></g></a><a href="#premis%3AOutcomeStatus" target="_top" title="#premis%3AOutcomeStatus" xlink:actuate="onRequest" xlink:href="#premis%3AOutcomeStatus" xlink:show="new" xlink:title="#premis%3AOutcomeStatus" xlink:type="simple"><g id="elem_premis_OutcomeStatus"><rect codeLine="24" fill="#F1F1F1" height="26.2969" id="premis_OutcomeStatus" rx="3.5" ry="3.5" style="stroke:#181818;stroke-width:0.5;" width="305" x="1616" y="194.5"/><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="71" x="1619" y="212.4951">Outcome</text><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="5" x="1690" y="212.4951"> </text><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="49" x="1695" y="212.4951">status</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="1744" y="212.4951"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="170" x="1748" y="212.4951">(premis:OutcomeStatus)</text></g></a><a href="../../organizations/en#schema%3APerson" target="_top" title="../../organizations/en#schema%3APerson" xlink:actuate="onRequest" xlink:href="../../organizations/en#schema%3APerson" xlink:show="new" xlink:title="../../organizations/en#schema%3APerson" xlink:type="simple"><g id="elem_schema_Person"><rect codeLine="25" fill="#F1F1F1" height="26.2969" id="schema_Person" rx="3.5" ry="3.5" style="stroke:#181818;stroke-width:0.5;" width="185" x="7" y="362.5"/><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="56" x="10" y="380.4951">Person</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="66" y="380.4951"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="119" x="70" y="380.4951">(schema:Person)</text></g></a><a href="#schema%3AThing" target="_top" title="#schema%3AThing" xlink:actuate="onRequest" xlink:href="#schema%3AThing" xlink:show="new" xlink:title="#schema%3AThing" xlink:type="simple"><g id="elem_schema_Thing"><rect codeLine="26" fill="#F1F1F1" height="26.2969" id="schema_Thing" rx="3.5" ry="3.5" style="stroke:#181818;stroke-width:0.5;" width="163" x="18" y="514.5"/><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="44" x="21" y="532.4951">Thing</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="65" y="532.4951"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="109" x="69" y="532.4951">(schema:Thing)</text></g></a><a href="#premis%3ASoftwareAgent" target="_top" title="#premis%3ASoftwareAgent" xlink:actuate="onRequest" xlink:href="#premis%3ASoftwareAgent" xlink:show="new" xlink:title="#premis%3ASoftwareAgent" xlink:type="simple"><g id="elem_premis_SoftwareAgent"><rect codeLine="27" fill="#F1F1F1" height="99.4844" id="premis_SoftwareAgent" rx="3.5" ry="3.5" style="stroke:#181818;stroke-width:0.5;" width="295" x="567" y="326"/><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="72" x="570" y="343.9951">Software</text><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="5" x="642" y="343.9951"> </text><text fill="#000000" font-family="sans-serif" font-size="14" font-weight="bold" lengthAdjust="spacing" textLength="45" x="647" y="343.9951">agent</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="692" y="343.9951"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="163" x="696" y="343.9951">(premis:SoftwareAgent)</text><line style="stroke:#181818;stroke-width:0.5;" x1="568" x2="861" y1="352.2969" y2="352.2969"/><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="43" x="573" y="369.292">model</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="616" y="369.292"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="5" x="620" y="369.292">:</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="625" y="369.292"> </text><text fill="#000000" font-family="sans-serif" font-size="14" font-style="italic" lengthAdjust="spacing" textLength="68" x="629" y="369.292">xsd:string</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="697" y="369.292"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="36" x="701" y="369.292">[0..1]</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="39" x="573" y="385.5889">name</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="612" y="385.5889"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="5" x="616" y="385.5889">:</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="621" y="385.5889"> </text><text fill="#000000" font-family="sans-serif" font-size="14" font-style="italic" lengthAdjust="spacing" textLength="92" x="625" y="385.5889">rdf:langString</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="717" y="385.5889"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="36" x="721" y="385.5889">[1..1]</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="91" x="573" y="401.8857">serialNumber</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="664" y="401.8857"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="5" x="668" y="401.8857">:</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="673" y="401.8857"> </text><text fill="#000000" font-family="sans-serif" font-size="14" font-style="italic" lengthAdjust="spacing" textLength="68" x="677" y="401.8857">xsd:string</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="745" y="401.8857"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="36" x="749" y="401.8857">[0..1]</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="50" x="573" y="418.1826">version</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="623" y="418.1826"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="5" x="627" y="418.1826">:</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="632" y="418.1826"> </text><text fill="#000000" font-family="sans-serif" font-size="14" font-style="italic" lengthAdjust="spacing" textLength="68" x="636" y="418.1826">xsd:string</text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="4" x="704" y="418.1826"> </text><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="36" x="708" y="418.1826">[0..1]</text></g></a><g id="link_prov_Activity_org_Organization"><path codeLine="39" d="M725.13,249 C841.41,286.19 1000.7152,337.1422 1074.0952,360.6122 " fill="none" id="prov_Activity-to-org_Organization" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#454645" points="1079.81,362.44,1072.4563,355.8884,1075.0477,360.9168,1070.0192,363.5081,1079.81,362.44" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#000000" points="867.2623,289.0896,859.5425,283.5349,857.7519,289.1334,867.2623,289.0896" style="stroke:#000000;stroke-width:1.0;"/><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="24" x="871.5" y="292.0669">was</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="895.5" y="292.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="69" x="899.5" y="292.0669">associated</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="968.5" y="292.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="25" x="972.5" y="292.0669">with</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="997.5" y="292.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="34" x="1001.5" y="292.0669">[1..1]</text></g><g id="link_prov_Activity_premis_HardwareAgent"><path codeLine="40" d="M471.31,234.25 C446,244.53 421.67,258.91 403.5,279 C391.92,291.81 386.8873,303.4807 383.6573,320.0607 " fill="none" id="prov_Activity-to-premis_HardwareAgent" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#454645" points="382.51,325.95,388.1572,317.8809,383.4661,321.0423,380.3048,316.3512,382.51,325.95" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#000000" points="404.9271,291.0642,413.4465,286.8367,409.3346,282.6365,404.9271,291.0642" style="stroke:#000000;stroke-width:1.0;"/><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="24" x="417.5" y="292.0669">was</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="441.5" y="292.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="69" x="445.5" y="292.0669">associated</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="514.5" y="292.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="25" x="518.5" y="292.0669">with</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="543.5" y="292.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="34" x="547.5" y="292.0669">[1..1]</text></g><g id="link_prov_Activity_premis_SoftwareAgent"><path codeLine="41" d="M588.7,249.25 C587.08,264.7 587.94,281.95 595.5,296 C601.6,307.33 605.6549,313.3033 615.3849,321.9933 " fill="none" id="prov_Activity-to-premis_SoftwareAgent" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#454645" points="619.86,325.99,615.8119,317.0115,616.1308,322.6594,610.4829,322.9783,619.86,325.99" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#000000" points="602.222,292.2605,601.866,282.7566,596.3478,284.7809,602.222,292.2605" style="stroke:#000000;stroke-width:1.0;"/><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="24" x="609.5" y="292.0669">was</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="633.5" y="292.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="69" x="637.5" y="292.0669">associated</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="706.5" y="292.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="25" x="710.5" y="292.0669">with</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="735.5" y="292.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="34" x="739.5" y="292.0669">[1..1]</text></g><g id="link_prov_Activity_schema_Person"><path codeLine="42" d="M471.24,213.79 C391.75,221.27 289.18,238.72 206.5,279 C164.42,299.5 130.2638,336.7663 113.0538,357.5763 " fill="none" id="prov_Activity-to-schema_Person" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#454645" points="109.23,362.2,118.0482,357.8137,112.4165,358.3469,111.8833,352.7153,109.23,362.2" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#000000" points="206.8599,289.4291,216.3488,288.7869,214.1591,283.3321,206.8599,289.4291" style="stroke:#000000;stroke-width:1.0;"/><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="24" x="220.5" y="292.0669">was</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="244.5" y="292.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="69" x="248.5" y="292.0669">associated</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="317.5" y="292.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="25" x="321.5" y="292.0669">with</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="346.5" y="292.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="34" x="350.5" y="292.0669">[1..1]</text></g><g id="link_premis_Event_prov_Activity"><path codeLine="45" d="M1097.98,74 C990.39,102.54 851.8781,139.2841 742.9481,168.1841 " fill="none" id="premis_Event-to-prov_Activity" style="stroke:#0000FF;stroke-width:1.0;stroke-dasharray:1.0,3.0;"/><polygon fill="none" points="725.55,172.8,744.4867,173.9835,741.4095,162.3848,725.55,172.8" style="stroke:#0000FF;stroke-width:1.0;"/></g><g id="link_premis_Event_org_Organization"><path codeLine="49" d="M1210.98,74.28 C1199.03,115.25 1177.74,187.46 1158.5,249 C1145.43,290.78 1130.945,334.3905 1123.465,356.7305 " fill="none" id="premis_Event-to-org_Organization" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#454645" points="1121.56,362.42,1128.2105,355.1557,1123.1475,357.6787,1120.6245,352.6157,1121.56,362.42" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#000000" points="1187.0202,212.3424,1192.5044,204.5723,1186.8899,202.8327,1187.0202,212.3424" style="stroke:#000000;stroke-width:1.0;"/><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="85" x="1197.5" y="212.0669">implemented</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="1282.5" y="212.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="15" x="1286.5" y="212.0669">by</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="1301.5" y="212.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="34" x="1305.5" y="212.0669">[1..1]</text></g><g id="link_premis_Event_premis_HardwareAgent"><path codeLine="50" d="M1090.22,52.1 C877.75,70.65 466.72,112.23 331.5,166 C246.68,199.73 120.65,220.88 172.5,296 C180.61,307.74 195.8695,317.0014 221.3495,327.4614 " fill="none" id="premis_Event-to-premis_HardwareAgent" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#454645" points="226.9,329.74,220.0933,322.6218,222.2746,327.8412,217.0552,330.0225,226.9,329.74" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#000000" points="331.7336,209.077,341.2439,209.1459,339.4682,203.5427,331.7336,209.077" style="stroke:#000000;stroke-width:1.0;"/><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="70" x="345.5" y="212.0669">instrument</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="415.5" y="212.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="33" x="419.5" y="212.0669">[0..*]</text></g><g id="link_premis_Event_premis_Object"><path codeLine="51" d="M1350.77,55.64 C1386.61,64.81 1423.32,79.74 1451.5,104 C1479.49,128.09 1489.6411,166.9778 1493.5711,188.4778 " fill="none" id="premis_Event-to-premis_Object" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#454645" points="1494.65,194.38,1496.9665,184.8074,1493.7509,189.4615,1489.0969,186.2459,1494.65,194.38" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#000000" points="1483.1609,123.5383,1478.5399,115.2258,1474.5365,119.5295,1483.1609,123.5383" style="stroke:#000000;stroke-width:1.0;"/><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="23" x="1488.5" y="117.0669">has</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="1511.5" y="117.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="43" x="1515.5" y="117.0669">source</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="1558.5" y="117.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="33" x="1562.5" y="117.0669">[0..*]</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="36" x="1488.5" y="132.1997">result</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="1524.5" y="132.1997"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="33" x="1528.5" y="132.1997">[0..*]</text></g><g id="link_premis_Object_premis_Event"><path codeLine="68" d="M1465.63,194.49 C1443.48,186.06 1412.85,174.77 1385.5,166 C1338.06,150.78 1317.17,166.13 1277.5,136 C1256.9,120.36 1244.6592,100.3938 1235.3392,79.8538 " fill="none" id="premis_Object-to-premis_Event" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#454645" points="1232.86,74.39,1232.9363,84.2386,1234.926,78.9432,1240.2214,80.9329,1232.86,74.39" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#000000" points="1278.0239,117.8383,1284.8116,124.5,1287.4309,119.238,1278.0239,117.8383" style="stroke:#000000;stroke-width:1.0;"/><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="24" x="1291.5" y="124.5669">was</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="1315.5" y="124.5669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="66" x="1319.5" y="124.5669">generated</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="1385.5" y="124.5669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="15" x="1389.5" y="124.5669">by</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="1404.5" y="124.5669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="34" x="1408.5" y="124.5669">[0..1]</text></g><g id="link_premis_Event_premis_OutcomeStatus"><path codeLine="52" d="M1350.93,49.82 C1426.83,57.8 1523.27,73.43 1604.5,104 C1664.52,126.59 1721.5746,168.7945 1749.0646,190.6645 " fill="none" id="premis_Event-to-premis_OutcomeStatus" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#454645" points="1753.76,194.4,1749.2073,185.6666,1749.8472,191.2871,1744.2267,191.9271,1753.76,194.4" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#000000" points="1675.2137,121.7339,1667.6667,115.9467,1665.7064,121.488,1675.2137,121.7339" style="stroke:#000000;stroke-width:1.0;"/><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="23" x="1679.5" y="124.5669">has</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="1702.5" y="124.5669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="57" x="1706.5" y="124.5669">outcome</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="1763.5" y="124.5669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="34" x="1767.5" y="124.5669">[0..1]</text></g><g id="link_premis_Event_premis_SoftwareAgent"><path codeLine="53" d="M1135.65,74.09 C1094.21,94.34 1047.38,124.53 1019.5,166 C986.8,214.63 1036.75,252.49 997.5,296 C978.16,317.44 926.4012,333.9418 868.1612,347.1618 " fill="none" id="premis_Event-to-premis_SoftwareAgent" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#454645" points="862.31,348.49,871.9722,350.3985,867.186,347.3832,870.2013,342.597,862.31,348.49" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#000000" points="1021.0012,211.1383,1029.4301,206.7333,1025.2311,202.6201,1021.0012,211.1383" style="stroke:#000000;stroke-width:1.0;"/><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="59" x="1033.5" y="212.0669">executed</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="1092.5" y="212.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="15" x="1096.5" y="212.0669">by</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="1111.5" y="212.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="34" x="1115.5" y="212.0669">[0..1]</text></g><g id="link_premis_HardwareAgent_premis_Agent"><path codeLine="56" d="M460.92,425.24 C488.35,440.92 519.39,457.88 548.5,472 C581.95,488.23 604.6985,497.6239 631.9285,507.9939 " fill="none" id="premis_HardwareAgent-to-premis_Agent" style="stroke:#0000FF;stroke-width:1.0;stroke-dasharray:1.0,3.0;"/><polygon fill="none" points="648.75,514.4,634.0639,502.3867,629.7932,513.601,648.75,514.4" style="stroke:#0000FF;stroke-width:1.0;"/></g><g id="link_premis_HardwareAgent_schema_Brand"><path codeLine="63" d="M389.89,425.2 C395.36,450.86 400.5873,475.3622 405.0173,496.1122 " fill="none" id="premis_HardwareAgent-to-schema_Brand" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#454645" points="406.27,501.98,408.3027,492.3432,405.2261,497.0902,400.4791,494.0135,406.27,501.98" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#000000" points="405.5431,468.4564,406.5303,458.9972,400.7818,460.2235,405.5431,468.4564" style="stroke:#000000;stroke-width:1.0;"/><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="37" x="413.5" y="468.0669">brand</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="450.5" y="468.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="34" x="454.5" y="468.0669">[0..1]</text></g><g id="link_premis_Object_prov_Entity"><path codeLine="66" d="M1496.5,220.71 C1496.5,251.4 1496.5,313.56 1496.5,344.28 " fill="none" id="premis_Object-to-prov_Entity" style="stroke:#0000FF;stroke-width:1.0;stroke-dasharray:1.0,3.0;"/><polygon fill="none" points="1496.5,362.28,1502.5,344.28,1490.5,344.28,1496.5,362.28" style="stroke:#0000FF;stroke-width:1.0;"/></g><g id="link_schema_Person_schema_Thing"><path codeLine="74" d="M99.5,388.52 C99.5,416.61 99.5,468.28 99.5,496.42 " fill="none" id="schema_Person-to-schema_Thing" style="stroke:#0000FF;stroke-width:1.0;stroke-dasharray:1.0,3.0;"/><polygon fill="none" points="99.5,514.42,105.5,496.42,93.5,496.42,99.5,514.42" style="stroke:#0000FF;stroke-width:1.0;"/></g><g id="link_premis_SoftwareAgent_premis_Agent"><path codeLine="77" d="M703.79,425.2 C696.86,456.68 692.2528,477.6616 688.0228,496.8616 " fill="none" id="premis_SoftwareAgent-to-premis_Agent" style="stroke:#0000FF;stroke-width:1.0;stroke-dasharray:1.0,3.0;"/><polygon fill="none" points="684.15,514.44,693.8822,498.1525,682.1633,495.5706,684.15,514.44" style="stroke:#0000FF;stroke-width:1.0;"/></g><g id="link_premis_SoftwareAgent_schema_Brand"><path codeLine="84" d="M616.12,425.2 C564.28,450.86 508.317,478.5678 466.407,499.3178 " fill="none" id="premis_SoftwareAgent-to-schema_Brand" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#454645" points="461.03,501.98,470.8704,501.5714,465.5109,499.7615,467.3208,494.402,461.03,501.98" style="stroke:#454645;stroke-width:1.0;"/><polygon fill="#000000" points="555.0191,465.7848,564.4291,464.4055,561.8212,459.1379,555.0191,465.7848" style="stroke:#000000;stroke-width:1.0;"/><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="37" x="568.5" y="468.0669">brand</text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="4" x="605.5" y="468.0669"> </text><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="34" x="609.5" y="468.0669">[0..1]</text></g></g></svg>
  </div>
</div>

## Namespaces

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

## Classes & Properties

**Classes:** 
 [Brand](#schema%3ABrand) |  [Activity](#prov%3AActivity) |  [Event](#premis%3AEvent) |  [Hardware agent](#premis%3AHardwareAgent) |  [Object](#premis%3AObject) |  [Organization <svg class="svg-external-link" viewBox="0 0 24 24" aria-labelledby="svg-external-link-title"><use xlink:href="#svg-external-link"></use></svg>](../../organizations/en#org%3AOrganization){:target="_blank"} |  [Outcome status](#premis%3AOutcomeStatus) |  [Person <svg class="svg-external-link" viewBox="0 0 24 24" aria-labelledby="svg-external-link-title"><use xlink:href="#svg-external-link"></use></svg>](../../organizations/en#schema%3APerson){:target="_blank"} |  [Software agent](#premis%3ASoftwareAgent)
## <a id="schema%3ABrand"></a>Brand <small>[(schema:Brand)](https://schema.org/Brand)</small>




| Property | Description | Cardinality | Datatype |
| :------ | :---------- | :---------- | :------- |
| <a id='schema%3Aname'></a>name <br> <small>[(schema:name)](https://schema.org/name)</small> | The name of the item. | `1..1` | [`rdf:langString`](http://www.w3.org/1999/02/22-rdf-syntax-ns#langString)  |

## <a id="prov%3AActivity"></a>Activity <small>[(prov:Activity)](http://www.w3.org/ns/prov#Activity)</small>


**Subclasses:** 
[Event](#premis%3AEvent)

An activity is something that occurs over a period of time and acts upon or with entities; it may include consuming, processing, transforming, modifying, relocating, using, or generating entities.

| Property | Description | Cardinality | Datatype |
| :------ | :---------- | :---------- | :------- |
| <a id='prov%3AendedAtTime'></a>has end date <br> <small>[(prov:endedAtTime)](http://www.w3.org/ns/prov#endedAtTime)</small> | The end date of the activity. | `1..1` | [`xsd:dateTime`](http://www.w3.org/2001/XMLSchema#dateTime)  |
| <a id='prov%3Agenerated'></a>has generated <br> <small>[(prov:generated)](http://www.w3.org/ns/prov#generated)</small> | The generated object. | `0..1` | [`IRI`](https://www.rfc-editor.org/rfc/rfc3987.txt)  |
| <a id='prov%3AstartedAtTime'></a>has start date <br> <small>[(prov:startedAtTime)](http://www.w3.org/ns/prov#startedAtTime)</small> | The start date of the activity. | `1..1` | [`xsd:dateTime`](http://www.w3.org/2001/XMLSchema#dateTime)  |
| <a id='prov%3AwasAssociatedWith'></a>was associated with <br> <small>[(prov:wasAssociatedWith)](http://www.w3.org/ns/prov#wasAssociatedWith)</small> | An `prov:Agent` that had some (unspecified) responsibility for the occurrence of this `prov:Activity`. | `1..1` | [Person <svg class="svg-external-link" viewBox="0 0 24 24" aria-labelledby="svg-external-link-title"><use xlink:href="#svg-external-link"></use></svg>](../../organizations/en#schema%3APerson){:target="_blank"} _or_ [Organization <svg class="svg-external-link" viewBox="0 0 24 24" aria-labelledby="svg-external-link-title"><use xlink:href="#svg-external-link"></use></svg>](../../organizations/en#org%3AOrganization){:target="_blank"} _or_ [Software agent](#premis%3ASoftwareAgent) _or_ [Hardware agent](#premis%3AHardwareAgent)  |

## <a id="premis%3AEvent"></a>Event <small>[(premis:Event)](http://www.loc.gov/premis/rdf/v3/Event)</small>


**Subclass of:** 
[Activity](#prov%3AActivity)

Action performed within or outside the repository that affects its capability to preserve Objects over the long term.

| Property | Description | Cardinality | Datatype |
| :------ | :---------- | :---------- | :------- |
| <a id='evtAgRole%3Aexe'></a>executed by <br> <small>[(evtAgRole:exe)](http://id.loc.gov/vocabulary/preservation/eventRelatedAgentRole/exe)</small> | The software that executed the event. | `0..1` | [Software agent](#premis%3ASoftwareAgent)  |
| <a id='premis%3Anote'></a>has note <br> <small>[(premis:note)](http://www.loc.gov/premis/rdf/v3/note)</small> | A note about the event. | `0..1` | [`xsd:string`](http://www.w3.org/2001/XMLSchema#string)  |
| <a id='premis%3Aoutcome'></a>has outcome <br> <small>[(premis:outcome)](http://www.loc.gov/premis/rdf/v3/outcome)</small> | The outcome status of the event. | `0..1` | [Outcome status](#premis%3AOutcomeStatus) <br>_Possible values: [`evtOutcome:fai`](http://id.loc.gov/vocabulary/preservation/eventOutcome/fai), [`evtOutcome:suc`](http://id.loc.gov/vocabulary/preservation/eventOutcome/suc), [`evtOutcome:war`](http://id.loc.gov/vocabulary/preservation/eventOutcome/war)_ |
| <a id='premis%3AoutcomeNote'></a>has outcome note <br> <small>[(premis:outcomeNote)](http://www.loc.gov/premis/rdf/v3/outcomeNote)</small> | A note about the outcome of the event. | `0..1` | [`xsd:string`](http://www.w3.org/2001/XMLSchema#string)  |
| <a id='evtObjRole%3Asou'></a>has source <br> <small>[(evtObjRole:sou)](http://id.loc.gov/vocabulary/preservation/eventRelatedObjectRole/sou)</small> | The object that was used as a source for the event. | `0..*` | [Object](#premis%3AObject)  |
| <a id='evtAgRole%3Aimp'></a>implemented by <br> <small>[(evtAgRole:imp)](http://id.loc.gov/vocabulary/preservation/eventRelatedAgentRole/imp)</small> | The organization that implemented the event. | `1..1` | [Organization <svg class="svg-external-link" viewBox="0 0 24 24" aria-labelledby="svg-external-link-title"><use xlink:href="#svg-external-link"></use></svg>](../../organizations/en#org%3AOrganization){:target="_blank"}  |
| <a id='schema%3Ainstrument'></a>instrument <br> <small>[(schema:instrument)](https://schema.org/instrument)</small> | The hardware that was used to execute the event. | `0..*` | [Hardware agent](#premis%3AHardwareAgent)  |
| <a id='evtObjRole%3Aout'></a>result <br> <small>[(evtObjRole:out)](http://id.loc.gov/vocabulary/preservation/eventRelatedObjectRole/out)</small> | The object that was generated by the event. | `0..*` | [Object](#premis%3AObject)  |

_Properties from [Activity](#prov%3AActivity):_  [has end date](#prov%3AendedAtTime),  [has generated](#prov%3Agenerated),  [has start date](#prov%3AstartedAtTime),  [was associated with](#prov%3AwasAssociatedWith)

## <a id="premis%3AHardwareAgent"></a>Hardware agent <small>[(premis:HardwareAgent)](http://www.loc.gov/premis/rdf/v3/HardwareAgent)</small>


**Subclass of:** 
[Agent](#premis%3AAgent)

Hardware agent (e.g., a computer) that is associated with one or more Events and/or Rights statement associated with a digital object.

| Property | Description | Cardinality | Datatype |
| :------ | :---------- | :---------- | :------- |
| <a id='schema%3Abrand'></a>brand <br> <small>[(schema:brand)](https://schema.org/brand)</small> | The particular brand of the Agent. | `0..1` | [Brand](#schema%3ABrand)  |
| <a id='schema%3Amodel'></a>model <br> <small>[(schema:model)](https://schema.org/model)</small> | The particular model of the Agent. | `0..1` | [`xsd:string`](http://www.w3.org/2001/XMLSchema#string)  |
| <a id='schema%3Aname'></a>name <br> <small>[(schema:name)](https://schema.org/name)</small> | The name of the item. | `1..1` | [`rdf:langString`](http://www.w3.org/1999/02/22-rdf-syntax-ns#langString)  |
| <a id='schema%3AserialNumber'></a>serialNumber <br> <small>[(schema:serialNumber)](https://schema.org/serialNumber)</small> | The serial number or any alphanumeric identifier of a particular agent. | `0..1` | [`xsd:string`](http://www.w3.org/2001/XMLSchema#string)  |
| <a id='schema%3Aversion'></a>version <br> <small>[(schema:version)](https://schema.org/version)</small> | The agent's version number or version name. | `0..1` | [`xsd:string`](http://www.w3.org/2001/XMLSchema#string)  |



## <a id="premis%3AObject"></a>Object <small>[(premis:Object)](http://www.loc.gov/premis/rdf/v3/Object)</small>


**Subclass of:** 
[Entity](#prov%3AEntity)

**Subclasses:** 
[File](#premis%3AFile)
, [Intellectual entity](#premis%3AIntellectualEntity)
, [Representation](#premis%3ARepresentation)

Discrete unit of information subject to digital preservation. Subclasses of Object are Intellectual Entity, Representation, File and Bitstream.

| Property | Description | Cardinality | Datatype |
| :------ | :---------- | :---------- | :------- |
| <a id='prov%3AwasGeneratedBy'></a>was generated by <br> <small>[(prov:wasGeneratedBy)](http://www.w3.org/ns/prov#wasGeneratedBy)</small> | The time at which the object was completely created and is available for use. | `0..1` | [Event](#premis%3AEvent)  |



## <a id="premis%3AOutcomeStatus"></a>Outcome status <small>[(premis:OutcomeStatus)](http://www.loc.gov/premis/rdf/v3/OutcomeStatus)</small>


Overall result of the Event in terms of success, partial success, or failure.


## <a id="premis%3ASoftwareAgent"></a>Software agent <small>[(premis:SoftwareAgent)](http://www.loc.gov/premis/rdf/v3/SoftwareAgent)</small>


**Subclass of:** 
[Agent](#premis%3AAgent)

Software agent (e.g., a computer program) that is associated with one or more Event and/or Rights statement associated with a digital object.

| Property | Description | Cardinality | Datatype |
| :------ | :---------- | :---------- | :------- |
| <a id='schema%3Abrand'></a>brand <br> <small>[(schema:brand)](https://schema.org/brand)</small> | The particular brand of the Agent. | `0..1` | [Brand](#schema%3ABrand)  |
| <a id='schema%3Amodel'></a>model <br> <small>[(schema:model)](https://schema.org/model)</small> | The particular model of the Agent. | `0..1` | [`xsd:string`](http://www.w3.org/2001/XMLSchema#string)  |
| <a id='schema%3Aname'></a>name <br> <small>[(schema:name)](https://schema.org/name)</small> | The name of the item. | `1..1` | [`rdf:langString`](http://www.w3.org/1999/02/22-rdf-syntax-ns#langString)  |
| <a id='schema%3AserialNumber'></a>serialNumber <br> <small>[(schema:serialNumber)](https://schema.org/serialNumber)</small> | The serial number or any alphanumeric identifier of a particular agent. | `0..1` | [`xsd:string`](http://www.w3.org/2001/XMLSchema#string)  |
| <a id='schema%3Aversion'></a>version <br> <small>[(schema:version)](https://schema.org/version)</small> | The agent's version number or version name. | `0..1` | [`xsd:string`](http://www.w3.org/2001/XMLSchema#string)  |



[^1]: Unique language tags required
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
