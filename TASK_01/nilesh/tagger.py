import spacy
from spacy.en import English
import sys

nlp = English()

doc = nlp(sys.stdin.read().decode('UTF-8'))
nlp.tagger(doc)

with open("./pos.txt", "w") as f, open("posner.txt", "w") as f2:
    for word in doc:
        only_tags = word.text
        if word.pos_ in ('PROPN', 'NOUN', 'VERB'):
            only_tags += "_" + word.pos_
        only_tags += " "
        f.write(only_tags.encode("UTF-8"))
        
    print doc.ents
        
    for ent in doc.ents:
        if ent.label_:
            ent.merge(ent.root.tag_, ent.text, ent.label_)
            
    for word in doc:
        if word.ent_type_:
            with_ner = "%s_%s" % (word.text.replace(" ", "_"), word.ent_type_)
        else:
            with_ner = word.text
            if word.pos_ in ('PROPN', 'NOUN', 'VERB'):
                with_ner += "_" + word.pos_
        with_ner += " "
        f2.write(with_ner.encode("UTF-8"))
        
