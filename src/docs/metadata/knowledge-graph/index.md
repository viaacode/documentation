---
title: Knowledge Graph
nav_order: 1
---

# Knowledge Graph Metadata Models

Here you will find all information about the semantic data models and thesauri in the meemoo Knowledge Graph.
These data models and thesauri are used to represent all knowledge from the meemoo archive as metadata.
To describe this broad knowledge we use a modular data model consisting of:

- a specific domain model per relevant domain (e.g. preserve, digitize, use) that describes the metadata that arises in this domain in depth;
- a broad core model with the general concepts that appear in the domain models;
- meta-models to annotate the accumulated knowledge such as usage rights (who may use the metadata or the material?), or data provenance (who added or modified the metadata and when?).

The thesauri are controlled (hierarchical) term lists to classify things.
All data models are available in [RDFS](https://www.w3.org/TR/rdf-schema/) and [SHACL](https://www.w3.org/TR/shacl/); the thesauri as [SKOS](https://www.w3.org/TR/skos-reference/).

!!! note

    These metadata models are currently still in development and therefore not available in production.



## Data Models


<figure>
    <div class="wrap">
        <div class="zoom">
            <!--<a href="0.0.1/all/all-diagram.nl.svg" target="_blank" rel="noopener noreferrer"> -->
                <object id="svg-object" data="1.0.0/all/all-diagram.nl.svg" type="image/svg+xml"></object>
            <!--</a>-->
        </div>
    </div>
    <figcaption>This diagram gives an overview of all models together.</figcaption>
</figure>


|Name|Documentation (NL)|Documentation (EN)|
|----|:-----------------------------:|:-------------------------:|
| **Objectstructure (core model)** | [1.0.0](1.0.0/objects/index.md) | [1.0.0](1.0.0/objects/index.md) |
| **Organizations** | [1.0.0](1.0.0/organizations/index.md) | [1.0.0](1.0.0/organizations/index.md) |
| **Description** | [1.0.0](1.0.0/description/index.md) | [1.0.0](1.0.0/description/index.md) |
| **Data provenance** | [1.0.0](1.0.0/events/index.md) | [1.0.0](1.0.0/events/index.md) |
| **Terms** | [1.0.0](1.0.0/terms/index.md) | [1.0.0](1.0.0/terms/index.md) |

## Thesauri

|Name|Documentation (NL)|Documentation (EN)|
|----|:----------------------------:|:------------------------:|
| **Education: education structure** | [1.0.0](https://w3id.org/onderwijs-vlaanderen/id/structuur/) | _Not available yet_ |
| **Education: subjects** | [1.0.0](https://w3id.org/onderwijs-vlaanderen/id/vak/) | _Not available yet_ |
| **Education: themes** | _Not available yet_ | _Not available yet_ |
| **Organization: types** | [0.0.1](https://termen.meemoo.be/conceptschemes/3) | [0.0.1](https://termen.meemoo.be/conceptschemes/3) |
| **Organization: functions** | [0.0.1](https://termen.meemoo.be/conceptschemes/5) | [0.0.1](https://termen.meemoo.be/conceptschemes/5) |
| **Data provenance: event types** | [0.0.1](https://termen.meemoo.be/conceptschemes/6) | [0.0.1](https://termen.meemoo.be/conceptschemes/6) |

<style>
#svg-object {
    width: 100%;
    height: auto;
    background-color: #fff;
}

#svg-object text{
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
  transform: scale(6.0); cursor: grab;
}
.svg-external-link {
  width: 16px;
  height: 16px;
}
</style>


<script type="text/javascript">
  window.addEventListener("load", function() {
    var svgObject = document.getElementById('svg-object').contentDocument;

    var svg = svgObject.querySelector('svg[zoomAndPan="magnify"]');
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

});
</script>
