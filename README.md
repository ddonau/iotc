# iotc

The following code interacts with the TensorFlow Object API (https://github.com/tensorflow/models/tree/master/research/object_detection) using webRTC for realtime object detection.


## With Docker
```$xslt
docker run -it -p 5000:5000 ddonaught/iotc:latest
```

## Web Interface

After running the above, stream can be found at:
-  `https://localhost:5000/local` - Video stream begins object detect and provides voice response to the user.

