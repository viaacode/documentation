# IIIF 3.0 Image API

**Nav Order:** 3

---

## Over IIIF 

The [Image Interoperability Framework](https://iiif.io) (IIIF) is a set of open standards to make digitized archives available online. It provides a user-friendly access to the objects in an archive.  
The IIIF protocol uses a stable manifest, and provides a sustainable URL for each object in the archive. This allows for other versions of the same object to be added to a collection (e.g., in higher resolution) without changing the URL of this object. 

The IIIF protocol consists of 6 APIs, which can be used independently. Currently, only the Image API is utilized. This allows users to view images in a performant manner (parts of images), resize, rotate,... 

### Authentication

The IIIF endpoints provided by meemoo are publicly available, so no authentication is required. 

### Endpoint

The use of the Image API version 3.0 is made.  
The meemoo Image API endpoint complies with the highest IIIF compliance level, namely level 2.  
More information about IIIF and the Image API can be found on the [iiif.io website](https://iiif.io/api/image/3.0/). 

#### Environments

The endpoint is available on 3 environments: TST, QAS and PRD.  
Note: The images may differ between environments, depending on availability in the meemoo archive system. 

#### URL Construction 

To retrieve an image via a URL, the URL is constructed as follows: 

```shell
https://{DOMAIN}/iiif/{IDENTIFIER}.jp2/{REGION}/{SIZE}/{ROTATION}/{QUALITY}.{FORMAT}
```

Here is a brief summary of the possibilities of the endpoint, with each parameter individually explained.  
For a detailed description of the URL composition, see the [iiif.io documentation](https://iiif.io/api/image/3.0/#21-image-request-uri-syntax).

##### Domain 

The domain indicates from which environment the object is requested. There are 3 environments available: TST, QAS and PRD.  

| Environment | Domain                                               |
|-------------|------------------------------------------------------|
| TST         | [images-tst.meemoo.be](https://images-tst.meemoo.be) |
| QAS         | [images-qas.meemoo.be](https://images-qas.meemoo.be) |
| PRD         | [images.meemoo.be](https://images.meemoo.be)         |


##### Identifier 

The identifier of the object to be retrieved must match the `OriginalFilename` of the object. This can be found in the metadata of the desired object.  
A list of available identifiers can be found via the [inventory](https://images.meemoo.be/inventory).

##### Region 

The `REGION` parameter determines which rectangular area of the image is returned. A region can be expressed in pixel coordinates, percentages, or by the value `full`. The latter option ensures the entire image is returned. 

##### Size 

The `SIZE` parameter indicates up to which size the selected region should be scaled. You can enter `max` to scale the images maximally. Scaling is not applicable. 

All images available via the meemoo IIIF endpoint have a maximum length or width of 5000 pixels. Protected images are unlocked in a 640x480 pixel format. 

##### Rotation 

The image can also be shown rotated. You can provide a number between 0 and 360 in the URL to rotate the selected region clockwise. 

##### Quality 

To determine the quality of the image, you can choose from the following values: 
- `color`
- `gray`
- `bitonal`
- `default` 

These values will determine if the image is shown in color, grayscale, or black and white. 

##### Format 

You can choose between `jpg` and `png` as the format, depending on the desired image format. 

### Inventory 

An inventory of the available images can be found at [https://images.meemoo.be/inventory](https://images.meemoo.be/inventory). 

# Use case 

## General 

This paragraph describes a use case where an object is retrieved via the IIIF endpoint and displayed in the browser. 
The following transformations are applied to the object: 
- selecting a certain region
- scaling the selected region
- rotating the selected region
- showing the selected region in grayscale
- choosing the format of the image 

Only a subset of the possibilities of an IIIF endpoint is used in this use case. For the full range of possibilities, see the Image API-[documentation](https://iiif.io/api/image/3.0/#21-image-request-uri-syntax). 

## Step 1: Determine the identifier 

Suppose the object 'The Mocking of Christ (Ecce Homo)' by James Ensor is to be shown. The [inventory](https://images.meemoo.be/inventory) indicates that the original file name of this work is `h12v432j8x` (see column `Descriptive.OriginalFilename`). 

## Step 2: Build the URL 

### Identifier 

If the identifier is provided, the URL is as follows: 

```shell 
https://images.meemoo.be/iiif/h12v432j8x.jp2/full/max/0/default.jpg
```

Browsing to this URL will return the entire image without any applied transformations. 

### Region 

Suppose a region with the following properties is to be captured: 
- 1700 pixels offset left
- 1300 pixels offset up
- 1100 pixels width
- 1750 pixels height

The URL is built as follows: 

```shell
https://images.meemoo.be/iiif/h12v432j8x.jp2/1700,1300,1100,1750/full/0/default.jpg
```

The displayed image is cropped according to the chosen values. 

### Size 

To scale the selected region to a maximum width of 300px and a maximum height of 400px without losing the aspect ratio, the `SIZE` parameter can be filled as follows: 

```shell
https://images.meemoo.be/iiif/h12v432j8x.jp2/1700,1300,1100,1750/!300,400/0/default.jpg
```

In this case, the previously selected region of the image is returned with a width of 251px and a height of 400px. 

### Rotation 

If the scaled region should be rotated 90 degrees clockwise, the URL can be adjusted as follows: 

```shell
https://images.meemoo.be/iiif/h12v432j8x.jp2/1700,1300,1100,1750/!300,400/90/default.jpg
```

### Quality 

To display the image in grayscale, `gray` can be entered for the `QUALITY` parameter: 

```shell
https://images.meemoo.be/iiif/h12v432j8x.jp2/1700,1300,1100,1750/!300,400/90/gray.jpg
```

### Format 

To obtain the image in PNG format, `jpg` in the URL is simply replaced by `png`: 

``` shell
https://images.meemoo.be/iiif/h12v432j8x.jp2/1700,1300,1100,1750/!300,400/90/default.png
```
