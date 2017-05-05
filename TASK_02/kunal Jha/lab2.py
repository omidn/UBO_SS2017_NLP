import nltk
from nltk.corpus import stopwords
import collections, re
from nltk.corpus import wordnet as wn


#counting bag of words vector
def printbagofwords(abc):
    bagsofwords = [ collections.Counter(re.findall(r'\w+', txt))
            for txt in filtered_sentence]
    sumbags = sum(bagsofwords, collections.Counter())

    print(sumbags)
    return

def givesenseWornet(word):
    print(wn.synsets(word))
    return


#Extract the original set of words
stop_words = set(stopwords.words("english"))
file =  open("abc.txt","r")
abc = file.readline()
all_word_tokens = nltk.word_tokenize(abc)
#add additional stop words
stop_words.update(('capital', 'European','Union'))
#Check to remove stop words
filtered_sentence = [w for w in all_word_tokens if not w in stop_words]
print(all_word_tokens)

print(filtered_sentence)
printbagofwords(filtered_sentence)
givesenseWornet('Berlin')







