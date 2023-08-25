from translate import Translator
translator = Translator(to_lang='id')
try:
    with open('./file_test/translate.txt', mode='r', encoding='utf-8') as my_file:
        file = my_file.read()
        tr = translator.translate(file)
        print(tr)
        with open('./file_test/tr_output.txt', 'w') as output:
            output.write(tr)
except FileNotFoundError:
    print('file not found')
