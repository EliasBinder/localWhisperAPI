from http.server import HTTPServer, BaseHTTPRequestHandler

from config import getAudioPath
from whisper.transcriber import transcribe


class WebserverHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'plain/text')
        self.end_headers()
        transcription = transcribe(getAudioPath())
        self.wfile.write(bytes(transcription.encode('utf-8')))


def getWebserver():
    webserver = HTTPServer(('127.0.0.1', 3001), WebserverHandler)
    return webserver
