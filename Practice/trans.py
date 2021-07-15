# pip install googletrans==3.1.0a0

from googletrans import Translator
translator = Translator()

# out = translator.translate("क्या हाल है", dest='en')
# print(out)

mystory = '''
I promised I'd show you how to avoid issues with skipping the defaultValue when using TypeScript. Guess what! By doing what I'm suggesting, you avoid the problem by default! It's actually not a problem at all. Check it out:
'''
out = translator.translate(mystory, dest='hi')
print(out.text)

# out = translator.translate("I am learning python", dest='gu')
# print(out)
