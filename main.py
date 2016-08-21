from flask import Flask, render_template, Response, request
import uuid, base64
default = 'None'
CHANNELS = {'1':default}
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/upload', methods=['POST'])
def upload():
    data = request.form['content']
    CHANNELS[request.form['channel']] = b"%s" % (data)
    return ''
def gen(channel):
    while True:
        frame = CHANNELS[channel]
        yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + base64.b64decode(frame) + b'\r\n')
@app.route('/video/<CHANNEL>')
def video_feed(CHANNEL):
    if CHANNEL in CHANNELS:
        return Response(gen(CHANNEL),
                        mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=9400, threaded=True)
