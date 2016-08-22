import cv2
import requests
import base64
class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        # self.video = cv2.VideoCapture('video.mp4')
        self.frames = 0
    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        self.frames += 1
        success, image = self.video.read()
        ret, jpeg = cv2.imencode('.jpeg', image)
        jpeg = base64.b64encode(jpeg)
        return jpeg
    def stream(self, server, channel):
        while True:
            try:
                frame = self.get_frame()
                url = 'http://' + server + '/upload'
                data = dict(content=frame, channel=channel)
                r = requests.post(url, data=data, allow_redirects=True)
            except KeyboardInterrupt:
                print self.frames
                exit()
vid = VideoCamera()
vid.stream('162.243.6.91:9400', '1') #162.243.6.91:9400         0.0.0.0:9400
