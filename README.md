# iotc

The following code interacts with the TensorFlow Object API (https://github.com/tensorflow/models/tree/master/research/object_detection) using webRTC for realtime object detection.


## Out of the box with Docker
```$xslt
docker run -it -p 5000:5000 ddonaught/dgd_vision:latest
```

## Web Interface

After running the above the stream can be found at:
-  `https://localhost:5000/local` - Video stream begins object detect and provides voice response to the user.


## Clone from Github for local copy 
```$xslt
git clone https://github.com/ddonaught/iotc
```