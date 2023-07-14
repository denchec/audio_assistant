import speech_recognition as sr

rec = sr.Recognizer()
mic = sr.Microphone()


def recognize_voice_message():
    with mic as source:
        audio = rec.listen(source)

    value = rec.recognize_google(audio, language='ru')

    return value
