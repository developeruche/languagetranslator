from googletrans import Translator
from googletrans import LANGUAGES

print("This is the list of all translatable language: ")

for lang in LANGUAGES:
    print(f"{lang} - {LANGUAGES[lang]}")
chooseSourceLanguage = input(
    "The language you want to translate from e.g. if English enter en"
)
chooseDestinationLanguage = input(
    "The language you want to translate to e.g. if English enter en")

statement = input("Input a statement... ")

translator = Translator()
if (len(chooseDestinationLanguage) > 0 and len(chooseDestinationLanguage) > 0 and len(statement) > 0):
    translated_sentence = translator.translate(
        statement, src=chooseSourceLanguage, dest=chooseDestinationLanguage)
else:
    print("Error!!! Error!! Error!")

print(translated_sentence.text)
