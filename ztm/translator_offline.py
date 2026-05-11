from translate import Translator

translator = Translator(to_lang="hi")

with open("test.txt") as my_file:
    text = my_file.read()
    translation = translator.translate(text)
    print(translation)
