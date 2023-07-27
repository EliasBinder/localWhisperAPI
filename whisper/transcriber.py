from whisper.modelLoader import getModel


def transcribe(filename):
    segments, _ = getModel().transcribe(filename)
    text = ""
    for segment in segments:
        text += segment.text + " "
    text = text.strip()
    return text
