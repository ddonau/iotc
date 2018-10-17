@app.route('/text', methods=['POST'])
def text():
    try:
        text_file = request.files['text']  # get the text from s.object


        # run the image through tensor flow object detection`
        text_object = text.open(s.objects)
        objects = speech_detection_api.get_objects(text)
        return objects

    except Exception as f:
        print('POST /text error: %f' % f)
        return f