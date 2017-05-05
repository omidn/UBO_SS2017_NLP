import nltk

from nltk.tag import pos_tag, map_tag

file =  open("abc.txt","r")


abc = file.readline()
text = nltk.word_tokenize(abc)
posTagged = pos_tag(text)
simplifiedTags = pos_tag(text, tagset='universal')

ner= nltk.ne_chunk(posTagged)

nouns = [item[0] for item in posTagged if item[1][0] == 'N']
verbs = [item[0] for item in posTagged if item[1][0] == 'V']


horus_csv = open("output.txt", 'wb')
horus_csv.write('\n Postags \n')
horus_csv.write(str((posTagged)))
horus_csv.write('\n*********************************************************')
horus_csv.write('\nSimple Tags \n')
horus_csv.write(str((simplifiedTags)))
horus_csv.write('\n*********************************************************')
horus_csv.write('\nNouns\n')
horus_csv.write(str((nouns)))
horus_csv.write('\nVerbs\n')
horus_csv.write(str((verbs)))
horus_csv.write('\n*********************************************************')
horus_csv.write('\nNER\n')
horus_csv.write(str((ner)))
horus_csv.write('\n*********************************************************')


file.close()
