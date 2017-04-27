import nltk

import csv

from nltk.tag import pos_tag, map_tag

file =  open("abc.txt","r")


abc = file.readline()
text = nltk.word_tokenize(abc)
posTagged = pos_tag(text)
simplifiedTags = pos_tag(text, tagset='universal')

ner= nltk.ne_chunk(posTagged)

nouns = [item[0] for item in posTagged if item[1][0] == 'N']
verbs = [item[0] for item in posTagged if item[1][0] == 'V']

print("Nouns :", nouns)
print("Verbs :", verbs)

horus_csv = open("output.txt", 'wb')
wr = csv.writer(horus_csv, quoting=csv.QUOTE_ALL)
wr.writerows(posTagged)
print("Wrote postags to Output.txt")
wr.writerows(simplifiedTags)
print("Wrote SimpleTags to Output.txt")
wr.writerows(ner)
print(ner)
print ("Wrote   NER to Output.txt")
wr.writerows(verbs)
wr.writerows(nouns)
print("Printed   Nouns and Verbs to Output.txt")

file.close()
