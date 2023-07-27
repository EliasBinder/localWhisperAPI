from faster_whisper import WhisperModel

model_size = "large-v2"

model = WhisperModel(model_size, device="cpu", compute_type="int8")


def getModel():
    return model
