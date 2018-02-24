import spacy

print("Reading the sample text document")
file = open('Sample.txt').read()
print("Extracting Noun, Lemmatization of the Verbs and Named Entities from text")
nlp = spacy.load('en_core_web_md')
doc = nlp(file.decode('utf8'))

print('\nNouns found in the document')
print('-'*50)
for token in doc:
	if token.pos_ == 'NOUN':
		print(token.text)
print('-'*50)

print('\nLemmatization of the Verbs from the document')
print('-'*50)
print ('Verb\t\tlemma')
for token in doc:
	if token.pos_ == 'VERB':
		print token.text,'\t\t',token.lemma_
print('-'*50)

print('\nNamed Entities from the document:')
print('-'*50)
print ('Entity\t\tType')
for entitiy in doc.ents:
	if entitiy.text != '\n':
		print entitiy.text,'\t\t',entitiy.label_
print('-'*50)