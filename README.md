# Innovator IoT Challenge Object Detection 

Interacts with TensorFlow Object API (https://github.com/tensorflow/models/tree/master/research/object_detection) as a web service. 

Relied heavily on this post and code from here: https://webrtchacks.com/webrtc-cv-tensorflow/


## Run with Docker
```$xslt
docker run -it -p 5000:5000 ddonaught/dgd_vision:latest
```

### Manual install

Follow the TensorFlow Object API install [instructions](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/installation.md).

## Web Interface

Point your browser to:
-  `https://localhost:5000/local` - Shows a video stream from a camera and begins object detect


## API Details

Point a `<script>` tag to `objDetect.js` with an id of `objDetect`. Include `data-source="myVideo"` and other optional `data-` tags to set parameters.

Example:
```$xslt
<script id="objDetect" src="/static/objDetect.js" data-source="myVideo" data-mirror="true" data-uploadWidth="1280" data-scoreThreshold="0.40"></script>
```
Data tags:

- `data-source` - the ID of the source `<video>` to use. Must be specified.
- `data-uploadWidth` - the width of the upload file. Height will automatically be calculated based on the source video's aspect ratio. Default is `640`.
- `data-mirror` - mirror the boundary boxes. Used is the image is mirrored (as is usual with a local getUserMedia view). Default is `false`.
- `data-scoreThreshold` - only show objects above this confidence threshold. Default is `0.5`
 - `data-apiServer` - the full URL of the TensorFlow Object Detection Web API server location. Default is `/image` off of the current domain - 
 i.e. `http://localhost:5000/image`


