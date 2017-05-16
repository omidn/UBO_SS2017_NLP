from nltk.corpus import stopwords, wordnet
from nltk.tokenize import word_tokenize
import string
from nltk.probability import FreqDist
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')


input_file_name = 'input.txt'

nltk_stopwords = set(stopwords.words('english'))

## source: http://xpo6.com/list-of-english-stop-words/
xpo6_stopwords = ["a", "about", "above", "above", "across", "after", "afterwards", "again", "against", "all", "almost", "alone",
                  "along", "already", "also","although","always","am","among", "amongst", "amoungst", "amount",  "an", "and",
                  "another", "any","anyhow","anyone","anything","anyway", "anywhere", "are", "around", "as",  "at", "back","be",
                  "became", "because","become","becomes", "becoming", "been", "before", "beforehand", "behind", "being", "below",
                  "beside", "besides", "between", "beyond", "bill", "both", "bottom","but", "by", "call", "can", "cannot", "cant",
                  "co", "con", "could", "couldnt", "cry", "de", "describe", "detail", "do", "done", "down", "due", "during", "each",
                  "eg", "eight", "either", "eleven","else", "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone",
                  "everything", "everywhere", "except", "few", "fifteen", "fify", "fill", "find", "fire", "first", "five", "for",
                  "former", "formerly", "forty", "found", "four", "from", "front", "full", "further", "get", "give", "go", "had", "has",
                  "hasnt", "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him",
                  "himself", "his", "how", "however", "hundred", "ie", "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its",
                  "itself", "keep", "last", "latter", "latterly", "least", "less", "ltd", "made", "many", "may", "me", "meanwhile", "might",
                  "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must", "my", "myself", "name", "namely", "neither",
                  "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of",
                  "off", "often", "on", "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out",
                  "over", "own","part", "per", "perhaps", "please", "put", "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems",
                  "serious", "several", "she", "should", "show", "side", "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone",
                  "something", "sometime", "sometimes", "somewhere", "still", "such", "system", "take", "ten", "than", "that", "the", "their", "them",
                  "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they", "thickv",
                  "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru", "thus", "to", "together", "too", "top", "toward",
                  "towards", "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us", "very", "via", "was", "we", "well", "were", "what",
                  "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether",
                  "which", "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "with", "within", "without", "would", "yet",
                  "you", "your", "yours", "yourself", "yourselves", "the"];

def removeStopWords(doc, dict):
    tokens = [word.lower() for word in word_tokenize(doc) if word not in string.punctuation]
    return [word for word in tokens if word not in dict]


with open(input_file_name, 'r') as f:
    ## part 1
    tokens = removeStopWords(f.read(), xpo6_stopwords)
    
    ## part 2 histogram
    fdist = FreqDist(word.lower() for word in tokens)
    # need to install this(http://matplotlib.org/users/installing.htm) in order to work.
    
    fdist.plot(30, cumulative=False)

    word = 'bugs'
    print 'frequency of word \'{}\' is {}'.format(word, fdist[word])

    ## part 3
    print wordnet.synsets('exhaust')
