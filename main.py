import speech_recognition as sr
r = sr.Recognizer()
file = sr.AudioFile('one.wav')
with file as source:
 audio = r.record(source)
 result = r.recognize_google(audio)
print(result)
