import speech_recognition as sr

r = sr.Recognizer()
m = sr.Microphone()

with m as source:
    audio = r.listen(source)

value = r.recognize_google(audio, language='ru')

print(value)
