import nltk
from nltk.stem.porter import PorterStemmer
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem import SnowballStemmer 
from nltk.corpus import stopwords
from pymongo import MongoClient
def get_tokens(stem):
		
	#with open('/home/akash/Downloads/a.txt') as stem:
	#stem="it was A the best of times it was the worst of times it was the age of wisdom it was the age of foolishness"
	tokens = nltk.word_tokenize(stem.lower())
	return tokens

def do_stemming(filtered):
	stemmed = []
	for f in filtered:
		stemmed.append(PorterStemmer().stem(f))
	return stemmed

def f4(seq): 
   # order preserving
   noDupes = []
   [noDupes.append(i) for i in seq if not noDupes.count(i)]
   return noDupes

if __name__ == "__main__":
        client = MongoClient()
        db = client.mydb.Iphone6s
        result=db.find()
        for i in result:
                stem=''
                stem = ''.join(i['Review'])
                tokens = get_tokens(stem)
                ##print("tokens = %s\n\n") %(tokens)
                tokens1 = [w for w in tokens if not w in stopwords.words('english')]
                stemmed_tokens = do_stemming(tokens1)
                print("stemmed_tokens = %s\n\n") %stemmed_tokens
                abc=f4(stemmed_tokens)
                print abc,"\n\n"
                tc=len(stemmed_tokens)
                wordfreq = []
                for w in stemmed_tokens:
                        wordfreq.append(stemmed_tokens.count(w))
                result=dict(zip(stemmed_tokens, wordfreq))
                print "Pairs\n = %s" %(result)
                tf=[]
                for w in stemmed_tokens:
                        tf.append(float(result[w])/tc)
                result1=dict(zip(stemmed_tokens,tf))
                print "Pairs1\n = %s" %result1  
