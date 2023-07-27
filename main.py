# This is a sample Python script.
from api.webServer import getWebserver
from whisper.modelLoader import getModel


def startServer():
    getModel()
    print('Model loaded')
    webserver = getWebserver()
    print('Starting server on port 3001')
    try:
        webserver.serve_forever()
    except KeyboardInterrupt:
        pass
    webserver.server_close()


if __name__ == '__main__':
    startServer()
