from googletrans import Translator

def text_translator(text='Hello World', src='en', dest='pl'):
    try:
        translator = Translator()
        translations = translator.translate(text, src=src, dest=dest)
        
        return translations.text
    except Exception as ex:
        return ex
    

def main():
    print(text_translator(text='Hello World', src='en', dest='pl'))
    

if __name__ == '__main__':
    main()
