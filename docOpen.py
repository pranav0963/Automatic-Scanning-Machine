from googletrans import Translator
import pyttsx3

text_speech = pyttsx3.init()


class WordFile:
    def __init__(self, file):
        self.file = file
        self.text = file

    def translate(self, Language):
        translator = Translator()
        detected_language = translator.detect(self.text)
        print(detected_language)
        translation = translator.translate(self.text, src=detected_language.lang, dest=Language)
        print(translation.text)
        return translation.text

    def conveertToAudio(self):
        text_speech.say(self.text)
        text_speech.runAndWait()

