import speech_recognition as sr
r = sr.Recognizer()
file = sr.AudioFile('one.wav')
with file as source:
 audio = r.record(source,duration=5)
 result = r.recognize_google(audio,language='es')
print(result)
