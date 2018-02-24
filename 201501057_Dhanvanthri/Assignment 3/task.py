import spacy

file = open('goingwest.txt').read()
nlp = spacy.load('en_core_web_md')
doc = nlp(file)

print('\nNouns in the document')
print('-'*10)
for token in doc:
	if token.pos_ == 'NOUN':
		print(token.text)
print('-'*10)

print('\nLemmatization of the Verbs')
print('-'*10)
for token in doc:
	if token.pos_ == 'VERB':
		print(token.text,' ',token.lemma_)
print('-'*10)

print('\nNamed Entities:')
print('-'*10)
for entitiy in doc.ents:
	if entitiy.text != '\n':
		print(entitiy.text," ",entitiy.label_)
print('-'*10)