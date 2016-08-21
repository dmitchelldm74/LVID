from flask import Flask, render_template, Response, request
#from camera import VideoCamera
default = 'None'
CHANNELS = {'1':default}
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/upload', methods=['POST'])
def upload():
    data = request.form['content']
    CHANNELS[request.form['channel']] = b"%s" % (data)#bytearray(data, 'utf-8')
    return ''
def gen(channel, url=False):
    frame = CHANNELS[channel]
    if url == True:
        return 'data:image/jpeg;base64,' + frame
    return render_template('image.html', url='data:image/jpeg;base64,' + frame)
@app.route('/video/<CHANNEL>')
def video_feed(CHANNEL):
    if CHANNEL in CHANNELS:
        return Response(gen(CHANNEL), mimetype='text/html')
    return ""
@app.route('/video_url/<CHANNEL>')
def video_feed2(CHANNEL):
    if CHANNEL in CHANNELS:
        return Response(gen(CHANNEL, url=True), mimetype='text/html')
    return ""

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=9400, threaded=True)
