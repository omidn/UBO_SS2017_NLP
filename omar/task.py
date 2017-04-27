import nltk
from nltk.tag import StanfordNERTagger

filename = 'quotes.txt'
secondfile = 'result.txt'
second = open(secondfile, 'w')

# group of tags
nouns = ['NN', 'PRP', 'PRP$', 'NNP', 'NNPS']
adverbs = ['RB', 'RBR', 'RBS']
verbs = ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']
adjectives = ['JJ', 'JJR', 'JJS']

def tagger_grouping(filename, secondfile):
    """
    Read a file with quotes and return a new file with grouped tags
    """
    with open(filename, 'r') as fileobj:
        lines = fileobj.readlines()
        for line in lines:
            words = nltk.tokenize.word_tokenize(line)
            tags = nltk.pos_tag(words)
            
            # pos_tag and grouping
            for tag in tags:
                if tag[1] in adjectives:
                    identifier = 'adjective'
                if tag[1] in nouns:
                    identifier = 'noun'
                elif tag[1] in adverbs:
                    identifier = 'adverb'
                elif tag[1] in verbs:
                    identifier = 'verb'
                else:
                    identifier = tag[1]
                second.write(tag[0] + '_' + identifier + ' ')
            second.write('\n')
    second.close()
