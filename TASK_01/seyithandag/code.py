#author: seyithan dag 2707701

import nltk
import os

input_filepath = ''
output_filepath = ''

output_file = open(output_filepath, 'w')

with open(input_filepath, 'r') as input_file:
    for line in input_file:
        sentence = line
        print 'input sentence: ' + sentence + '\n',
        sentence_posmerged_str = ''
        sentence_posmerged_ner_str = ''
        tokens = nltk.word_tokenize(sentence)
        postags = nltk.pos_tag(tokens)
        noun = ['NN','NNS','NNP','NNPS']
        adjective = ['JJ','JJR','JJS']
        adverb = ['RB','RBR', 'RBS']
        verb = ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']
        ners_tree = nltk.ne_chunk(postags)
        ners_list = []
        for t in ners_tree.subtrees():
            if (t.label() == 'PERSON') or (t.label() == 'GPE') or (t.label() == 'ORGANIZATION'):
                ners_list.append(list(t)) 
        ners_list = [item for sublist in ners_list for item in sublist] 
        for tuple in postags:
            if(tuple[1] in noun):
                tuple = (tuple[0], '_NOUN')
            elif (tuple[1] in adjective):
                tuple = (tuple[0], '_ADJECTIVE')
            elif (tuple[1] in adverb):
                tuple = (tuple[0], '_ADVERB')
            elif (tuple[1] in verb):
                tuple = (tuple[0], '_VERB')
            else:
                tuple = (tuple[0], '')
            sentence_posmerged_str += str(tuple[0] + tuple[1] + ' ')
            if [i for i, v in enumerate(ners_list) if v[0] == tuple[0]]:
                sentence_posmerged_ner_str += str(tuple[0] + '_NER' + ' ')
            else:
                sentence_posmerged_ner_str += str(tuple[0] + tuple[1] + ' ')
        
        print 'output1: ' + sentence_posmerged_str + '\n',
        print 'output2: ' + sentence_posmerged_ner_str + '\n',
        output_file.write(sentence_posmerged_str + '\n',)
        output_file.write(sentence_posmerged_ner_str +'\n',)
        print '\n'

input_file.close()
output_file.close()
