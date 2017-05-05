import nltk as nl

def replace_at_index(tup, ix, val):
    lst = list(tup)
    lst[ix] = val
    return tuple(lst)


def merger(sents):
    merged_tag = []
    for s in sents:
        new_sent = []
        for tag in s:
            if tag[1] in ['NN', 'NNS', 'NNP', 'NNPS']:
                new_sent.append(replace_at_index(tag, 1, 'NOUN'))
            elif tag[1] in ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']:
                new_sent.append(replace_at_index(tag, 1, 'VERB'))
            elif tag[1] == '.':
                new_sent.append(replace_at_index(tag, 1, 'DOT'))
            else:
                new_sent.append(replace_at_index(tag, 1, ''))
        merged_tag.append(output_sentence(new_sent))

    return merged_tag


def make_doc_list():
    tokenizer = nl.data.load('tokenizers/punkt/english.pickle')
    fp = open("myText.txt")
    data = fp.read()
    return tokenizer.tokenize(data)


def output_sentence(token):
    text = ''
    for tag in token:
        if text != '':
            if tag[1] != '':
                if tag[1] != 'DOT':
                    text += ' ' + tag[0] + "_" + tag[1]
                else:
                    text += tag[0] + '\n'
            else:
                text += ' ' + tag[0]
        else:
            if tag[1] != '':
                if tag[1] != 'DOT':
                    text += tag[0] + "_" + tag[1]
                else:
                    text += tag[0] + '\n'
            else:
                text += tag[0]
    return text


def my_tokenizer(doc_list):
    tagged_sent = []
    for sentence in doc_list:
        text = nl.word_tokenize(sentence)
        tags = nl.pos_tag(text)
        tagged_sent.append(tags)

    return tagged_sent


def file_output(sent_list, fileName):
    target = open(fileName, 'w')
    for sentence in sent_list:
        target.write(sentence)


def ner_merger(tagged_s):
    named_sents = []

    for s in tagged_s:
        text = ''
        namedEnt = nl.ne_chunk(s, binary=True)
        for i in range(len(namedEnt)):
            if text != '':
                if "NE" in str(namedEnt[i]):
                    text += ' ' + str(namedEnt[i][0][0]) + '_' + namedEnt[i].label()
                elif str(namedEnt[i][0]) != '.':
                    text += ' ' + str(namedEnt[i][0])
                else:
                    text += str(namedEnt[i][0]) + '\n'
            else:
                if "NE" in str(namedEnt[i]):
                    text += str(namedEnt[i][0][0]) + '_' + namedEnt[i].label()
                elif str(namedEnt[i][0]) != '.':
                    text += str(namedEnt[i][0])
                else:
                    text += str(namedEnt[i][0]) + '\n'
        named_sents.append(text)

    return named_sents


if __name__ == "__main__":
    doc_list = make_doc_list()
    tagged_s = my_tokenizer(doc_list)
    merged_tags = merger(tagged_s)
    # print(merged_tags)
    named_sent = ner_merger(tagged_s)

    file_output(merged_tags, "POS.txt")
    file_output(named_sent, "NER.txt")
