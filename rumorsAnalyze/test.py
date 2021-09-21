from translate import Translator
def covert(char):
	translator = Translator(from_lang="chinese",to_lang="english")
	return translator.translate( char)
print(covert("你好"))
