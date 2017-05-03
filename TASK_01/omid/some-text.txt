import nltk
from nltk.tokenize import word_tokenize
from nltk.chunk import ne_chunk
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')

FILE_PATH = 'some-text.txt'
OUTPUT1_PATH = 'output1.txt'
OUTPUT2_PATH = 'output2.txt'
    
def format_output(entry):
    if type(entry) is nltk.tree.Tree:
        return '_'.join([x[0] for x in list(entry)]) + '_NER' 
    elif entry[1] in ['VERB', 'NOUN']:
        return entry[0] + '_' + entry[1].upper()
    return entry[0]

with open(FILE_PATH, 'r') as file, open(OUTPUT1_PATH, 'w') as file_output1, open(OUTPUT2_PATH, 'w') as file_output2:

    for line in file:
        tokens = word_tokenize(line)
    
        without_ner =  [tag for tag in nltk.pos_tag(tokens, tagset='universal')]
        ner =  ne_chunk(without_ner, binary=False)
    
        output1 =  ' '.join([format_output(chunk) for chunk in without_ner])
        output2 = ' '.join([format_output(chunk) for chunk in ner])
    
        file_output1.write(output1)
        file_output2.write(output2)

    print 'Operation completed. Please check \'{}\' and \'{}\' files.'.format(OUTPUT1_PATH,OUTPUT2_PATH)
